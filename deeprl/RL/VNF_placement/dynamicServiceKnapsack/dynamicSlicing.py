# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:30:27 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
import matplotlib.pyplot as plt  
    
    
## Define Variables
epsilon = 1.0           #Greed 100%
epsilon_min = 0.0005     #Minimum greed 0.05%
epsilon_decay = 0.99 #Decay multiplied with epsilon after each episode 
episodes = 6000      #Amount of games
max_steps = 100         #Maximum steps per episode 
learning_rate = 0.6
gamma = 0.65
##
DC_max = 10 # 5
DC_rem = DC_max
val1 = 1
maxS1 = DC_max
aSize = maxS1 +1
state_size = np.array((aSize,aSize))
max_action = aSize
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
            deparRate = np.random.randint(1,20)
            DC_rem = DC_rem + (DC_max - DC_rem)* deparRate/100
        state[0] =  DC_rem
        state[1] =  np.random.randint(1,maxS1+1)
        Exp = np.random.randint(0,1000)/1000
        if Exp > epsilon or episode> 5700: 
            action = np.argmax(Q[state[0],state[1], 0:state[1]+1])
            #print(Q[state[0],state[1], :])
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
        if state[1]> state[0]:
            a = state[0]
        else:
            a = state[1]
        if a == 0:
            a = 1
        state[0] = DC_rem
        statePath[j] = action/state[1]
        statePath1[j] = action/a
        if statePath1[j]>1 :
            statePath1[j] = 0.5
        j = j + 1
        
    # Reducing our epsilon each episode (Exploration-Exploitation trade-off)
    if epsilon >= epsilon_min:
        epsilon *= epsilon_decay

#plt.plot(list(range(0,episodes* max_steps,100)),statePath1[0:episodes* max_steps:100])
#plt.plot(list(range(0,episodes* max_steps,100)),np.mean(statePath1.reshape(-1, 100), axis=1))
a1 = statePath1[0:episodes* max_steps:100]
fig = plt.figure(figsize=(5, 5),dpi=100)
hfont = {'fontname':'Times New Roman'}
plt.plot(list(range(0,episodes* max_steps,5000)),np.mean(a1.reshape(-1,50),axis =1),'r')
plt.title("Admission rate vs. Epoch number",fontsize=10,**hfont)
plt.xlabel('Epoch Number ',fontsize=10,**hfont)
plt.ylabel('Admission Rate',fontsize=10,**hfont)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
#plt.ylim([0,0.015])
plt.show()