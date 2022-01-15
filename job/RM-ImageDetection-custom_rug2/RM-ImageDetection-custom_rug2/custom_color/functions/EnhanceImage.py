# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:02:35 2018

@author: mkm19
"""

import numpy as np


#########################

def maxRepeating(img, num): 
    count = np.zeros([num])
    for i in range(0, 9):
        for j in range(0, num):
            if img[i]==j:
                count[j]= count[j]+1
    
  
    result = max(count)
    ind  = np.argmax(count)
    return result, ind

def enhancing(img, clus_num):
    vec = np.zeros([3,3])
    l1, w1 = np.shape(img)
    for i in range(1,l1-1):
        for j in range(1, w1-1):
            vec[:,:] = img[i-1:i+2,j-1:j+2]
            vec1 = vec.reshape((9)) 
            result, ind = maxRepeating(vec1,   clus_num) 
            if result > 3:
                img[i,j] = ind
    return img
            
            
            