# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:48:38 2019

@author: mkm1992
"""


import numpy as np
import cv2 
import PIL
from PIL import Image

import matplotlib.pyplot as plt
from functions.EnhanceImage import  meanColoring ,enhancing
from sklearn.cluster import KMeans
from functions.crop_func import crop
from scipy import ndimage
from functions.func import dist, crop,  dist1, dist2 #, enhancing
import colorgram
############################################### Reading Image
name_nat = 'm21.jpg'
name =  'input/'+name_nat
imag = cv2.imread(name)
imag1 = crop(imag)
imag2 =  imag1[5:-5,5:-5,:]
img =  cv2.cvtColor(imag2, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
#########################################Cluster First Color
im = Image.open(name)
x =max(im.getcolors(im.size[0]*im.size[1]))

cl = im.getcolors(im.size[0]*im.size[1])
cl1 =sorted(cl, reverse=True)
if x[1]==(255,255,255):
    x = cl1[1]
thresh = 32
flag = 0
if (x[1][0]<50 and x[1][1]<50 and x[1][2]<50) or flag==1 :
    print('rgb')
    color12 = meanColoring(im, thresh)
    imgH =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img21 = np.zeros([img.shape[0] , img.shape[1]])
    img1 = np.copy(img)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if dist1(color12, img[i,j,:])<thresh:
                img21[i,j]=1 
    
else :
    imgH =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    im = Image.fromarray(imgH)
    img1 = np.copy(imgH)
    color12 = meanColoring(im, thresh)
    img21 = np.zeros([img.shape[0] , img.shape[1]])
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if dist1(color12, imgH[i,j,:])<thresh:
                img21[i,j]=1    
model2 =enhancing(img21, 2)
###########################################Change First Color
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model2[i,j]==1:
            imgH[i,j,0] =10
            imgH[i,j,1] =200
            if imgH[i,j,2]<50:
                imgH[i,j,2] =170
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/1'+name_nat
cv2.imwrite(name_out,imgN2)