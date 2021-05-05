# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:08:42 2021

@author: Mojdeh
"""
dict1 = dict()
for i in range(1, 16):
    dict1[i] = i**2
    
print(dict1)

dict2 = dict() 
for i in range(1, 11):
    name = input("name  ")
    number = input("number  ")
    dict2[name] = number

print(dict2)