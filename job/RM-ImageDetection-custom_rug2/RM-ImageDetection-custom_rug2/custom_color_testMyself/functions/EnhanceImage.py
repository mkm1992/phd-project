# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:02:35 2018

@author: mkm19
"""

import numpy as np
from functions.func import dist, crop,  dist1, dist2

#########################

def maxRepeating(img, num): 
    count = np.zeros([num])
    for i in range(0, 25):
        for j in range(0, num):
            if img[i]==j:
                count[j]= count[j]+1
    
  
    result = max(count)
    ind  = np.argmax(count)
    return result, ind

def enhancing(img, clus_num):
    vec = np.zeros([5,5])
    l1, w1 = np.shape(img)
    for i in range(3,l1-2):
        for j in range(3, w1-2):
            vec[:,:] = img[i-2:i+3,j-2:j+3]
            vec1 = vec.reshape((25)) 
            result, ind = maxRepeating(vec1,   clus_num) 
            if result > 5:
                img[i,j] = ind

    return img
            
            
def meanColoring(im, thresh):
    cl = im.getcolors(im.size[0]*im.size[1])
    cl1 =sorted(cl, reverse=True)
    x =max(im.getcolors(im.size[0]*im.size[1]))
    i = 0
    if x[1]==(255,255,255):
        x = cl1[1]
        i = 1
    count  = 1
    color = np.dot(x[1],x[0])
    sigma = x[0]
    for j in range(i+1,len(cl1)):
        x1 = cl1[j]
        if dist1(x1[1][:],x[1][:])<thresh+5:
            count += 1
            color += np.dot(x1[1],x1[0]) 
            sigma += x1[0]
    color1 = np.dot(color,1/sigma) 
    return color1
