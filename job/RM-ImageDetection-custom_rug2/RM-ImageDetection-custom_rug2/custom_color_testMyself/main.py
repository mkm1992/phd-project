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
############################################### Reading Image
name_nat = 'm25_1.jpg'
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
    
    #cv2.imwrite('hsv/imgh.png',imgH)
    #name1 = 'hsv/imgh.png'
    im = Image.fromarray(imgH)
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
            if imgH[i,j,2]<70:
                imgH[i,j,2] =170
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/'+name_nat
cv2.imwrite(name_out,imgN2)
############################################Second Color

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model2[i,j]==1:
             img1[i,j,:] = [0,0,0]

new_im = Image.fromarray(img1)
cl2 = new_im.getcolors(im.size[0]*im.size[1])
cl12 =sorted(cl2, reverse=True)

for i in range(1, len(cl12)):
    x1 = cl12[i]
    if x1[1][1]<250:
        print(i)
        i = len(cl12)
        break



color12 = np.zeros([3])

color12[0] =x1[1][0]

color12[1] =x1[1][1]

color12[2] =x1[1][2]
########################################################change second color
#img21 = np.zeros([img.shape[0] , img.shape[1]])
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if dist1(color12, img1[i,j,:])<thresh+5 and model2[i,j]==0:
            model2[i,j]=2    
model3 =enhancing(model2, 3)
###########################################Change First Color
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if model2[i,j]==2:
            imgH[i,j,0] =100
            imgH[i,j,1] =200
            if imgH[i,j,2]<50:
                imgH[i,j,2] =110
imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
plt.imshow(imgN2)
plt.show()
imgN2=cv2.cvtColor(imgN2, cv2.COLOR_BGR2RGB)
name_out = 'output/'+name_nat
cv2.imwrite(name_out,imgN2)


