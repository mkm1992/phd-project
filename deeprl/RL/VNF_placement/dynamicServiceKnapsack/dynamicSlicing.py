# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:30:27 2020

@author: Mojdeh Karbalaee
"""
import numpy as np

    
    
## Define Variables
epsilon = 1.0           #Greed 100%
epsilon_min = 0.005     #Minimum greed 0.05%
epsilon_decay = 0.9999 #Decay multiplied with epsilon after each episode 
episodes = 700      #Amount of games
max_steps = 100         #Maximum steps per episode 
learning_rate = 0.6
gamma = 0.65
##
DC_max = 5
DC_rem = DC_max
val1 = 1
maxS1 = 5
state_size = np.array((6,6))
max_action = 6
Q = np.zeros((state_size[0], state_size[1], max_action))
score = 0
state = np.array([0,0])
statePath = np.zeros((episodes* max_steps))
statePath1 = np.zeros((episodes* max_steps))
j = 0;
for episode in range(episodes):
    score = 0
    state = np.array([0,0])
    DC_rem = DC_max
    for k in range(max_steps):
        if DC_max - DC_rem > 0:
            deparRate = np.random.randint(0,50)
            DC_rem = DC_rem + (DC_max - DC_rem)* deparRate/100
        state[0] =  DC_rem
        state[1] =  np.random.randint(1,maxS1+1)
        if episode > 499: 
            action = np.argmax(Q[state[0],state[1], 0:state[1]+1])
            print(Q[state[0],state[1], :])
        else:
            actions =  list(range(0,state[1]+1))
            if len(actions) > 0 :
                act = np.random.randint(0,len(actions))
                action = actions[act]
                #print(action)

        # Step the game forward
        DC_rem =  DC_rem -  action 
        if DC_rem < 0:
            reward =  -100000
        else:
            reward =  pow(DC_rem,2)*(-10) +100
        if DC_rem < 0:
            DC_rem = 0
        # Add up the score
        score += reward
        stateN = DC_rem
        
            
        
        # Update our Q-table with our Q-function
        Q[state[0],state[1], action] = (1 - learning_rate) * Q[state[0],state[1], action] \
            + learning_rate * (reward + gamma * np.max(Q[int(stateN),state[1],:]))
        
           
        # Set the next state as the current state
        a = 0
        if state[1]> DC_rem:
            a = DC_rem
        else:
            a = state[1]
        if a == 0:
            a = 1
        state[0] = DC_rem
        statePath[j] = action/state[1]
        statePath1[j] = action/a
        j = j + 1
        
    # Reducing our epsilon each episode (Exploration-Exploitation trade-off)
    if epsilon >= epsilon_min:
        epsilon *= epsilon_decay
import matplotlib.pyplot as plt  
plt.plot(list(range(50000,episodes* max_steps,100)),statePath[50000:episodes* max_steps:100])
plt.show()    