import json
import os


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



folder_path = r"C:/Users/garvt/repos/projectx/Converter/data"
for filename in os.listdir(folder_path):
    fn = filename
    extension = os.path.splitext(filename)[1]
    print(f"The extension of {filename} is {extension}")
    # convert to JSON
    import xml.etree.ElementTree as ET
    tree = ET.parse(fn)
    root = tree.getroot()

    # convert XML to JSON
    json_data = {root.tag: {}}
    add_node_to_dict(root, json_data[root.tag])


    # Specify the path to the output file here
    output_file_path = "C:/Users/garvt/repos/projectx/Converter/output/file.json"

    # Write the JSON data to the output file
    with open(output_file_path, "w") as f:
        json.dump(json_data, f, indent=4)


