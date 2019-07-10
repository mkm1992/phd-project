import numpy as np
import cv2
from functions.func import dist, crop,  dist1, dist2
from PIL import Image
from functions.EnhanceImage import enhancing
import colorgram

class ColorCluster:
    def readImage(name):
        imag = cv2.imread(name)
        imag1 = crop(imag)
        imag2 =  imag1[5:-5,5:-5,:]
        img =  cv2.cvtColor(imag2, cv2.COLOR_BGR2RGB) 
        return img
    def pilread(name):
        im = Image.open(name)
        return im
    def checkRH(im, flag_hsv):
        x =max(im.getcolors(im.size[0]*im.size[1]))
        cl = im.getcolors(im.size[0]*im.size[1])
        cl1 =sorted(cl, reverse=True)
        if x[1]==(255,255,255):
            x = cl1[1]
        if (x[1][0]<50 and x[1][1]<50 and x[1][2]<50) or flag_hsv==0 :
            flag_hsv =0
        return flag_hsv, x
    def RGB(x, img, thresh):
        color12 = np.zeros([3])
        color12[0] =x[1][0]
        color12[1] =x[1][1]
        color12[2] =x[1][2]
        img21 = np.zeros([img.shape[0] , img.shape[1]])
        #imgH =cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        img1 = np.copy(img)
        print('rgb')
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if dist1(color12, img[i,j,:])<thresh:
                    img21[i,j]=1 
        model2 =enhancing(img21, 2)
        return model2, img1
    def HSV(x, img, thresh):
        imgH =cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        im = Image.fromarray(imgH)
        img1 = np.copy(imgH)
        x =max(im.getcolors(im.size[0]*im.size[1]))
        cl = im.getcolors(im.size[0]*im.size[1])
        cl1 =sorted(cl, reverse=True)
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
        return model2, img1
    def changeColor(model2, imgH):
        for i in range(0,imgH.shape[0]):
            for j in range(0,imgH.shape[1]):
                if model2[i,j]==1:
                    imgH[i,j,0] =100
                    imgH[i,j,1] =80
                    if imgH[i,j,2]<50:
                        imgH[i,j,2] =170
        imgN2 =  cv2.cvtColor(imgH, cv2.COLOR_HSV2RGB)
        return imgN2
    def modeling23color(model2, img1):
        for i in range(0,img1.shape[0]):
            for j in range(0,img1.shape[1]):
                if model2[i,j]==1:
                     img1[i,j,:] = [0,0,0]
        new_im = Image.fromarray(img1)
        return new_im, img1
    def colorfindergram(new_im, thresh):
        color_group = 4
        colorsG =  colorgram.extract(new_im, color_group)
        color_zero = np.zeros([3])
        color_centre1 = np.zeros([2,3])
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
        return color_centre1
    def colorfinderhist(new_im, thresh):
        cl2 = new_im.getcolors(new_im.size[0]*new_im.size[1])
        cl12 =sorted(cl2, reverse=True) 
        color_zero = np.zeros([3])
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
        return color12
    def mergeColor(color_centre1,color12 ):
        if dist1(color_centre1[0,:],color12)< dist1(color_centre1[1,:],color12):
            if dist1(color_centre1[0,:],color12)<100:
                color_centre1[0,:] =  (color_centre1[0,:] + color12[:])/2
        else :
            if dist1(color_centre1[1,:],color12)<100:
                color_centre1[1,:] =  (color_centre1[1,:] + color12[:])/2
        return color_centre1
    def model23maker(thresh, model2, color_centre1, img1):
        for i in range(0,model2.shape[0]):
            for j in range(0,model2.shape[1]):
                if model2[i,j]==0:
                    temp =thresh +10
                    index = 0
                    for ch in range(0,2):
                        if dist1( color_centre1[ch,:],img1[i,j,:])< temp:
                            temp = dist1( color_centre1[ch,:],img1[i,j,:])
                            index = ch+2
                    model2[i,j] = index  
        model3 =enhancing(model2, 4)
        return model3
    