# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:02:19 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
from envir_VNF import Env

## Define Variables
epsilon = 1.0           #Greed 100%
epsilon_min = 0.005     #Minimum greed 0.05%
epsilon_decay = 0.9 #Decay multiplied with epsilon after each episode 
episodes = 1000      #Amount of games
max_steps = 1000         #Maximum steps per episode 
learning_rate = 0.65
gamma = 0.65

## 