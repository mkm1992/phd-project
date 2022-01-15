# -*- coding: utf-8 -*-
import numpy as np
from services.customRug.image_service import ImageAlter
from PIL import Image
from services.customRug.dominant_service import DominantService
from services.customRug.color2_service import Color2Service
from numba import jit
from numba import jit, autojit

class Color3Service:
    def color3get(new_im, thresh, c, c1, flag, num_max):

        cl2 = new_im.getcolors(new_im.size[0]*new_im.size[1])
        cl12 =sorted(cl2, reverse=True)
        for i in range(num_max, len(cl12)):
            x1 = cl12[i]
            if x1[1][2]<250 and x1[1][2]> 10:
                if flag ==1 and (x1[1][2]>230 or x1[1][2]< 50 ):
                    distance = ImageAlter.dist_v(x1[1][:], c[1][:])
                    distance1 = ImageAlter.dist_v(x1[1][:], c1[1][:])
                else:
                    distance = ImageAlter.dist1(x1[1][:], c[1][:])
                    distance1 = ImageAlter.dist1(x1[1][:], c1[1][:])
                if  distance> (thresh + 10) and distance1 > (thresh + 10)  :
                    print(i)
                    i = len(cl12)
                    break
        
        color2 = np.zeros([3])
        
        color2[0] =x1[1][0]
        
        color2[1] =x1[1][1]
        
        color2[2] =x1[1][2]
#        print("colorpil")
#        print(color2)
#        print("colorpil")
        return color2
    def colorConcat(colorN, colorO):
        len1 = colorO.shape[0] +1
        coloring1 = np.zeros([len1,3])
        coloring1[0:len1-1,:]= colorO
        coloring1[len1-1,:] = colorN
        return coloring1
    #@jit(nopython=True)
    @autojit
    def color4get(new_im, thresh, colors, flag, num_max):
        distance = np.zeros(colors.shape[0])
        cl2 = new_im.getcolors(new_im.size[0]*new_im.size[1])
        cl12 =sorted(cl2, reverse=True)
        #print(num_max)
        #print("num_max")
        x1 = cl12[0]
        for i in range(num_max, len(cl12)):
            x1 = cl12[i]
            #print(x1)
            if x1[1][2]<250 and x1[1][2]> 10:
                if flag ==1 and (x1[1][2]>230 or x1[1][2]< 50 ):
                    for k in range(0, colors.shape[0]):
                        distance[k] = ImageAlter.dist_v(x1[1][:], colors[k,:])

                else:
                    for k in range(0, colors.shape[0]):
                        distance[k] = ImageAlter.dist1(x1[1][:], colors[k,:])
                if  np.all(distance> (thresh + 10))  :
                    #print(i)
                    i = len(cl12)
                    break
        
        color2 = np.zeros([3])
        #print('x1', x1)
        color2[0] =x1[1][0]
        
        color2[1] =x1[1][1]
        
        color2[2] =x1[1][2]
        #print("colorpil")
        #print(color2)
        #print("colorpil")
        return color2
    
    def havingColor(model, flag, num):
        model_new = model +1;
        counter = sum(model_new[model_new==1])
        if counter <num:
           flag = 0
        return flag
#model_new1 = Color2Service.unreshaping(model1, img1)
#new_im1, img11 =  Color2Service.modeling23color(model_new1, img1)
#color_centre11 = Color2Service.colorfindergram(new_im1, thresh)
#color121 = Color2Service.color2get(new_im1, thresh)
#color_centre11 = Color2Service.mergeColor(color_centre11, color121)
#model31 = Color2Service.finalModel(thresh,color_centre11, img1, model_new1, flag1, 6)
#model_new2 = Color2Service.reshaping(model31)
#num =number + 2
#colors1 = FinalMerge.colorConcat(colors, color_centre11)
#admat = FinalMerge.adMat(num, colors1, thresh, flag1)
#print(admat)
#model22, number1 = FinalMerge.mergeColor(model_new2, num, admat)
#print(np.size(model2))
#number, model1=FinalMerge.modelEnhance(model22, num)
