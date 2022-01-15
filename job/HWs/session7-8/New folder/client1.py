import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:8080/")
print server.hello()
a = int(input("write"))
print server.findMark(a)
print server.RFile1()
server.WFile1(a)