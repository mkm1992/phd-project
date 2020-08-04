# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:55:26 2020

@author: Mojdeh Km
"""
import numpy as np
import matplotlib.pyplot as plt

NumDC = 1;
NumVNF = 3;
state_size = pow(2, NumVNF)
action_size = NumVNF
DC =  np.array([8])
VNF = np.array([6, 5, 3])
Q = np.zeros((state_size, action_size))
R = np.zeros((state_size, action_size))
S = np.zeros(state_size)
####
epsilon = 1.0           #Greed 100%
epsilon_min = 0.005     #Minimum greed 0.05%
epsilon_decay = 0.9 #Decay multiplied with epsilon after each episode 
episodes = 1000      #Amount of games
max_steps = 1000         #Maximum steps per episode 
learning_rate = 0.65
gamma = 0.65
##
for i in range(1, state_size+1):
    if i <= NumVNF:
        S[i] = 10 - VNF[i-1] + DC
    elif i == state_size-1:
        S[i] = DC - sum(VNF) - 10 
S[4] = -3 - 20
S[5] = -1 - 20
S[6] = 100
S[7] = -10
def nextState(action, state):
    if state == 0  :
        nextS =  action
    elif state in [4, 5, 6] and action == 7 - state :
        nextS = 7
    elif state in [1, 2, 3] and action != state :
        nextS = action + state + 1
    elif state == 7 :
        nextS = 7 - action
    else :
        nextS = state
    return nextS
done  = 0
statePath = np.zeros((episodes, max_steps))    
for episode in range(episodes):
 
    state = 0 #Gets current game state
    done = False        #decides whether the game is over
    score = 0
 
    for k in range(max_steps):
        statePath[episode, k] = state
        # With the probability of (1 - epsilon) take the best action in our Q-table
        if np.random.uniform(0, 1) > epsilon:
            action = np.argmax(Q[state, :])
        # Else take a random action
        else:
            action =  np.random.randint(1,4)
        
        # Step the game forward
        next_state = nextState(action, state)
        reward = S[next_state] - S[state] 
        if reward == 0:
            reward = -10
        if next_state == 7:
            reward = -50
        if state == 7 :
            reward  = -50
        if state == 6:
            done = 1
        # Add up the score
        score += reward
 
        # Update our Q-table with our Q-function
        Q[state, action-1] = (1 - learning_rate) * Q[state, action-1] \
            + learning_rate * (reward + gamma * np.max(Q[next_state,:]))
 
        # Set the next state as the current state
        state = next_state
 
        if done:
            break
        
    # Reducing our epsilon each episode (Exploration-Exploitation trade-off)
    if epsilon >= epsilon_min:
        epsilon *= epsilon_decay

