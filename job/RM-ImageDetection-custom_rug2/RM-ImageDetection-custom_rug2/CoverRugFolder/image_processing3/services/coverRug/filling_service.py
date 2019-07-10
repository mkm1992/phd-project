# -*- coding: utf-8 -*-

import numpy as np

class CoverRug:
    def covering(img, dst):
        imax,jmax,ch = np.shape(img)
        for i in range(0,imax):
            for j in range(0,jmax):
                if  (dst[i,j,0]>0 or dst[i,j,1]>0 or dst[i,j,2]>0 ):
                    img[i,j,:]= dst[i,j,:]
        return img

        