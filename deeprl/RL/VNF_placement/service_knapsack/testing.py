# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:59:58 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
s = np.array([[1,0],[1,1],[0,1]])
s1 = np.zeros((8,2))
num = 0
for i  in range(0, 3) :
    k = sum(s[i])
    s1[num:num +k*2] = s[i]
    for j in range(0, 2) :
        if s[i][j] == 1 :
            for t in range(1,3):
                s1[num][j] =  t
                num +=1
print(s1)

a = np.array([1,0,1])
numState = 2
nActive = sum(a)
b = np.zeros((4,3)) + a
c = np.where(a==1)
for i in c[0]:
    for i in range(0, 4) : 
            j = 0
            temp = int(bin(i)[2:])
            while temp > 0 :
                b[i][self.NumVNF-1- j] = temp % 10
                temp = int(temp /10)
                j = j +1
    
from itertools import combinations
n = 0
a = combinations([0,1,2,3],3)
for i in list(a):
    print(i)
    n +=1
print(n)


from itertools import combinations


def place_ones(size, count):
    for positions in combinations(range(size), count):
        p = [0] * size

        for i in positions:
            p[i] = 1

        yield p

a =list(place_ones(4, 2))




def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base
    base_num = base_num[::-1]  #To reverse the string
    return base_num






