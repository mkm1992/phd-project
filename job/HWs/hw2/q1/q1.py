# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:49:19 2021

@author: Dr-ShahMansouri
"""

import numpy as np
import os
import textMining
 # write a question to open a text file and write this is line number i 
# open text file 
f= open("file1.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))

pth = os.getcwd()


filelist = os.listdir(pth)
for f1 in filelist:
    if ".txt" in f1 and "file1" not in f1:
        print(f1)
        filename = f1


User, Pass = textMining.find_user_pass(filename)
string, str = textMining.find_json_file(filename)
print(string)