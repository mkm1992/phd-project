import xml.etree.ElementTree as ET

tree = ET.parse('std.xml')
root = tree.getroot()
print(root.tag)

count = 0
for child in root:
    print(child.tag, child.attrib)
    count+=1

for elem in root:
   #ET.Element('child', num=str(1))
   for subelem in elem:
      print(subelem.text)

print(root[0][1].text)      
print('---------------------')

student = tree.findall('student')
print('student count:', len(student))

for std in student:
    print('Name: ', std.find('name').text)
    print('Email: ', std.find('email').text)
    print('Phone: ', std.find('phone').text)
    data = ET.Element('child', num=str(std))
    print(data)
    root.extend(data)
    


for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write('output.xml')



children = [
    ET.Element('child', num=str(i))
    for i in range(3)
    ]

root.extend(children)


count = 0
for child in root:
    #print(child.tag, child.attrib)
    math = ET.Element("math")
    data = ET.SubElement(math, "10")
    #root.insert(1,data)
    #ET.dump(root)
tree = ET.ElementTree(root)
tree.write('2.xml')
#tree = ET.parse('output.xml')
#root = tree.getroot()
#print(root.tag)
#
#for student in root.findall('student'):
#    rank = int(student.find('rank').text)
#    if rank > 9:
#        root.remove(student)
#
#tree.write('output1.xml')
