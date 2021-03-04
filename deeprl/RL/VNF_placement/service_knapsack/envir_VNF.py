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
        np_listState =  np.asarray(list_state)
        num = []
        x = np.size(np_listState,axis =0)
        for i in range(0,x):
            b = np.array(np_listState[i])
            for j in range(0,self.NumVNF):
                vector = np.arange(j, self.action_size , self.NumVNF)
                if sum(b[vector]) > 1:
                    num = np.append(num, i)
                    #a = np.delete(a,i,0)
        num = num.astype(int)
        self.State =  np.delete(np_listState,num,0) 
        print(self.State)
        print(len(self.State))
        self.state_size = len(self.State)
        print(self.state_size)
#    def available_state(self):
#        for i in range(0, self.state_size):
#            for j in range(0, self.NumVNF):
#                vector = np.arange(j, self.action_size , self.NumVNF)
#                if sum(self.State[i][vector]) == 0 :
#                    self.S[i][vector]
                
                
#    def available_state(self):
#        for i in range(0, self.state_size):
#            for j in range(0, self.state_size):
#                if (i- j > 0) and ((Env.dec2bin(i) - Env.dec2bin(j)) == 1 or  np.log10(Env.dec2bin(i) - Env.dec2bin(j))% 1 == 0) :
#                    self.S[self.state_size-i - 1][self.state_size -j - 1] = 1
#        print(self.S)
    def choose_action(self, state):
        actions = []
        #self.state_define()
        #print(self.State[state])
        for j in range(0, self.NumVNF):
            vector = np.arange(j, self.action_size , self.NumVNF)
            if sum(self.State[state][vector])==0 :    
                actions = np.append(actions,vector)
            #actions = np.where(self.State[state][vector]==0)
        return actions
    def next_state(self, state, action):
        possible_actions = self.choose_action(state)
        #print('possible_actions')
        #print(possible_actions)
        state_new = 0
        if action not in possible_actions :
            state_new = state
        else:
            temp =  np.copy(self.State[state][:])
            #print(temp)
            temp[int(action)] = 1
            #print(temp)
            for i in range(0, len(self.State)):  
                if all(temp == self.State[i]):
                    state_new = i
        return state_new
    def value_state(self):       
        DC_value = np.repeat(self.DC,self.NumVNF);
        VNF_value = np.tile(self.VNF, (1,self.NumDC))[0]
        #print(DC_value)
        #print(VNF_value)
        self.ValueState = np.zeros(len(self.State))
        valuStateDC = np.zeros((len(self.State),self.NumDC))
        for i in range(0, len(self.State)):
            k =  0
            for j in range(0, self.NumDC):
                valuStateDC[i][j] = self.DC[j] - np.dot(self.State[i][k:k+self.NumVNF], self.VNF)
                k = k + self.NumVNF
                if valuStateDC[i][j] < 0:
                    self.ValueState[i] += -20 * pow(valuStateDC[i][j],2) -150
                else:
                    self.ValueState[i] += -2 * pow(valuStateDC[i][j],2) +100
            #print(valuStateDC[i])
        #print(self.ValueState)
    def get_reward(self, state, next_state):
        self.value_state()
        return self.ValueState[next_state] - self.ValueState[state]
    def done_action(self, state):
        done  = 1
        if len(self.choose_action(state)) == 0:
            done = 1
            print('done')
            return done
        else :
            actions = (self.choose_action(state)).astype(int)
#            print('act')
#            print(actions)
            for i in range(0, len(actions)):
                nxt = self.next_state(state, actions[i])
                reward = self.get_reward(state, nxt)
                if reward > 0 :
                        done = 0
                        print('not done')
        return done
                        
                        
        
a = Env(np.array([4,5,3,1]), np.array([12, 13]))    
a.state_define()                          
print('choose_action') 
print(a.choose_action(10))  
print('nextState')      
print(a.next_state(10, 4))
print('value')
a.value_state()
print('reward')
print(a.get_reward(10,22))
print(a.done_action(10))
###

#a = Env(np.array([4,5,3, 1]), np.array([10]))                              
#print('choose_action') 
#print(a.choose_action(4)[0])  
#print('nextState')      
#print(a.next_state(4, 2))
#print(a.get_reward(9,13))