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
    def state(VNF1, VNF2, DC_rem):
        
        

