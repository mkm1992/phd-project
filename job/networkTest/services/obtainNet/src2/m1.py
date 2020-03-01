from ctypes import *
sf = "/home/test/Desktop/cpp/ntttcp-for-linux/src2/libmain.so"
a = CDLL(sf)
list = a.func()
print(list)
