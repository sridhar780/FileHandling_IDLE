import xml.etree.ElementTree as ET

# Function to read an XML file
def read_xml(file_path):
    tree = ET.parse('C:\\Users\\SYS28\\Desktop\\test.xml')
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
