import signal
from ctypes import *



class TimeoutException(Exception):
	pass
def timeout_handler(signum, frame):
	raise TimeoutException
	signal.signal(signal.SIGALRM, timeout_handler)

TIMEOUT = 2
signal.alarm(TIMEOUT)    
try:
	sf = "/home/test/Desktop/cpp/ntttcp-for-linux/src2/libmain.so"
	a = CDLL(sf)
	list = a.func()
	signal.alarm(0)
except TimeoutException:
	print('function terminated')