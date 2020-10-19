# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:32:55 2020

@author: mojdeh
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:50:16 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
import matplotlib.pyplot as plt  
import scipy.io    
    
## Define Variables
epsilon = 1.0           #Greed 100%
epsilon_min = 0.0005     #Minimum greed 0.05%
epsilon_decay = 0.7 #Decay multiplied with epsilon after each episode 
episodes = 1200      #Amount of games
max_steps = 300         #Maximum steps per episode 
learning_rate = 0.95
gamma = 0.5
T0 = 5;
##
result1 = np.zeros((T0+1))
result2 = np.zeros((T0+1))
for t in range(1,T0+1):
    DC_max = 10*t # 5
    DC_rem = DC_max*t
    val1 = 1
    maxS1 = 6*t
    val2 = 2
    maxS2 = 4*t
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
    statePath2 = np.zeros((episodes* max_steps))
    statePath3 = np.zeros((episodes* max_steps))
    stateOpt = np.zeros((episodes* max_steps))
    
    j = 0;    
    for episode in range(episodes):
        score = 0
        state = np.array([0,0,0])
        DC_rem = DC_max
        for k in range(max_steps):
            if DC_max - DC_rem > 0:
                deparRate = np.random.randint(1,100)
                DC_rem = DC_rem + (DC_max - DC_rem)* deparRate/100
            state[0] =  DC_rem
            state[1] =  np.random.randint(1,maxS1+1)
            state[2] =  np.random.randint(1,maxS2+1)
            Exp = np.random.randint(0,1000)/900
            if Exp > epsilon or episode> 900: 
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
            statePath2[j] = DC_rem;
            statePath3[j] = (action1*val1 + action2*val2)
            statePath[j] = (action1*val1 + action2*val2)/DC_rem
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
            stateOpt[j] = a
            if a == 0:
                a = 1
            state[0] = DC_rem
            
            statePath1[j] = (action1*val1 + action2*val2)/a
             
            if statePath1[j]>1 :
                statePath1[j] = 1
            j = j + 1
            
        # Reducing our epsilon each episode (Exploration-Exploitation trade-off)
        if epsilon >= epsilon_min:
            epsilon *= epsilon_decay
    result1[t] = np.mean(statePath3[900*300:1200*300])
    result2[t] = np.mean(stateOpt[900*300:1200*300])
xx = 200
ss = 0
plt.plot(list(range(ss,episodes* max_steps,xx)),statePath1[ss:episodes* max_steps:xx])
fig = plt.figure(figsize=(5, 5),dpi=100)
plt.plot(list(range(0,episodes* max_steps,1000)),np.mean(statePath.reshape(-1, 1000), axis=1))
a1 = statePath1[0:episodes* max_steps:300]

#scipy.io.savemat('test.mat', statePath1)
scipy.io.savemat('test.mat', {'mydata': statePath1})
#fig = plt.figure(figsize=(5, 5),dpi=100)
#hfont = {'fontname':'Times New Roman'}
#plt.plot(list(range(0,episodes* max_steps,1000)),np.mean(a1.reshape(-1,50),axis =1),'r')
#plt.title("Admission rate vs. Epoch number",fontsize=10,**hfont)
#plt.xlabel('Epoch Number ',fontsize=10,**hfont)
#plt.ylabel('Admission Rate',fontsize=10,**hfont)
#plt.xticks(fontsize=10)
#plt.yticks(fontsize=10)
#plt.show()