"""
Created on Sun Sep 13 16:55:18 2020

@author: Mojdeh Karbalaee
"""
import numpy as np
from itertools import combinations
class Env:
    def __init__(self, VNF1, VNF2, DC_rem):
        self.VNF1 = VNF1
        self.VNF2 = VNF2
        self.DC_rem = DC_rem
        self.action_size = self.VNF1 + self.VNF2
        self.Val1 = 2;  #value for first service
        self.Val2 = 1;  #value for second service 
        self.MaxS1 = 5;
        self.MaxS2 = 10;
    def state_define(self):
        self.state = self.DC_rem, self.VNF1, self.VNF2
    def choose_action(self):
        if self.VNF1 > 0:
            ac1 = list(range(1,self.VNF1+1))*self.Val1
        else :
            ac1 = list(range(-1,self.VNF1-1,-1))*self.Val1  
        if self.VNF2 > 0:
            ac2 = list(range(1,self.VNF2+1))*self.Val2
        else :
            ac2 = list(range(-1,self.VNF2-1,-1))*self.Val2 
        actions = ac1, ac2
        return actions
    def next_state(self, action):
        DC_remN = self.DC_rem -  action[0] - action[1]
        return DC_remN
    def reward(self, DC_remN):
        if DC_remN < 0:
            reward_s =  -100
        else:
            reward_s = pow(self.MaxS1*self.Val1 + self.MaxS2*self.Val2-DC_remN,2)
        return reward_s
        
        

        
                       
        
        

