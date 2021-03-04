# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:11:30 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
import matplotlib.pyplot as plt

NumDC = 2;
NumVNF = 3;
state_size = 4
action_size = pow(NumDC, NumVNF)
DC = np.array([8, 9])
VNF = np.array([3, 4, 2])
Q = np.zeros((state_size, action_size))
R = np.zeros((state_size, action_size))
for i in range(0, state_size):
    for j in range(0, action_size):
        if 
    R[i,j] = 
epsilon = 0.2
if random.uniform(0, 1) < epsilon:
    1
else:
      Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])  