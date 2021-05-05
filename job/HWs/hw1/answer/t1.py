# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 09:44:50 2021

@author: Mojdeh
"""

import numpy as np

#x = (input("Enter 3 marks \n").split())
#num = []
#a = float(x[0])
#b = float(x[1])
#c = int(x[2])
#print(a + b + c)


##############

x = (input("Enter 3 marks \n").split())
num = []
for i in range(3):
    num.append(float(x[i]))
print(sum(num))


product_result = 1;
for x in num:
    product_result = product_result * x
print(product_result)

print(sum(num)/3)

average = sum(num)/3
if average > 18 :
    print("A")
elif average > 16:
    print("B")
else:
    print("C")