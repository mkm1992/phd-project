# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:22:05 2021

@author: Mojdeh
"""
num = []
new_num = 1
while new_num != 0:
    new_num =  int(input('number '))
    if new_num != 0 :
        num.append(new_num)
print(num)

for i in range(len(num)):
    for j in range(len(num)-1):
        if num[j] > num[j + 1]:
            #swapping
            num[j], num[j + 1] = num[j + 1], num[j]
print(num)