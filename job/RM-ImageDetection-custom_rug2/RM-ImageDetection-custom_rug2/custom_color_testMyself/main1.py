# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:41:57 2019

@author: mojdeh
"""

import numpy as np
import cv2
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from functions.EnhanceImage import enhancing
from sklearn.cluster import KMeans
from functions.crop_func import crop
from scipy import ndimage
from functions.func import dist, crop, enhancing, dist1, dist2
import colorgram
############################################### Reading Image
name_nat = 'm13.jpg'
name =  'input/'+name_nat
imag = cv2.imread(name)
imag1 = crop(imag)
imag2 =  imag1[10:-10,10:-10,:]
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
thresh = 30

if x[1][0]<50 and x[1][1]<50 and x[1][2]<50 :
    color1 = np.zeros([2,2,3])
    color1[:,:,0] =x[1][0]
    color1[:,:,1] =x[1][1]
    color1[:,:,2] =x[1][2]
    plt.imshow(color1.astype(int))
    plt.show()
    print('rgb')
    color12 = np.zeros([3])
    color12[0] =x[1][0]
    color12[1] =x[1][1]
    color12[2] =x[1][2]
    imgH =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img21 = np.zeros([img.shape[0] , img.shape[1]])
    img1 = np.copy(imgH)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if dist1(color12, img[i,j,:])<thresh:
                img21[i,j]=1 
    
else :
    imgH =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    im = Image.fromarray(imgH)
    cv2.imwrite('hsv/imgh.png',imgH)
    name1 = 'hsv/imgh.png'
    imgH1 =cv2.cvtColor(imgH, cv2.COLOR_BGR2RGB)
    img1 = np.copy(imgH)
    #im = Image.open(name1)
    x =max(im.getcolors(im.size[0]*im.size[1]))
    cl = im.getcolors(im.size[0]*im.size[1])
    cl1 =sorted(cl, reverse=True)
    #x = cl1[3]
    color1 = np.zeros([2,2,3])   
    color1[:,:,0] =x[1][0]
    color1[:,:,1] =x[1][1]    
    color1[:,:,2] =x[1][2]
    plt.imshow(color1.astype(int))
    plt.show()
    print('hsv')
    color12 = np.zeros([3])
    color12[0] =x[1][0]
    color12[1] =x[1][1]
    color12[2] =x[1][2]
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
            imgH[i,j,1] =80
            if imgH[i,j,2]<50:
                imgH[i,j,2] =170
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/'+name_nat
cv2.imwrite(name_out,imgN2)
img1 = np.copy(img)
############################################Sec
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model2[i,j]==1:
             img1[i,j,:] = [0,0,0]
new_im = Image.fromarray(img1)
color_group = 4
colorsG =  colorgram.extract(new_im, color_group)
color_centre1 = np.zeros([2,3])
color_zero = np.zeros([3])
for i in range(0,color_group):
    a = colorsG[i]
    color_centre1[0,0] = a.rgb.r
    color_centre1[0,1] = a.rgb.g
    color_centre1[0,2] = a.rgb.b
    if dist1(color_centre1[0,:], color_zero)>thresh:
        print(i)
        i = color_group
        break
a = colorsG[2]
color_centre1[1,0] = a.rgb.r
color_centre1[1,1] = a.rgb.g
color_centre1[1,2] = a.rgb.b                 

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model2[i,j]==0:
            temp =thresh + 30
            index = 0
            for ch in range(0,2):
                if dist1( color_centre1[ch,:],img1[i,j,:])< temp:
                    temp = dist1( color_centre1[ch,:],img1[i,j,:])
                    index = ch+2
            model2[i,j] = index  
model3 =enhancing(model2, 4)
#model2 =enhancing(img21, color_group)

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model3[i,j] == 3:
            imgH[i,j,0] =10
            imgH[i,j,1] =200
            #img[i,j,2] =170
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model3[i,j] == 2:
            imgH[i,j,0] =70
            imgH[i,j,1] =100
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()

imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/'+name_nat
cv2.imwrite(name_out,imgN2)