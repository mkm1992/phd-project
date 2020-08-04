"""
Created on Tue Aug  4 10:42:20 2020

@author: Mojdeh Karbalaee
"""
import numpy as np

class Env:
    def __init__(self, VNF, DC):
        self.VNF = VNF
        self.DC = DC
        self.NumVNF = len(VNF)
        self.NumDC = len(DC)
        self.state_size =  pow(2, self.NumVNF)
        self.action_size  =  self.NumVNF 
        self.Q = np.zeros((self.state_size, self.action_size))
        self.R = np.zeros((self.state_size, self.action_size))
        self.S = np.zeros((self.state_size, self.state_size))
        self.State = np.zeros((self.state_size, self.action_size))
    def dec2bin(num):
        return int(bin(num)[2:])
    def available_state(self):
        for i in range(0, self.state_size):
            for j in range(0, self.state_size):
                if (i- j > 0) and ((Env.dec2bin(i) - Env.dec2bin(j)) == 1 or  np.log10(Env.dec2bin(i) - Env.dec2bin(j))% 1 == 0) :
                    self.S[i][j] = 1
                    #print(Env.dec2bin(i),Env.dec2bin(j))
        print(self.S)
    def choose_action(self, state):
        actions = np.where(self.S[state]==1)
        return actions
    def nextState(action, state):
        possible_actions = Env.choose_action(state)[0]
        if action not in possible_actions :
            state_new = state
        else:
            state_new = action
    #def value_state(self, state):
a = Env(np.array([4,5,3]), np.array([8]))        
a.available_state()                
a.choose_action(1)        
        