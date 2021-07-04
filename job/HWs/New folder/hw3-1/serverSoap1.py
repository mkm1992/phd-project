import SOAPpy
import xml.etree.ElementTree as ET 


def ChangeMark(str1, math):
	tree = ET.parse('std.xml')
	root = tree.getroot()
	student = tree.findall('student')
	count = 0
	for child in root:
		stdNum = child.attrib
		if stdNum['std_num'] == str1:
			countStd = count
		count += 1
	student[countStd].find('mark').text = math
	print student[countStd].find('mark').text
	tree.write('std.xml')
def ReadMark(std_num):
	tree = ET.parse('std.xml')
	root = tree.getroot()
	student = tree.findall('student')
	count = 0
	for child in root:
		stdNum = child.attrib
		if stdNum['std_num'] == std_num:
			countStd = count
		count += 1
	print student[countStd].find('mark').text
def AverageMark():
	tree = ET.parse('std.xml')
	root = tree.getroot()
	count = 0
	sum_mark  = 0
	for mark in root.iter('mark'):
		sum_mark = int(mark.text) + sum_mark
		count = count + 1
	print "mean:"
	print sum_mark/count

server = SOAPpy.SOAPServer(("localhost",8080))
server.registerFunction(ChangeMark)
server.registerFunction(AverageMark)
server.registerFunction(ReadMark)
server.serve_forever()		