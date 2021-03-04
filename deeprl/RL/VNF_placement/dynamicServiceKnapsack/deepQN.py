# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:10:38 2020

@author: Mojdeh Karbalaee
"""

import numpy as np
import matplotlib.pyplot as plt  
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from keras import datasets, layers, models
import tensorflow as tf
    
## Define Variables
epsilon = 1.0           #Greed 100%
epsilon_min = 0.0005     #Minimum greed 0.05%
epsilon_decay = 0.99 #Decay multiplied with epsilon after each episode 
episodes = 100      #Amount of games
max_steps = 300         #Maximum steps per episode 
learning_rate = 0.6
gamma = 0.65
##
DC_max = 11 # 5
DC_rem = DC_max
val1 = 1
maxS1 = 3
val2 = 2
maxS2 = 3
aSize1 = maxS1 +1
aSize2 = maxS2 +1
aSize0 = DC_max + 1
state_size = np.array((aSize0,aSize1,aSize2))
max_action = np.array((aSize1,aSize2))
Q = np.zeros((state_size[0], state_size[1], state_size[2], max_action[0], max_action[1]))
score = 0
state = np.array([0,0,0])
statePath = np.zeros((episodes* max_steps))
statePath1 = np.zeros((episodes* max_steps))
##
model = models.Sequential()
model.add(layers.Conv3D(4, (3, 3, 3), activation='relu', input_shape=( state_size[0], state_size[1], state_size[2],1)))
model.add(layers.MaxPooling3D((2, 2, 2)))
model.add(Activation('relu'))
#model.add(layers.Reshape((-1, 4)))
model.add(Flatten())
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(layers.Reshape((max_action[0], max_action[1])))
#model.add(Dense(max_action[0], max_action[1]))
#model.add(layers.Conv3D(64, (3, 3, 3), activation='relu'))
#model.add(layers.MaxPooling3D((3, 3, 3)))
#model.add(layers.Conv3D(64, (3, 3, 3), activation='relu'))
print(model.summary())
model.compile(loss='mse', optimizer=Adam(lr=learning_rate))
######################
j = 0;
for episode in range(episodes):
    score = 0
    state = np.array([0,0,0])
    DC_rem = DC_max
    for k in range(max_steps):
        if DC_max - DC_rem > 0:
            deparRate = np.random.randint(1,20)
            DC_rem = DC_rem + (DC_max - DC_rem)* deparRate/100
        state[0] =  DC_rem
        state[1] =  np.random.randint(1,maxS1+1)
        state[2] =  np.random.randint(1,maxS2+1)
        Exp = np.random.randint(0,1000)/1000
        if Exp > epsilon: #or episode> 6000: 
            temp1 = np.zeros([1,12,4,4,1])
            temp1[0][state[0]][state[1]][state[2]][0] = 1
            temp2 = model.predict(temp1)
            ind = np.unravel_index(np.argmax(temp2, axis=None), temp2.shape)
            action1 = ind[0]
            action2 = ind[1]
            #action = np.argmax(model.predict(temp1))
            #action = np.argmax(Q[state[0],state[1], state[2], 0:state[1]+1, 0:state[2]+1])
            #print(Q[state[0],state[1], :])
        else:
            actions1 =  list(range(0,state[1]+1))
            actions2 =  list(range(0,state[2]+1))
            if len(actions1) > 0 or len(actions2) > 0 : 
                act1 = np.random.randint(0,len(actions1))
                act2 = np.random.randint(0,len(actions2))
                action1 = actions1[act1]
                action2 = actions2[act2]
                #print(action)

        # Step the game forward
        DC_rem =  DC_rem -  action1*val1 - action2*val2 
        if DC_rem < 0:
            reward =  -100000
        else:
            reward =  pow(DC_rem,2)*(-10) + 50 #+200
        if DC_rem < 0:
            DC_rem = 0
        # Add up the score
        score += reward
        stateN = DC_rem
        temp11 = np.zeros([1,12,4,4,1])
        temp11[0][int(stateN)][state[1]][state[2]][0] = 1
        temp22 = model.predict(temp11)
        temp1 = np.zeros([1,12,4,4,1])
        temp1[0][state[0]][state[1]][state[2]][0] = 1
        target = (reward + gamma * np.max(temp22))
        target_vec = model.predict(temp1)[0]
        target_vec[action1][action2] = target
        tr = np.reshape(target_vec,(1,4,4,1))
        model.fit(temp1, tr, epochs=1, verbose=0)    
        
        # Update our Q-table with our Q-function
        #Q[state[0],state[1],  state[2], action1, action2] = (1 - learning_rate) * Q[state[0],state[1],  state[2], action1, action2] \
        #    + learning_rate * (reward + gamma * np.max(Q[int(stateN),state[1],:,:]))
        
           
        # Set the next state as the current state
        a = 0
        if state[1]*val1 + state[2]* val2> state[0]:
            a = state[0]
        else:
            a = int(state[0]/2) + int(state[0]/4) 
        if a == 0:
            a = 1
        state[0] = DC_rem
        statePath[j] = (action1*val1 + action2*val2)/state[1]
        statePath1[j] = (action1*val1 + action2*val2)/a
        if statePath1[j]>1 :
            statePath1[j] = 1
        j = j + 1
        
    # Reducing our epsilon each episode (Exploration-Exploitation trade-off)
    if epsilon >= epsilon_min:
        epsilon *= epsilon_decay

plt.plot(list(range(0,episodes* max_steps,300)),statePath1[0:episodes* max_steps:300])
fig = plt.figure(figsize=(5, 5),dpi=100)
plt.plot(list(range(0,episodes* max_steps,300)),np.mean(statePath1.reshape(-1, 300), axis=1))
# a1 = statePath1[0:episodes* max_steps:300]
# fig = plt.figure(figsize=(5, 5),dpi=100)
# hfont = {'fontname':'Times New Roman'}
# plt.plot(list(range(0,episodes* max_steps,15000)),np.mean(a1.reshape(-1,50),axis =1),'r')
# plt.title("Admission rate vs. Epoch number",fontsize=10,**hfont)
# plt.xlabel('Epoch Number ',fontsize=10,**hfont)
# plt.ylabel('Admission Rate',fontsize=10,**hfont)
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.show()
