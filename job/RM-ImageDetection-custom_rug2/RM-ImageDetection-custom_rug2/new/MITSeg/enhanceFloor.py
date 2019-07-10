# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:51:01 2019

@author: mkm1992
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean
################################
img = cv2.imread('output/n8.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
############################
img1 = cv2.imread('input/n8.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img4 = np.copy(img1)
plt.imshow(img1)
plt.show()
############################
imCarp = cv2.imread('carpet/m27.jpg')
imCarp = cv2.cvtColor(imCarp, cv2.COLOR_BGR2RGB)
plt.imshow(imCarp)
##########################
imax,jmax,ch = np.shape(img)
index = np.zeros([2,4]) + imax + jmax
for i in range(0,imax):
    for j in range(0,jmax):
        if (img[i,j,0]== 80 and  img[i,j,1]== 50 and img[i,j,2]== 50)  or (img[i,j,0]==255 and img[i,j,1]==9 and img[i,j,2]==92):
            img1[i,j,:]= 255

            
plt.imshow(img1)
plt.show()
#img2=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#cv2.imwrite('out/image.png',img2)
########################
for i in range(0,imax):
    for j in range(0,jmax):
        if img[i,j,0]==255 and img[i,j,1]==9 and img[i,j,2]==92 :
            index[0,0] =i
            index[1,0] = j
            i = imax-1
            j = jmax-1
            break
for j in range(0,jmax):
    for i in range(0,imax):
        if img[i,j,0]==255 and img[i,j,1]==9 and img[i,j,2]==92 :
            index[0,1] =i
            index[1,1] = j
            i = imax-1
            j = jmax-1
            break
for i in range(imax-1,0,-1):
    for j in range(jmax-1,0,-1):
        if img[i,j,0]==255 and img[i,j,1]==9 and img[i,j,2]==92 :
            index[0,2] =i
            index[1,2] = j
            i = 1
            j = 1
            break
for j in range(jmax-1,0,-1):
    for i in range(imax-1,0,-1):
        if img[i,j,0]==255 and img[i,j,1]==9 and img[i,j,2]==92 :
            index[0,3] =i
            index[1,3] = j
            i = 1
            j = 1
            break
####################################
imCarp = cv2.resize(imCarp,(jmax, imax))

#im1=resize(imCarp, (imax, jmax),anti_aliasing=True)
#
#plt.imshow(im1)
##########################################
#imCarp = np.uint8(im1*255)


rows,cols,ch = imCarp.shape
index1 = np.copy(index)
#index[0,:] = index[0,:] +100
#index[1,:] = index[1,:] -100
#index[0,:] = index[0,:] - min(index[0,:])
#index[1,:] = index[1,:] - min(index[1,:])
pts1 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
ctx = 0
#pts2 = np.float32([[index[1,3],index[0,3]],[index[1,2],index[0,2]],[index[1,0],index[0,0]],[index[1,1],index[0,1]]])
pts2 = np.float32([[index[1,3]-ctx,index[0,3]+ctx],[index[1,2]-ctx,index[0,2]-ctx],[index[1,0]+ctx,index[0,0]+ctx],[index[1,1]+ctx,index[0,1]-ctx]])
#####################################
pts2[3,0] = 1250
pts2[3,1] = 815
M = cv2.getPerspectiveTransform(pts1,pts2)
h, status = cv2.findHomography(pts1,pts2)
dst = cv2.warpPerspective(imCarp,h,(int(cols),int(rows)))
plt.imshow(dst)
plt.show()
###################################

#pts2 = np.float32([[index[1,3],index[0,3]],[index[1,2],index[0,2]],[index[1,0],index[0,0]],[index[1,1],index[0,1]]])
##############Comment
#pts1 = np.float32([[index[1,3]-ctx,index[0,3]+ctx],[index[1,2]-ctx,index[0,2]-ctx],[index[1,0]+ctx,index[0,0]+ctx],[index[1,1]+ctx,index[0,1]-ctx]])
#ctx = 0
#pts2 = np.float32([[index[1,3]-ctx,index[0,3]+ctx],[index[1,2]-ctx,index[0,2]-ctx],[index[1,0]+ctx,index[0,0]+ctx],[index[1,1]+ctx,index[0,1]-ctx]])
######################################
#M = cv2.getPerspectiveTransform(pts1,pts2)
#dst1 = cv2.warpPerspective(dst,M,(cols,rows))
#plt.imshow(dst1)
#plt.show()
#################################


imax,jmax,ch = np.shape(img)
img3 = np.copy(img4)
for i in range(0,imax):
    for j in range(0,jmax):
        if  (img[i,j,0]==255 and img[i,j,1]==9 and img[i,j,2]==92)or (np.all( img1[i,j,:]==255) and (np.all(dst[i,j,:]>0))):
            img3[i,j,:]= dst[i,j,:]


plt.imshow(img3)
plt.show()











            
