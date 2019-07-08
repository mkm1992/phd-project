# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:50:19 2019

@author: Mojdeh karbalaee
"""

import numpy as np
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