import tkinter as tk
from tkinter import filedialog
import os
import json
import xml.etree.ElementTree as ET

#converts XML to JSON
def add_node_to_dict(node, dictionary):
    # add node attributes as dictionary items
    for key, value in node.items():
        dictionary[key] = value

    # add child nodes as dictionary items
    if len(node):
        for child in node:
            child_dict = {}
            add_node_to_dict(child, child_dict)
            if child.tag in dictionary:
                # convert existing value to a list if necessary
                existing = dictionary[child.tag]
                if not isinstance(existing, list):
                    existing = [existing]
                    dictionary[child.tag] = existing
                existing.append(child_dict)
            else:
                dictionary[child.tag] = child_dict
    else:
        # add text content as dictionary value
        dictionary[node.tag] = node.text

def convert_xml_to_json(input_file_path, output_file_path):
    # read input XML file
    tree = ET.parse(input_file_path)
    root = tree.getroot()

    # convert XML to JSON
    json_data = {root.tag: {}}
    add_node_to_dict(root, json_data[root.tag])

    # write JSON data to JSON file
    with open(output_file_path, "w") as f:
        json.dump(json_data, f, indent=4)

def main():
    # create Tkinter UI
    root = tk.Tk()
    root.withdraw()  # hide the Tkinter window

    # select input XML file
    input_file_path = filedialog.askopenfilename(
        title="Select XML file",
        filetypes=(("XML files", "*.xml"), ("all files", "*.*"))
    )

    # check if file is selected
    if not input_file_path:
        return

    # create output folder if it doesn't exist
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # create output file path
    input_file_name = os.path.basename(input_file_path)
    output_file_name = os.path.splitext(input_file_name)[0] + ".json"
    output_file_path = os.path.join(output_folder, output_file_name)

    # convert XML to JSON and save to output file
    convert_xml_to_json(input_file_path, output_file_path)

    # display message box to confirm output file location
    message = f"File converted successfully!\nOutput file saved to {output_file_path}"
    tk.messagebox.showinfo("File Conversion", message)

if __name__ == "__main__":
    main()
