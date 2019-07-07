# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:00:50 2019

@author: Mojdeh Karbalaee
"""
import numpy as np

##Define Variables
N_service = 5  #number of services
N_rrh = 10 #number of RRHs
N_slice = 7 # number of slices
N_bbu =  10 # number of bbu
N_prb =  15 # number of prb
N_UE = 100 # number of UE
N_antenna = 4 # number of antenna in each rrh
############
## Define variables with correct size
#np.random.randint(low=1, high=100, size=4)
RRH = np.zeros([N_rrh, N_slice])
UE = np.zeros([N_UE, N_service])
BBU = np.zeros([N_bbu,N_slice])
PRB = np.zeros([N_prb, N_slice])
Service2Slice = np.zeros([N_service, N_slice])
channel_gain = np.zeros([N_slice, N_rrh, N_prb, N_service, N_UE, N_antenna])
precoding = np.zeros([N_slice, N_rrh, N_prb, N_service, N_UE, N_antenna])
P_UE = np.zeros([N_service,N_UE])
Interf= np.zeros([N_slice, N_rrh, N_prb, N_service, N_UE])
Interf1 = np.zeros([N_slice, N_rrh, N_prb, N_service, N_UE])
Rate = np.zeros([N_slice, N_rrh, N_prb, N_service, N_UE])
UE2PRB = np.zeros([N_slice, N_prb, N_service, N_UE])
BBU2RRH = np.zeros([N_slice,N_bbu,N_rrh])
Capacity_fronthaul = np.zeros([N_slice, N_bbu, N_rrh])
print('variables are defined')
###########

