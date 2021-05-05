import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)


for child in root:
    print(child.tag, child.attrib)

for elem in root:
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
    


for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write('output.xml')


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
