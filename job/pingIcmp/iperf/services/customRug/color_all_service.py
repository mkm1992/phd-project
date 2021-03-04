# -*- coding: utf-8 -*-

from services.customRug.dominant_service import DominantService
from services.customRug.color2_service import Color2Service
from services.customRug.color3_service import Color3Service
from services.carpettingImage.cv2_service import CV2Service
import json
import numpy as np
from services.utility.utility_reader import UtilityReader
from services.customRug.final_merge import FinalMerge
from services.customRug.color_center import ColorCenter
from services.customRug.image_service import ImageAlter

class ColorAllService:
    def color1(x, img, thresh):
        model2, img1, colorC1, x, num_max, color1 = DominantService.HSV(x, img, thresh)
        return model2, img1, colorC1, x, num_max, color1
        
    def color2(model2, img1, thresh, flag, num_max, x, color1, flag_havingColor ):
        if flag_havingColor == 1:
            new_im, img1 =  Color2Service.modeling2color(model2, img1)
            color2, x1, num_max = Color2Service.color2get(new_im, thresh, x, flag, num_max)
            #color_centre1 = Color2Service.mergeColor(color_centre1, color12)
            model3 = Color2Service.finalModel(thresh, color2, img1, model2, flag, 3)
            colors12 = Color2Service.colorConcat(color2, color1)
            return colors12, model3, x1, num_max
        else:
            print('oh no')
            return 1,1,1,1;
    def color3(model3, img, flag, num_max, thresh, x, x1, colors12, flag_havingColor):
        if flag_havingColor == 1:
            new_im, img1 =  Color2Service.modeling2color(model3, img)
            color3 = Color3Service.color3get(new_im, thresh, x, x1, flag, num_max)
            model4 = Color2Service.finalModel(thresh, color3, img1, model3, flag, 4)
            colors123 = Color3Service.colorConcat(color3, colors12)
            return colors123, model4
        else:
            print('oh no')
            return 1,1
    def otherColors(img, colors123, flag, num_max, thresh, model4, flag_havingColor,iteration ):
        if  flag_havingColor == 1:
            new_im, img1 =  Color2Service.modeling2color(model4, img)
            color4 = Color3Service.color4get(new_im, thresh+10, colors123, flag, num_max)
            model5 = Color2Service.finalModel(thresh+10, color4, img1, model4, flag, iteration)
            colors1234 = Color3Service.colorConcat(color4, colors123)
            return model5, colors1234
        else:
            print('oh no')
            return 1,1;
    def afterFindingColor(model6, img_correct, num_flg, colors123456, flag, thresh):
        print(model6)
        colorCen = ColorCenter.colorCent(model6, img_correct, num_flg)
        model_new = Color2Service.reshaping(model6)
        s = DominantService.size_img(img_correct)
        #colors =colors123456
        num = num_flg+1
        admat = FinalMerge.adMat(num, colorCen, thresh, flag)
        print(admat)
        print("num", num)
        model66, number1 = FinalMerge.mergeColor(model_new, num, admat)
        print("number1", number1)
        number, model1=FinalMerge.modelEnhance(model66, number1)
        print("number", number)
        return model1, number, colorCen, s
    def afterFindingColor1(model6, img_correct, num_flg, colors123456, flag, thresh,percentage):
        print(model6)
        colorCen = ColorCenter.colorCent(model6, img_correct, num_flg)
        model_new = Color2Service.reshaping(model6)
        s = DominantService.size_img(img_correct)
        #colors =colors123456
        num = num_flg+1
        admat = FinalMerge.adMat(num, colorCen, thresh, flag)
        print(admat)
        print("num", num)
        model66, number1 = FinalMerge.mergeColor(model_new, num, admat)
        print("number1", number1)
        number, model1=FinalMerge.modelEnhance1(model66, number1,percentage)
        print("number", number)
        return model1, number, colorCen, s
    
        
    
         