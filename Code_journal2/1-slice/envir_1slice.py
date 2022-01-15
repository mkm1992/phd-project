"""
created on Saturday Nov 6 11:06:00 2021

@author: Mojdeh Karbalaee Motalleb
"""
import numpy as np

class enviroment:
    def __init__(self, N_PRB, N_VNF, Rmin, Dmax, pDrop, packetRate) -> None:
        self.Slice_Num = 1
        self.N_VNF = N_VNF
        self.N_PRB = N_PRB
        self.PRB_Slice  = 0
        self.VNF = 0
        self.Rmin = Rmin
        self.delay = Dmax
        self.packetDrop = pDrop
        self.packetRate = packetRate
        
    def state(self):
        return  [self.Rmin, self.delay, self.packetDrop, self.packetRate]

    def action_set(self):
        self.VNF_set = np.arange(self.N_VNF) 
        self.PRB_set = np.arange(self.N_PRB)
        return self.VNF_set, self.PRB_set

    def step(self, action):
        self.VNF = action[0]
        self.PRB_Slice = action[1]

    def reset(self):
        self.VNF = 0
        self.PRB_Slice = 0
        self.Rmin = 0
        self.delay = 0
        self.packetDrop = 0
        self.packetRate = 0

    def reward(self):
        return self.VNF/self.N_VNF 

