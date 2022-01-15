# -*- coding: utf-8 -*-
import numpy as np
from services.customRug.image_service import ImageAlter
from PIL import Image
from services.customRug.dominant_service import DominantService
from numba import jit, autojit, njit
class Color2Service:
    #@jit(nopython=True)
    def modeling2color(model2, img1):
        for i in range(0,img1.shape[0]):
            for j in range(0,img1.shape[1]):
                if model2[i,j]>0:
                     img1[i,j,:] = [0,0,0]
        new_im = Image.fromarray(DominantService.croping(img1))
        return new_im, img1

    def color2get(new_im, thresh, x, flag, num_max):
        
        cl2 = new_im.getcolors(new_im.size[0]*new_im.size[1])
        cl12 =sorted(cl2, reverse=True)
        for i in range(num_max, len(cl12)):
            x1 = cl12[i]
            if x1[1][2]<250 and x1[1][2]> 10:
                if flag ==1 and (x1[1][2]>230 or x1[1][2]< 50 ):
                    distance = ImageAlter.dist_v(x1[1][:], x[1][:])
                else:
                    distance = ImageAlter.dist1(x1[1][:], x[1][:])
                if  distance> (thresh + 10) :
                    print(i)
                    num_max =i
                    i = len(cl12)
                    break
        
        color2 = np.zeros([3])
        
        color2[0] =x1[1][0]
        
        color2[1] =x1[1][1]
        
        color2[2] =x1[1][2]
        print("colorpil")
        print(color2)
        print("colorpil")
        return color2, x1, num_max
    def colorConcat(color2, color1):
        len1 = 2
        coloring1 = np.zeros([len1,3])
        coloring1[0,:]= color1
        coloring1[1,:] = color2
        return coloring1
    #@jit(nopython=True)
    #@autojit
    def finalModel(thresh, color2, img1, model2, flag, enhNum):
        for i in range(0,img1.shape[0]):
            for j in range(0,img1.shape[1]):
                if model2[i,j]==0:
                    if flag ==1 and (color2[2]>230 or color2[2]< 50):
                        distance = ImageAlter.dist_v(color2[:], img1[i,j,:])
                    else:
                        distance = ImageAlter.dist1(color2[:], img1[i,j,:]) 
                    if distance < thresh:
                        model2[i,j] = enhNum-1
        model3 =model2 #ImageAlter.enhancing(model2, enhNum)
        return model3
    


    def reshaping(model):
        model_new = np.reshape(model,[model.shape[0]*model.shape[1]])
        return model_new
    def unreshaping(model, img):
        model_new = np.reshape(model,[img.shape[0],img.shape[1]])
        return model_new
    def reshaping_img(img):
        img_new = np.reshape(img,[img.shape[0]*img.shape[1]*3])
        return img_new
