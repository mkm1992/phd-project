# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 10:28:20 2018

@author: mkm19
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
def crop(img):
    l1, w1, ch = np.shape(img)
    k =0
    t =0
    k1 =0
    t1 =0
    for i in range(0,int(w1/2)):
        if img[int(l1/2),i,0]!=255 or  img[int(l1/2),i,1]!=255 or  img[int(l1/2),i,2]!=255:
            k = i
            #print(k)
            break
    for i in range(0,int(l1/2)):
        if img[i,int(w1/2),0]!=255 or  img[i,int(w1/2),1]!=255 or  img[i,int(w1/2),2]!=255:
            t = i
            #print(t)
            break
    
    for i in range(1,int(w1/2)):
        if img[int(l1/2),w1-i,0]!=255 or  img[int(l1/2),w1-i,1]!=255 or  img[int(l1/2),w1-i,2]!=255:
            k1 = w1-i-1
            #print(k1)
            break
    for i in range(1,int(l1/2)):
        if img[l1-i,int(w1/2),0]!=255 or  img[l1-i,int(w1/2),1]!=255 or  img[l1-i,int(w1/2),2]!=255:
            t1 = l1-i-1
            #print(t1)
            break
    img2 = img[t:t1,k:k1,:] 
    return img2

#name = 'm1.jpg'
#imag = cv2.imread(name)
#imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
#img = crop(imag)
#plt.imshow(img)
#plt.show()
#name = 'm1.jpg'
#imag = cv2.imread(name)
#img = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
#imag1 = crop(imag)
#img =  cv2.cvtColor(imag1, cv2.COLOR_RGB2HSV)
##img = imag1
##img = cv2.resize(img , (100,100))
#plt.imshow(img)
#plt.show()