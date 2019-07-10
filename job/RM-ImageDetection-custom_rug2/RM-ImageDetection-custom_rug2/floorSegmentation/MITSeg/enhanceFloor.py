# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:51:01 2019

@author: mkm1992
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
################################
img = cv2.imread('output/m3.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
############################
img1 = cv2.imread('input/m3.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.show()
############################
imax,jmax,ch = np.shape(img)
for i in range(0,imax):
    for j in range(0,jmax):
        if img[i,j,0]== 80 and  img[i,j,1]== 50 and img[i,j,2]== 50:
            img1[i,j,:]= 0
plt.imshow(img1)
plt.show()
img2=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
cv2.imwrite('out/image.png',img2)