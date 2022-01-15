"""
created on Saturday Nov 6 11:06:00 2021

@author: Mojdeh Karbalaee Motalleb
"""
import numpy as np

class enviroment:
    def __init__(self, Slice_URLLC, Slice_eMBB, N_PRB, N_VNF) -> None:
        self.Slice_Num = Slice_URLLC + Slice_eMBB  # number of slices (a1,a2)
        self.Slice_URLLC = Slice_URLLC  # number of URLLC slices
        self.Slice_eMBB = Slice_eMBB  # number of eMBB slices
        self.VNF_List = [] # list of VNFs
        self.N_VNF = N_VNF
        self.N_PRB = N_PRB
        self.PRB_Slice  = np.zeros((self.N_PRB, self.N_Slice)) # list of PRBs
        self.VNF = np.zeros((1, self.N_Slice)) # list of VNFs
        self.Rmin = np.zeros((1, self.N_Slice)) # list of Rmin
        self.delay = np.zeros((1, self.N_Slice)) # list of delay
        self.packetDrop = np.zeros((1, self.N_Slice)) # list of packet drop
        
    def state(self):
        return  [self.Rmin, self.delay, self.packetDrop]   

    def action(self, action):
        return action    

