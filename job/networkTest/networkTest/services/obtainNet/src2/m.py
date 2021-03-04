from ctypes import *
sf = "/home/test/Desktop/networkTest/services/obtainNet/src2/libmain.so"
a = CDLL(sf)
a.func1()

