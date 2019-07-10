# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:23:07 2019

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
name_nat = 'm3.jpg'
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
thresh = 35
flag = 0
###############################
if (x[1][0]<50 and x[1][1]<50 and x[1][2]<50) and flag==1 :
    flag = 1
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
    imgH =  np.copy(img)
    img21 = np.zeros([img.shape[0] , img.shape[1]])
    colorsG =  colorgram.extract(name, 1)
    color_centre1 = np.zeros([3])
    color_zero = np.zeros([3])
    a = colorsG[0]
    color_centre1[0] = a.rgb.r
    color_centre1[1] = a.rgb.g
    color_centre1[2] = a.rgb.b
    ###########################
    if dist1(color_centre1[:],color12)<50:
        color12[:] =  (color_centre1[:] + color12[:])/2
        print('yes')
#    else:
#        color12 = color_centre1
    img1 = np.copy(imgH)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if dist1(color12, img[i,j,:])<thresh:
                img21[i,j]=1 
    
else :
    imgH =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    im = Image.fromarray(imgH)
    colorsG =  colorgram.extract(im, 1)
    color_centre1 = np.zeros([3])
    color_zero = np.zeros([3])
    a = colorsG[0]
    color_centre1[0] = a.rgb.r
    color_centre1[1] = a.rgb.g
    color_centre1[2] = a.rgb.b
    ###########################
#    else:
#    cv2.imwrite('hsv/imgh.png',imgH)
#    name1 = 'hsv/imgh.png'
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
#    if dist1(color_centre1[:],color12)<thresh:
#        color12[:] =  (color_centre1[:] + color12[:])/2
#        print('yes')
    img21 = np.zeros([img.shape[0] , img.shape[1]])
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if dist1(color12, imgH[i,j,:])<thresh:
                img21[i,j]=1    
model2 =enhancing(img21, 2)
if flag ==1:
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if model2[i,j]==1:
                img[i,j,0] =170
                img[i,j,1] =80
                img[i,j,0] =100
    imgN2 = np.copy(img)
    imgH =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
else:
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if model2[i,j]==1:
                imgH[i,j,0] =100
                imgH[i,j,1] =100
                if imgH[i,j,2]<50:
                    imgH[i,j,2] =170
    imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/'+name_nat
cv2.imwrite(name_out,imgN2)
#img1 = np.copy(img)  
#####################################
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

#if dist1(color_centre1[0,:],color12)< dist1(color_centre1[1,:],color12):
#    if dist1(color_centre1[0,:],color12)<100:
#        color_centre1[0,:] =  (color_centre1[0,:] + color12[:])/2
#else :
#    if dist1(color_centre1[1,:],color12)<100:
#        color_centre1[1,:] =  (color_centre1[1,:] + color12[:])/2
        
####################################################
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
            imgH[i,j,0] =250
            imgH[i,j,1] =200
            if imgH[i,j,2]<10:
                    imgH[i,j,2] =170
            #img[i,j,2] =170
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model3[i,j] == 2:
            imgH[i,j,0] =20
            imgH[i,j,1] =250
            if imgH[i,j,2]<10:
                    imgH[i,j,2] =170
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/'+name_nat
cv2.imwrite(name_out,imgN2)    
