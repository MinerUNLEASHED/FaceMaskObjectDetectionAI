import xml.etree.ElementTree as ET
import os

def convert_xml_to_yolo(xml_file_path, output_folder):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    filename = root.find('filename').text
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)

    yolo_output = ""
    for obj in root.findall('object'):
        class_name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        x_center = (xmin + xmax) / 2.0 / width
        y_center = (ymin + ymax) / 2.0 / height
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        if class_name == "with_mask":
            class_name = 0
        elif class_name == "without_mask":
            class_name = 1
        else:
            class_name = 2

        yolo_output += f"{class_name} {x_center} {y_center} {bbox_width} {bbox_height}\n"

    output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
    with open(output_file_path, 'w') as f:
        f.write(yolo_output)

def batch_convert_xml_to_yolo(xml_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith(".xml"):
            xml_file_path = os.path.join(xml_folder, xml_file)
            convert_xml_to_yolo(xml_file_path, output_folder)

xml_folder = r"insert/xml/files/folder/here"
output_folder = r"insert/output/folder/here"
batch_convert_xml_to_yolo(xml_folder, output_folder)
