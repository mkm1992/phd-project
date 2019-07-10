# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:39:53 2019

@author: mkm1992
"""

import numpy as np
import cv2 
import PIL
from PIL import Image
import extcolors
import matplotlib.pyplot as plt
from functions.EnhanceImage import enhancing
from sklearn.cluster import KMeans
from functions.crop_func import crop
from scipy import ndimage
from functions.func import dist, crop, enhancing, dist1, dist2
import colorgram
################################################
####
name_nat = 'm16.jpg'
name =  'input/'+name_nat
imag = cv2.imread(name)
imag1 = crop(imag)
img =  cv2.cvtColor(imag1, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
colors, pixel_count = extcolors.extract(name)
color_group, n = np.shape(colors)
color_centre = np.zeros([color_group,3])
for i in range(0,color_group):
    color_centre[i,0] = colors[i][0][0]
    color_centre[i,1] = colors[i][0][1]
    color_centre[i,2] = colors[i][0][2]
######################################
colorsG = colorgram.extract(name, color_group)
color_centre1 = np.zeros([color_group,3])
for i in range(0,color_group):
    a = colorsG[i]
    color_centre1[i,0] = a.rgb.r
    color_centre1[i,1] = a.rgb.g
    color_centre1[i,2] = a.rgb.b
img21 = np.zeros([img.shape[0] , img.shape[1]])
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        temp =1000
        index = 0
        for ch in range(0,color_group):
            if dist( color_centre1[ch,:],img[i,j,:])< temp  :
                temp = dist( color_centre[ch,:],img[i,j,:])
                index = ch
        if dist( color_centre1[index,:],img[i,j,:])< 35:
            img21[i,j] = index+1
#model2 =enhancing(img21, color_group)
model2  = img21
#imgH2 =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
imgH2 = np.copy(img)
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model2[i,j] == 1:
            imgH2[i,j,0] =255
            imgH2[i,j,1] =255
            imgH2[i,j,2] =255

plt.imshow(imgH2)
plt.show()
imgN2=cv2.cvtColor(imgH2, cv2.COLOR_BGR2RGB)
name_out = 'output/'+name_nat
cv2.imwrite(name_out,imgN2)