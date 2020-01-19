# -*- coding: utf-8 -*-

import numpy as np
from numba import jit, int32
from numba import jit, autojit
class ColorCenter:
    #@jit(int32[:,:](int32[:,:],int32[:,:], int32))
    @autojit
    def colorCent(model, img, num):
        color_center = np.zeros([num+1,3])
        for i in range(0, num+1):
             a = (img[model == i])
             print("---a---",i)
             b = a.mean(axis = (0))
             print("---b---",b)
             color_center[i,0] = int(b[0])
             color_center[i,1] = int(b[1])
             color_center[i,2] = int(b[2])
        print(color_center)
        print("color_center")
        return color_center
        