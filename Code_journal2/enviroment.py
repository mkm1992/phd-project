"""
created on Saturday Nov 6 11:06:00 2021

@author: Mojdeh Karbalaee Motalleb
"""
import numpy as np

class enviroment:
    def __init__(self, Slice_Num, N_PRB) -> None:
        self.Slice_Num = Slice_Num  # number of slices (a1,a2)
        self.VNF_List = [] # list of VNFs
        self.N_PRB = N_PRB
        self.N_Slice = Slice_Num[0] + Slice_Num[1]
        self.PRB_Slice  = np.zeros(self.N_PRB, self.N_Slice) # list of PRBs

    def state(self):
        return self.VNF_List        

