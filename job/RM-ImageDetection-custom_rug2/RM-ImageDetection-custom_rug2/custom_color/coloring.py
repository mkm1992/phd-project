# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:03:30 2019

@author: mojdeh
"""
import matplotlib.pyplot as plt
from colorthief import ColorThief
import numpy as np
name_nat = 'm11.jpg'
name =  'input/'+name_nat
color_thief = ColorThief(name)
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=6)
i =5
x = palette
color1 = np.zeros([2,2,3])

color1[:,:,0] =x[i][2]

color1[:,:,1] =x[i][1]

color1[:,:,2] =x[i][0]

plt.imshow(color1.astype('float32'))
plt.show()