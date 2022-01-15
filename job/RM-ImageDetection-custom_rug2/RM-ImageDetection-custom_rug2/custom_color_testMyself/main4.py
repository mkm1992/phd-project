# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 11:40:06 2019

@author: mkm1992
"""

import numpy as np
import cv2 
import PIL
from PIL import Image
from classFunc.colorfinder import ColorCluster
import matplotlib.pyplot as plt
from functions.EnhanceImage import enhancing, meanColoring
from sklearn.cluster import KMeans
from functions.crop_func import crop
from scipy import ndimage
from functions.func import dist, crop,  dist1, dist2
import colorgram
###############################
name_nat = 'm27.jpg'
name =  'input/'+name_nat
img = ColorCluster.readImage(name)
plt.imshow(img)
plt.show()
##########################
im = ColorCluster.pilread(name)
flag_hsv = 0
flag_hsv, x = ColorCluster.checkRH(im, flag_hsv)
thresh =  33
if flag_hsv == 0:
   model2, img1 = ColorCluster.RGB(x, img, thresh)
else:
   model2, img1 = ColorCluster.HSV(x, img, thresh)
imgH =cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
imgN2 = ColorCluster.changeColor(model2, imgH)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/2'+name_nat
cv2.imwrite(name_out,imgN2)
###########################
new_im, img1 =  ColorCluster.modeling23color(model2, img1)
color_centre1 = ColorCluster.colorfindergram(new_im, thresh)
color12 = ColorCluster.colorfinderhist(new_im, thresh)
color_centre1 = ColorCluster.mergeColor(color_centre1,color12 )
model3 = ColorCluster.model23maker(thresh, model2, color_centre1, img1)

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model3[i,j] == 3:
            imgH[i,j,0] =150
            imgH[i,j,1] =50
           # img[i,j,2] =170
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model3[i,j] == 2:
            imgH[i,j,0] =10
            imgH[i,j,1] =200
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()

imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/3'+name_nat
cv2.imwrite(name_out,imgN2)
