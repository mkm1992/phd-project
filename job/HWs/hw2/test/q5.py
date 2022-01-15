import shutil
import os
import numpy as np

pth = os.path.join(os.getcwd(),"root")
if os.path.exists(pth):
    shutil.rmtree(pth)
name_folder = ["root","first", "second", "third","forth","fifth"]
for j in range(len(name_folder)):
    os.mkdir(name_folder[j])
    os.chdir(name_folder[j])
    for i in range(np.random.randint(1,10)):
        with open(str(np.random.randint(1,10))+".txt","w") as text:
            pass
counter = 0
for directory, folders, files in os.walk(pth):
    for textnames in files:
        counter +=  1
        print(textnames)
        if "0" in textnames: 
            os.rename(os.path.join(directory,textnames),os.path.join(directory,textnames.replace("0","_")))
    