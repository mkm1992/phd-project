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
epsilon_decay = 0.9999 #Decay multiplied with epsilon after each episode 
episodes = 2500      #Amount of games
max_steps = 10         #Maximum steps per episode 
learning_rate = 0.5
gamma = 0.65

## 
env1 = Env(np.array([4,5,3,1]), np.array([12,13])) 
#env1.available_state() 
env1.state_define()
env1.value_state()
Q = np.zeros((env1.state_size, env1.action_size))
statePath = np.zeros((episodes, max_steps))    
for episode in range(episodes):
 
    state = 0 #Gets current game state
    done = False        #decides whether the game is over
    score = 0
 
    for k in range(max_steps):
        statePath[episode, k] = state
        # With the probability of (1 - epsilon) take the best action in our Q-table
        done = env1.done_action(state)
        if done:
            break
        if episode > 2000: #np.random.uniform(0, 1) > epsilon: #episode > 1800: 
            action = np.argmax(Q[state, :])
        # Else take a random action
        else:
            actions =  env1.choose_action(state)
            if len(actions) > 0 :
                act = np.random.randint(0,len(actions[0]))
                action = actions[0][act]
                #print(action)

        # Step the game forward
        next_state = env1.next_state(state, action)
        reward =  env1.get_reward(state, next_state) 

        # Add up the score
        score += reward
 
        # Update our Q-table with our Q-function
        Q[state, action] = (1 - learning_rate) * Q[state, action] \
            + learning_rate * (reward + gamma * np.max(Q[next_state,:]))
 
        # Set the next state as the current state
        state = next_state

        
    # Reducing our epsilon each episode (Exploration-Exploitation trade-off)
    if epsilon >= epsilon_min:
        epsilon *= epsilon_decay
      