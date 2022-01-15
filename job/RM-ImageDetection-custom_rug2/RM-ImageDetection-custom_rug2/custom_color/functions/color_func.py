# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:44:01 2019

@author: mkm1992
"""
import colorsys
import numpy as np

def colorCent_hsv(hsl):
    h=hsl[0]
    s=hsl[1]
    l=hsl[2]
    hsv_raw_color = colorsys.hls_to_rgb(h / 255, s/ 255, l / 255)
    hsv_color = np.zeros([3])
    hsv_color[0] =  np.floor(hsv_raw_color[0] *255) 
    hsv_color[1] =  np.floor(hsv_raw_color[1] *255)
    hsv_color[2] =  np.floor(hsv_raw_color[2] * 255)
    if hsl[2]>240 :
        hsv_color[0]=255
        hsv_color[1] = 255
        hsv_color[2] =255
    return np.array(hsv_color)

def colorCent_rgb(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    hsv_raw_color = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    hsv_color = np.zeros([3])
    hsv_color[0] =  np.floor(hsv_raw_color[0] *255) 
    hsv_color[1] =  np.floor(hsv_raw_color[1] *255)
    hsv_color[2] =  np.floor(hsv_raw_color[2] * 255)
    return np.array(hsv_color)