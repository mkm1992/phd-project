"""
created on Saturday Nov 27 15:31:00 2021

@author: Mojdeh Karbalaee Motalleb
"""
import numpy as np

class enviroment:
    def __init__(self, M_VNF, Rmin, Dmax, packetArrive ) -> None:
        self.M_VNF = M_VNF
        self.VNF = 0
        self.Rmin = Rmin
        self.Dmax = Dmax
        self.packetArrive = packetArrive
        
    def state(self):
        return  [self.Rmin, self.Dmax, self.packetArrive, self.M_VNF]

    def action_set(self):
        self.VNF_set = np.arange(self.M_VNF) 
        self.Rate_set = np.arange(self.N_PRB)
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

