import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:8080/")
print server.hello()
#a = int(input("write number\n"))

input_type = raw_input("name\n")
print input_type
if input_type== 'teacher':
	mark_math = int(raw_input("mark\n"))
	std_num = raw_input("std number\n")
	server.ChangeMark(str(std_num), str(mark_math))
elif input_type == 'student':
	std_num = raw_input("std number\n")
 	server.ReadMark(str(std_num))
elif input_type == 'admin':
	server.AverageMark()

