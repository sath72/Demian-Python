from xml.etree.ElementTree import *

person=Element('Person') #root node
name=Element('name')
name.text='Demian'
person.append(name)
age=Element('age')
age.text='51'
person.append(age)
SubElement(person,'address').text='Milpitas'
no=Element('no')
no.text='7'
person.insert(0,no)
person.remove(no)
person.attrib['date']='2024-05-24'
dump(person)
ElementTree(person).write("/Users/Demian/Desktop/pythonproject/person.xml")