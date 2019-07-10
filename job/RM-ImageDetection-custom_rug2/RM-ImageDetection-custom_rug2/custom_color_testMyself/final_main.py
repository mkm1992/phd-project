# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:22:49 2019

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
from functions.colorFunction import FindColor
############################################### Reading Image
name_nat = 'm3.jpg'
name =  'input/'+name_nat
imag = cv2.imread(name)
imag1 = crop(imag)
imag2 =  imag1[5:-5,5:-5,:]
img =  cv2.cvtColor(imag2, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
flag_clustering = 1
model = np.zeros([img.shape[0], img.shape[1]])
########################################
imgH =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
thresh = 30
img_copy = np.copy(img)
######################################## loop for clustering
hsv = 0
num = 0
while num <3 :#flag_clustering:
   num += 1
   colorCent = FindColor.findDominantColor(img, thresh , hsv)
   color_centre1 = FindColor.ColorG(img, hsv )
   #colorCent1 = FindColor.meaningColor(colorCent, color_centre1)
   model = FindColor.makeModel(model, colorCent, img, thresh, num)
   imgNew = FindColor.newImg(img, model, num, hsv)
   flag_clustering = FindColor.finishingColor(model, flag_clustering)
   img = np.copy(imgNew)
print(num)
   
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model[i,j] == 1:
            imgH[i,j,0] =250
            imgH[i,j,1] =200
            if imgH[i,j,2]<10:
                    imgH[i,j,2] =170  
   
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()

imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/1'+name_nat
cv2.imwrite(name_out,imgN2)  
    