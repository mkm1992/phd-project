# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:13:14 2021

@author: 
"""

def find_user_pass(name):
    lines = []  # Declare an empty list.
    with open(name, 'rt') as myfile:  # Open lorem.txt for reading text.
        for myline in myfile:  # For each line in the file,
            lines.append(myline.rstrip('\n'))  # strip newline and add to list.
    for element in lines:  # For each element in the list,
        if 'User:' in element:
            User = element.replace('User: ', '')
        if 'Pass:' in element:
            Pass = element.replace('Pass: ', '')
    print(User, Pass)
    return User, Pass



import re



def find_json_file(name):
    with open(name, 'rt') as myFile:  # Open lorem.txt for reading text.
        data = myFile.readlines()
    print(data)
    print('------------')
    str = ''
    for i in range(len(data)):
        str = str + data[i]
    print(str)
    print('------------')
    str1 = re.findall(r'\[(.*?)\]', str)
    return str1 , str

def sum1(a,b):
    return (a+b)