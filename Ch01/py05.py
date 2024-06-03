import xml.etree.ElementTree as ET
tree=ET.parse("/Users/Demian/Desktop/pythonproject/person.xml")
root=tree.getroot()
print(root.tag)
for i in root:
    print(i.tag, i.text)