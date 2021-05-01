# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:36:41 2021

@author:Mojdeh
"""

import shutil
import os
import numpy as np

pth=os.path.join(os.getcwd(),"root")  #Root Folder Path
if os.path.exists(pth):
    shutil.rmtree(pth)  #To Remove Root Folder if Exists

name_folder=["root", "first", "second", "third", "forth", "fifth"] 
for j in range(6):
    os.mkdir(name_folder[j])
    os.chdir(name_folder[j])
    for i in range(np.random.randint(1,100)):
        with open(str(np.random.randint(100)) + ".txt", "w") as text: #to create an empty txt file
            pass

#for directory, folders, files in os.walk(pth): #To search in Root directory
#    for Textnames in files:
#        if "0" in Textnames:
#            os.rename(os.path.join(directory, Textnames), os.path.join(directory, Textnames.replace("0", "_")))