# -*- coding: utf-8 -*-
import numpy as np
from services.customRug.image_service import ImageAlter
import colorgram
from PIL import Image
from services.customRug.dominant_service import DominantService
class Color2Service:
    def modeling23color(model2, img1):
        for i in range(0,img1.shape[0]):
            for j in range(0,img1.shape[1]):
                if model2[i,j]>0:
                     img1[i,j,:] = [0,0,0]
        new_im = Image.fromarray(DominantService.croping(img1))
        return new_im, img1
    def colorfindergram(new_im, thresh):
        color_group = 5
        colorsG =  colorgram.extract(new_im, color_group)
        color_zero = np.zeros([3])
        color_centre1 = np.zeros([2,3])
        for i in range(0,color_group):
            a = colorsG[i]
            color_centre1[0,0] = a.rgb.r
            color_centre1[0,1] = a.rgb.g
            color_centre1[0,2] = a.rgb.b
            if ImageAlter.dist1(color_centre1[0,:], color_zero)>thresh:
                print(i)
                i = color_group
                break
        print(colorsG)
        print("colorGS")
        if len(colorsG)>2:
            a = colorsG[2]
            color_centre1[1,0] = a.rgb.r
            color_centre1[1,1] = a.rgb.g
            color_centre1[1,2] = a.rgb.b 
        return color_centre1
    def color2get(new_im, thresh):
        color_zero = np.zeros([3])
        cl2 = new_im.getcolors(new_im.size[0]*new_im.size[1])
        cl12 =sorted(cl2, reverse=True)

        for i in range(1, len(cl12)):
            x1 = cl12[i]
            if x1[1][1]<240 and x1[1][0]<240 and ImageAlter.dist1_w(x1[1][:],color_zero)>thresh:
                print(i)
                i = len(cl12)
                break
        
        color12 = np.zeros([3])
        
        color12[0] =x1[1][0]
        
        color12[1] =x1[1][1]
        
        color12[2] =x1[1][2]
        print("colorpil")
        print(color12)
        print("colorpil")
        return color12
    def mergeColor(color_centre1, color12):
        if ImageAlter.dist1(color_centre1[0,:],color12)< ImageAlter.dist1(color_centre1[1,:],color12):
            if ImageAlter.dist1(color_centre1[0,:],color12)<100:
                color_centre1[0,:] =  (color_centre1[0,:] + color12[:])/2
        else :
            if ImageAlter.dist1(color_centre1[1,:],color12)<100:
                color_centre1[1,:] =  (color_centre1[1,:] + color12[:])/2
        return color_centre1
    def finalModel(thresh,color_centre1, img1, model2, flag, enhNum):
        for i in range(0,img1.shape[0]):
            for j in range(0,img1.shape[1]):
                if model2[i,j]==0:
                    temp =thresh
                    index = 0
                    for ch in range(0,2):
                        if flag ==1 and (color_centre1[ch,2]>230 or color_centre1[ch,2]< 50 ):
                            if np.abs( color_centre1[ch,2]-img1[i,j,2])< temp:
                                temp = ImageAlter.dist1_v( color_centre1[ch,:],img1[i,j,:])
                                index = ch+2
#                        elif flag ==1:
#                            if ImageAlter.dist1_w( color_centre1[ch,:],img1[i,j,:])< temp:
#                                temp = ImageAlter.dist1_w( color_centre1[ch,:],img1[i,j,:])
#                                index = ch+2
                        else :
                            if ImageAlter.dist1_w( color_centre1[ch,:],img1[i,j,:])< temp:
                                temp = ImageAlter.dist1_w( color_centre1[ch,:],img1[i,j,:])
                                index = ch+2
                            
                    model2[i,j] = index  
        model3 =ImageAlter.enhancing(model2, enhNum)
        return model3
    def findColorC(model3, img):
        colorC23 = np.zeros([2,3])
        count2 = 0
        count3 = 0
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if model3[i,j]==2:
                    count2 += 1
                    colorC23[0,:] = colorC23[0,:]+img[i,j,:]
                if model3[i,j]==3:
                    count3 += 1
                    colorC23[1,:] = colorC23[1,:]+img[i,j,:]
        colorC23[0,:] = np.round(colorC23[0,:]/count2)
        colorC23[1,:] = np.round(colorC23[1,:]/count3)
        return colorC23
    def reshaping(model):
        model_new = np.reshape(model,[model.shape[0]*model.shape[1]])
        return model_new
    def unreshaping(model, img):
        model_new = np.reshape(model,[img.shape[0],img.shape[1]])
        return model_new
    def reshaping_img(img):
        img_new = np.reshape(img,[img.shape[0]*img.shape[1]*3])
        return img_new
    def colorConcat(color_centre1, x):
        coloring1 = np.zeros([3,3])
        coloring1[1:3,:]= color_centre1
        coloring1[0,:] = x[1]
        return coloring1