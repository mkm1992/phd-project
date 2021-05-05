import numpy as np
import os
import text_mine

f = open("file.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n"%(i+1))

pth = os.getcwd()
filelist = os.listdir(pth)
for f1 in filelist:
    if ".txt" in f1 and "file" not in f1:
        print(f1)
        filename = f1
User, Pass = text_mine.find_user_pass(filename)

string, str = text_mine.find_json_file(filename)
