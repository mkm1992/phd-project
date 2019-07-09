# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:50:19 2019

@author: Mojdeh karbalaee
"""

import numpy as np
import math
from func import db2pow
from var import *
##############
dist = np.random.rand(N_rrh,N_UE)*Radius;
d1 = np.zeros([N_rrh, N_UE, N_antenna])
for i in range(0, N_antenna):
    d1[:,:,i] = dist[:,:]
loss = np.zeros([N_rrh, N_UE, N_antenna])
var_fading = db2pow(10);
ke = np.random.lognormal(0, var_fading, [N_rrh, N_UE, N_antenna]);
loss[:,:,:]= np.multiply(ke[:,:,:],np.power((np.power(d1[:,:,:],3.8)),-1));
ch1 = np.random.randn(N_rrh, N_UE, N_antenna)
ch2 = np.random.randn(N_rrh, N_UE, N_antenna)
channel_gain[:,:,:] = np.multiply(np.power(loss[:,:,:],0.5)/np.sqrt(2),(ch1[:,:,:]+1j*ch2[:,:,:]));
########
ro = 0.1
for i in range(0, N_antenna):
    a = np.matmul(np.transpose(channel_gain[:,:,i]),channel_gain[:,:,i])
    b = a + ro * np.eye(N_UE)
    b1 = np.linalg.inv(b) 
    precoding_mat[:,:,i] = np.matmul(channel_gain[:,:,i],b1)
