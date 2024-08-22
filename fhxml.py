import xml.etree.ElementTree as ET

# Function to read an XML file
def read_xml(file_path):
    tree = ET.parse('C:\\Users\\SYS28\\Desktop\\test.xml')
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)

# Function to write to an XML file
def write_xml(file_path):
    root = ET.Element("data")
    item1 = ET.SubElement(root, "item", attrib={"name": "item1"})
    item1.text = "This is item 1"
    item2 = ET.SubElement(root, "item", attrib={"name": "item2"})
    item2.text = "This is item 2"

    tree = ET.ElementTree(root)
    tree.write(file_path)

# Specify the file path
file_path = "test.xml"

# Write to the XML file
write_xml(file_path)

# Read from the XML file
read_xml(file_path)
