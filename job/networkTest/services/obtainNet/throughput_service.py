from ctypes import *
import os
class throughputService:
	def CfunctionReciever():
		path1 = os.getcwd() 
		sf = os.path.join(path1,"src2/libmain.so")
		functionC = CDLL(sf)
		functionC.func()
	def CfunctionTransmitter():
		path1 = os.getcwd() 
		sf = os.path.join(path1,"src2/libmain.so")
		functionC = CDLL(sf)
		functionC.func1()