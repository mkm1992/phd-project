import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:8080/")

input_type = raw_input("type user \n")

if input_type == 'teacher':
	
	mark_math  =  int(raw_input("mark\n"))
	std_num = raw_input("std num \n")
	server.ChangeMark(str(std_num),str(mark_math))

elif input_type == 'student':
	std_num = raw_input("std num \n")
	server.ReadMark(str(std_num))

elif input_type == 'admin':
	server.AverageMark()