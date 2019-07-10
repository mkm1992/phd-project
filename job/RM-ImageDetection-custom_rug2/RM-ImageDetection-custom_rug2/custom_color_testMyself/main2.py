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
from functions.EnhanceImage import enhancing
from sklearn.cluster import KMeans
from functions.crop_func import crop
from scipy import ndimage
from functions.func import dist, crop, enhancing, dist1, dist2
import colorgram
############################################### Reading Image
name_nat = 'm20.jpg'
name =  'input/'+name_nat
imag = cv2.imread(name)
imag1 = crop(imag)
imag2 =  imag1[10:-10,10:-10,:]
#imag2 = imag
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
for i in range(1, len(cl1)):
    x = cl1[i]
    if x[1][0]<240 and x[1][1]<240 and x[1][2]<240:
        print(i)
        i = len(cl1)
        break

thresh = 33
flag = 0
if (x[1][0]<50 and x[1][1]<50 and x[1][2]<50) or flag==0:
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
    img1 = np.copy(img)
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
            imgH[i,j,0] =100
            imgH[i,j,1] =80
            if imgH[i,j,2]<80:
                imgH[i,j,2] =170
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/2'+name_nat
cv2.imwrite(name_out,imgN2)
#img1 = np.copy(img)
############################################Second color method 2
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
#################################################secondColor Method one
cl2 = new_im.getcolors(im.size[0]*im.size[1])
cl12 =sorted(cl2, reverse=True)

for i in range(1, len(cl12)):
    x1 = cl12[i]
    if x1[1][1]<240 and x1[1][0]<240 and dist1(x1[1][:],color_zero)>thresh:
        print(i)
        i = len(cl12)
        break

color12 = np.zeros([3])

color12[0] =x1[1][0]

color12[1] =x1[1][1]

color12[2] =x1[1][2]

if dist1(color_centre1[0,:],color12)< dist1(color_centre1[1,:],color12):
    if dist1(color_centre1[0,:],color12)<100:
        color_centre1[0,:] =  (color_centre1[0,:] + color12[:])/2
else :
    if dist1(color_centre1[1,:],color12)<100:
        color_centre1[1,:] =  (color_centre1[1,:] + color12[:])/2
        

#color_centre1 =  color12

####################################################

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model2[i,j]==0:
            temp =thresh +10
            index = 0
            for ch in range(0,2):
                if dist1( color_centre1[ch,:],img1[i,j,:])< temp:
                    temp = dist1( color_centre1[ch,:],img1[i,j,:])
                    index = ch+2
            model2[i,j] = index  
model3 =enhancing(model2, 4)
#model2 =enhancing(img21, color_group)

#for i in range(0,img.shape[0]):
#        for j in range(0,img.shape[1]):
#            if dist1(color12, imgH[i,j,:])<thresh+30:
#                model3[i,j]=2

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model3[i,j] == 3:
            imgH[i,j,0] =255
            imgH[i,j,1] =255
            imgH[i,j,2] =255
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model3[i,j] == 2:
            imgH[i,j,0] =10
            imgH[i,j,1] =200
            #imgH[i,j,2] = 50
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()

imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/1'+name_nat
cv2.imwrite(name_out,imgN2)

