import SOAPpy
import xml.etree.ElementTree as ET



def ChangeMark(str1, math):
	tree = ET.parse('std.xml')
	root = tree.getroot()
	print(root.tag)
	student = tree.findall('student')
	count = 0
	for child in root:
		stdNum =child.attrib
		if stdNum['std_num'] == str1:
			counterStd = count
		count+= 1
	student[counterStd].find('mark').text =  math
	print student[counterStd].find('mark').text 
	tree.write('std.xml')

def hello():
    return "Hello World mojdeh"
def ReadMark(std_num):
	tree = ET.parse('std.xml')
	root = tree.getroot()
	print(root.tag)
	student = tree.findall('student')
	count = 0
	for child in root:
		stdNum =child.attrib
		if stdNum['std_num'] == std_num:
			counterStd = count
		count+= 1
	print "your Mark :"
	print student[counterStd].find('mark').text 

def AverageMark():
	tree = ET.parse('std.xml')
	root = tree.getroot()
	print(root.tag)
	student = tree.findall('student')
	count = 0
	sum_mark =  0
	for mark in root.iter('mark'):
		sum_mark = int(mark.text) + sum_mark
		count  = count + 1
	print "mean:"
	print sum_mark/count 

server = SOAPpy.SOAPServer(("localhost", 8080))
server.registerFunction(hello)
server.registerFunction(ChangeMark)
server.registerFunction(ReadMark)
server.registerFunction(AverageMark)
server.serve_forever()





