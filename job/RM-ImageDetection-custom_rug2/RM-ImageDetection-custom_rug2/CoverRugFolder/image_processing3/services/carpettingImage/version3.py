#################################################################################
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage.transform import rescale, resize, downscale_local_mean
import cython
import time
###############################################################################
#%load_ext cython

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray
###############################################################################
start = time.time()

img = cv2.imread('m12.png',0)
img11 = cv2.imread('m12.png')
img1   = cv2.imread('m1.png')
imgR = np.copy(img1)
imCarp1 = cv2.imread('s2.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img11 = cv2.cvtColor(img11, cv2.COLOR_BGR2RGB)
imgR  = cv2.cvtColor(imgR, cv2.COLOR_BGR2RGB)
imCarp1 = cv2.cvtColor(imCarp1, cv2.COLOR_BGR2RGB)
#############################################################3
r,c,a=np.shape(img1)
img11 = cv2.resize(img11,(c,r))
#############################################################
mat1 = np.copy(imCarp1)
r,c,a=np.shape(mat1)
mat1 = mat1[20:r-20,20:c-20,:]
r,c,a=np.shape(mat1)
imcarp3 = np.empty([10*r,15*c,3],dtype='uint8')
#############################################################
for i in range(0,r*10):
    for j in range(0,c*15):
            imcarp3[i,j,:]= mat1[np.mod(i,r),np.mod(j,c),:]

            
plt.imshow(imcarp3)
plt.imsave("rug.png",imcarp3)
#################################################################
rows,cols,ch = imcarp3.shape
pts1 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
pts2 = np.float32([[0,np.int(rows/7)],[np.int(4*cols/7),0],[np.int(cols/5),rows],[cols,np.int(rows/3)]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(imcarp3,M,(cols,rows))
plt.imshow(dst)
image = dst
im1=resize(image, (3000, 5000),
                       anti_aliasing=True)

#imcarp4 = dst[2000:3000,600:1600,:]
plt.imshow(im1)
#################################################################

im2 = np.uint8(im1*255)
im3=im2[450:2000,1000:2000,:]
#im3 = np.copy(im2)
plt.imshow(im3)
imax,jmax,ch = np.shape(img11)
mat1 =np.copy(im3) 
r,c,a=np.shape(mat1)
img3= np.copy(img11)
img2 = rgb2gray(img3)
b =0
for ii in range(0,imax):
    for jj in range(0,jmax):
        if img2[ii,jj]==0 : 
            img3[ii,jj,:]=mat1[ii,jj,:]
           # img3[ii+1,jj,:]=mat1[ii,jj,:]
        if img2[ii,jj]==0 and b==0:
            print(ii)
            b =1

##############
            
plt.imshow(img3)

duration = time.time() - start
print(duration)
plt.imsave("final6.png",img3)

