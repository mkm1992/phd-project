# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:28:12 2020

@author: Mojdeh Karbalaee
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:50:16 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
import matplotlib.pyplot as plt  
from keras.models import Sequential
#from keras.layers import Dense, Activation, Flatten
#from keras.optimizers import Adam
#from keras import datasets, layers, models
#import tensorflow as tf
    
## Define Variables
epsilon = 1.0           #Greed 100%
epsilon_min = 0.0005     #Minimum greed 0.05%
epsilon_decay = 0.99 #Decay multiplied with epsilon after each episode 
episodes = 3000      #Amount of games
max_steps = 300         #Maximum steps per episode 
learning_rate = 0.6
gamma = 0.65
##
DC_max = 12 # 5
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
input_shape =(4, state_size[0], state_size[1], state_size[2], 1)
x = tf.random.normal(input_shape)
y = tf.keras.layers.Conv3D(
2, 3, activation='relu', input_shape=input_shape[1:])(x)

model = Sequential()
model.add(Flatten(input_shape=(4, state_size[0], state_size[1], state_size[2])))
model.add(layers.Conv2D(13, (4,4), activation='relu', input_shape=(state_size[0], state_size[1], state_size[2],1)))
model.add(Activation('relu'))
model.add(Dense([16,16,16]))
model.add(Activation('relu'))
model.add(Dense([16,16,16]))
model.add(Activation('relu'))
model.add(Dense(max_action[0], max_action[1]))
model.add(Activation('linear'))
model.compile(loss='mse', optimizer=Adam(lr=learning_rate))
print(model.summary())
##
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
            action = np.argmax(Q[state[0],state[1], state[2], 0:state[1]+1, 0:state[2]+1])
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
        
            
        
        # Update our Q-table with our Q-function
        Q[state[0],state[1],  state[2], action1, action2] = (1 - learning_rate) * Q[state[0],state[1],  state[2], action1, action2] \
            + learning_rate * (reward + gamma * np.max(Q[int(stateN),state[1],state[2],:,:]))
        
           
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
a1 = statePath1[0:episodes* max_steps:300]
fig = plt.figure(figsize=(5, 5),dpi=100)
hfont = {'fontname':'Times New Roman'}
plt.plot(list(range(0,episodes* max_steps,15000)),np.mean(a1.reshape(-1,50),axis =1),'r')
plt.title("Admission rate vs. Epoch number",fontsize=10,**hfont)
plt.xlabel('Epoch Number ',fontsize=10,**hfont)
plt.ylabel('Admission Rate',fontsize=10,**hfont)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()