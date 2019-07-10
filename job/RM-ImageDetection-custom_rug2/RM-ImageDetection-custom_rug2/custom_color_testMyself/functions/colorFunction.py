# -*- coding: utf-8 -*-

import numpy as np
import cv2 
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from functions.EnhanceImage import enhancing
from functions.func import dist, crop, enhancing, dist1, dist2
import colorgram

class FindColor:
    def hsvImage(img):
       img1 =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
       return img1
    
    def make_pil(img):
        new_im = Image.fromarray(img)
        return new_im
    
    def findDominantColor(img, thresh = 32, hsv = 0):
        if hsv == 1:
            new_im= FindColor.make_pil(FindColor.hsvImage(img))
        else:
            new_im = FindColor.make_pil(img)    
        cl = new_im.getcolors(new_im.size[0]*new_im.size[1])
        cl1 =sorted(cl, reverse=True) 
        color_zero = np.zeros([3])
        for i in range(1, len(cl1)):
            x1 = cl1[i]
            if x1[1][1]<240 and x1[1][0]<240 and x1[1][2]<240 and dist1(x1[1][:],color_zero)>thresh:
                print(i)
                i = len(cl1)
                break    
        colorCent = np.zeros([3])    
        colorCent[0] =x1[1][0]
        colorCent[1] =x1[1][1]    
        colorCent[2] =x1[1][2]
        return colorCent
    
    def ColorG(img, hsv =0):
        if hsv == 1:
            new_im= FindColor.make_pil(FindColor.hsvImage(img))
        else:
            new_im = FindColor.make_pil(img)     
        colorsG =  colorgram.extract(new_im, 1)
        color_centre1 = np.zeros([3])
        a = colorsG[0]
        color_centre1[0] = a.rgb.r
        color_centre1[1] = a.rgb.g
        color_centre1[2] = a.rgb.b
        return color_centre1
    
    def meaningColor(ColorCent, color_centre1):
        if dist1(color_centre1[:],ColorCent[:])<50:
            ColorCent[:] =  (color_centre1[:] + ColorCent[:])/2 
            return ColorCent
    
    def makeModel(model, ColorCent, img, thresh, num):
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if dist1(ColorCent, img[i,j,:])<thresh:
                    model[i,j]= num
        model2 =enhancing(model, num)
        return model2
    def newImg(img, model, num, hsv = 0):
        if hsv == 1:
            imgNew= FindColor.hsvImage(img)
        else:
            imgNew = np.copy(img)    
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if model[i,j]>0:
                     imgNew[i,j,:] = [0,0,0]
        return imgNew
    def finishingColor(model, flag=1):
        count = 0
        for i in range(0, model.shape[0]):
            for j in range(0, model.shape[1]):
                if model[i,j]==0:
                    count += 1
        if (count*10000 )< (model.shape[0]*model.shape[1]):
            flag = 0
        return flag
        
        
        