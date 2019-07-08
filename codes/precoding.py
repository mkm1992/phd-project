# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:50:36 2019

@author: Mojdeh Karbalaee
"""
import numpy as np
import math

ro = 0.1

for i in range(0, N_antenna):
    a = (np.transpose(channel_gain[:,:,i])*channel_gain[:,:,i])
    b = a + ro *
    precoding_mat[:,:,i] = channel_gain[:,:,i]*a






ro = 0;
v1 = H1*(H1'*H1+ro*eye(K*S1))^(-1);
v1(:,:) = v1(:,:)/norm(v1(:,:));
