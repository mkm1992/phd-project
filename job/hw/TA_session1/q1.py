# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:16:59 2021

@author: Mojdeh
"""

import numpy as np

# 1:10 print

for i in range(1,11):
    print(i**2)

#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 1 and 100 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
    
l=[]
for i in range(10, 101):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

def fact(num):
    if num == 0 or num ==1:
        return 1
    else:
        return(num*fact(num-1))
fact(8)

#### dictionary i, 10*i
d = dict()
for i in range(1,5):
    d[i] = 10*i
print(d)

######


#Question:
#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))

###########

f= open("a.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()      
#####################
     
# a file named "geek", will be opened with the reading mode.
file = open('a.txt', 'r')
# This will print every line one by one in the file
for line in file:
    print (line)
    
#########################
    
    
#### prime number
prime_numbers = 0

def is_prime_number(x):
    flag = 0
    if (x >= 2):
        for i in range(2,int(x/2)):
            if  x % i == 0:
                flag =1
                break
    if flag == 1:
        print("no prime")
    else:
        print("prime")
    return flag

is_prime_number(2)
is_prime_number(10)
is_prime_number(7)

##############

def fib(num) :
    if num == 1 or num ==0 :
        return 1        
    else:
        return fib(num-2) + fib(num-1)
fib(4)


################# BMM
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
  

print (gcd(12,18))