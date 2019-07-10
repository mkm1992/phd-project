# -*- coding: utf-8 -*-
import numpy as np
from services.customRug.image_service import ImageAlter
import colorgram
from PIL import Image
from services.customRug.dominant_service import DominantService
from services.customRug.color2_service import Color2Service



    
    
model_new1 = Color2Service.unreshaping(model1, img1)
new_im1, img11 =  Color2Service.modeling23color(model_new1, img1)
color_centre11 = Color2Service.colorfindergram(new_im1, thresh)
color121 = Color2Service.color2get(new_im1, thresh)
color_centre11 = Color2Service.mergeColor(color_centre11, color121)
model31 = Color2Service.finalModel(thresh,color_centre11, img1, model_new1, flag1, 6)
model_new2 = Color2Service.reshaping(model31)
num =number + 2
colors1 = FinalMerge.colorConcat(colors, color_centre11)
admat = FinalMerge.adMat(num, colors1, thresh, flag1)
print(admat)
model22, number1 = FinalMerge.mergeColor(model_new2, num, admat)
print(np.size(model2))
number, model1=FinalMerge.modelEnhance(model22, num)