# -*- coding: utf-8 -*-

import numpy as np
from services.customRug.image_service import ImageAlter
import colorsys

class FinalMerge:
    def adMat(num, colorCenter, thresh, flag):
        adjancyMat = np.eye(num)
        count = 0
        distan = 0
        for i in range(0, num):
            for j in range(0, num):
                if flag==1 :
                    a =colorsys.hsv_to_rgb(colorCenter[i,0]/255, colorCenter[i,1]/255,colorCenter[i,2]/255)
                    b =colorsys.hsv_to_rgb(colorCenter[j,0]/255, colorCenter[j,1]/255,colorCenter[j,2]/255)
                    distan= ImageAlter.dist1(np.dot(a,255), np.dot(b,255))
                else:
                    a = colorCenter[i,:]
                    b = colorCenter[j,:]
                    distan= ImageAlter.dist1(a, b)
#                print("a,b")
#                print(a)
#                print(b)
                if distan< thresh-10:
                    adjancyMat[i,j] =1
                    count += 1
        return adjancyMat
    def mergeColor(model, num, adjancyMat):
        counter = 0
        #colorC = np.zeros([num,3])
        for i in range(0, num):
            for j in range(i+1, num):
                #model[model==(i+1)] = i+1-counter
                if adjancyMat[i,j] ==1:
                   model[model==(j+1)] = i+1
                   counter += 1
                   adjancyMat[j,i] = 0
        number = num - counter
        return model , number
    def modelEnhance(model, number):
        count = 1
        size_tot = model.shape[0]
        model_n = np.zeros(size_tot)
        for i in range(0, number):
            #if (sum(model[model==i+1]))> 0:
            if (sum(model[model==i+1])/(i+1))/size_tot > 0.0005:
                print(count)
                print("okey")
                print((sum(model[model==i+1])/(i+1))/size_tot)
                model_n[model==(i+1)] = count
                count += 1
        return count-1, model_n
    def colorConcat(color1, color2):
        size_tot = color1.shape[0]+ color2.shape[0]
        coloring1 = np.zeros([size_tot,3])
        coloring1[0:color1.shape[0],:]= color1
        coloring1[color1.shape[0]:,:]= color2
        return coloring1

                
                
            
    
                    

            