import SOAPpy
def hello():
    return "Hello World mojdeh"
def findMark(num):
	return str(num+1)
def RFile1():
	f = open("1.txt", "r")
	a = f.read()
	return a
def WFile1(x):
	f = open("1.txt", "a")
	f.write(str(x))
	f.close()
server = SOAPpy.SOAPServer(("localhost", 8080))
server.registerFunction(hello)
server.registerFunction(findMark)
server.registerFunction(RFile1)
server.registerFunction(WFile1)
server.serve_forever()