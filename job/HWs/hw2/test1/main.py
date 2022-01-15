# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:22:00 2021

@author: mojdeh
"""

import numpy as np
import os
#import textMining
 # write a question to open a text file and write this is line number i 
# open text file 
f= open("file3.txt","w")
n = np.random.randint(1,11)
for i in range(n):
     f.write("This is line %d\r\n" % (i+1))

#pth = os.getcwd()
#
#
#filelist = os.listdir(pth)
#for f1 in filelist:
#    if ".txt" in f1 and "file1" not in f1:
#        print(f1)
#        filename = f1
#
#
#User, Pass = textMining.find_user_pass(filename)
#string, str = textMining.find_json_file(filename)
#print(string)