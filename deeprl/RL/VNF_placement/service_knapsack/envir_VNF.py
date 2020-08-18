"""
Created on Tue Aug  4 10:42:20 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
from itertools import combinations
class Env:
    def __init__(self, VNF, DC):
        self.VNF = VNF
        self.DC = DC
        self.NumVNF = len(VNF)
        self.NumDC = len(DC)
        self.state_size =  pow( self.NumDC+1, self.NumVNF) 
        self.action_size  =  self.NumVNF * self.NumDC
        self.Q = np.zeros((self.state_size, self.action_size))
        self.ValueState = np.zeros(self.state_size)
        self.S = np.zeros((self.state_size, self.state_size))
        self.State = np.zeros((self.state_size, self.NumVNF ))
    def place_ones(size, count):
        for positions in combinations(range(size), count):
            p = [0] * size
            for i in positions:
                p[i] = 1
    
            yield p
    def state_define(self):
        list_state = [];
        for i in range(0, self.NumVNF + 1):
            list_state += list(Env.place_ones(self.NumDC * self.NumVNF, i))
        self.State =  np.asarray(list_state)
        print(self.State)
        print(len(self.State))
        print(self.state_size)
                
    def available_state(self):
        for i in range(0, self.state_size):
            for j in range(0, self.state_size):
                if (i- j > 0) and ((Env.dec2bin(i) - Env.dec2bin(j)) == 1 or  np.log10(Env.dec2bin(i) - Env.dec2bin(j))% 1 == 0) :
                    self.S[self.state_size-i - 1][self.state_size -j - 1] = 1
        print(self.S)
    def choose_action(self, state):
        self.available_state() 
        self.state_define()
        actions = np.where(self.State[state][:]==0)
        return actions
    def next_state(self, state, action):
        possible_actions = self.choose_action(state)[0]
        #print('possible_actions')
        #print(possible_actions)
        state_new = 0
        if action not in possible_actions :
            state_new = state
        else:
            temp =  np.copy(self.State[state][:])
            print(temp)
            temp[action] = 1
            print(temp)
            for i in range(0, self.NumVNF):  
                state_new = state_new + temp[self.NumVNF - i -1] * pow(2,i)
        return int(state_new)
    def value_state(self):
        for i in range(0, self.state_size):
            temp = self.DC - np.dot(self.State[i], self.VNF)
            if temp < 0 :
                self.ValueState[i] = -10* pow(self.DC - np.dot(self.State[i], self.VNF),2) - 100 
            else :
                self.ValueState[i] = -2* pow(-self.DC + np.dot(self.State[i], self.VNF),2) + 100 
            self.ValueState[i] = self.DC - np.dot(self.State[i], self.VNF)
        print((self.ValueState))
    def get_reward(self, state, next_state):
        self.value_state()
        if self.S[state][next_state] == 1 :
            return self.ValueState[next_state] - self.ValueState[state]
        else:
            return 0 
    def done_action(self, state):
        done  = 1
        if np.sum(self.S[state]) == 0:
            done = 1
            print('done')
            return done
        else :
            for i in range(0, self.state_size):
                if self.S[state][i] == 1 :
                    reward = self.get_reward(state, i)
                    if reward > 0 :
                        done = 0
                        print('not done')

        return done
                        
                        
        
a = Env(np.array([4,5]), np.array([8,9]))    
a.state_define()                          
#print('choose_action') 
#print(a.choose_action(0)[0])  
#print('nextState')      
#print(a.next_state(6, 2))
#print('reward')
#print(a.get_reward(6,7))
#print(a.done_action(4))
###

#a = Env(np.array([4,5,3, 1]), np.array([10]))                              
#print('choose_action') 
#print(a.choose_action(4)[0])  
#print('nextState')      
#print(a.next_state(4, 2))
#print(a.get_reward(9,13))