# -*- coding: utf-8 -*-

from services.customRug.dominant_service import DominantService
from services.customRug.color2_service import Color2Service
from services.carpettingImage.cv2_service import CV2Service
import json
import numpy as np
from services.utility.utility_reader import UtilityReader
from services.customRug.final_merge import FinalMerge
class MainService:
    def __init__(self, url, flag):
        self.url = url
        self.flag = int(flag)
    def start_clustering(self, socket):        
        im  = DominantService.pilimread(self.url)
        img = CV2Service.cv2imread(self.url)
        x = DominantService.getColors(im)
        flag1 = DominantService.rgbOrhsv(x, self.flag)
        thresh = 32
        #flag1 = 1
        if flag1 <1 :
            print('hi')
            model2, img1 = DominantService.RGB(x, img, thresh)
            #colorC1 = np.copy(x)
        else:
            print('bye')
            model2, img1, colorC1, x = DominantService.HSV(x, img, thresh)
        print("part 123")
        new_im, img1 =  Color2Service.modeling23color(model2, img1)
        color_centre1 = Color2Service.colorfindergram(new_im, thresh)
        color12 = Color2Service.color2get(new_im, thresh)
        #color_centre1 = Color2Service.mergeColor(color_centre1, color12)
        model3 = Color2Service.finalModel(thresh,color_centre1, img1, model2, flag1, 4)
        model_new = Color2Service.reshaping(model3)
        s = DominantService.size_img(img)
        colorC23 = Color2Service.findColorC(model3, img)
        colors = Color2Service.colorConcat(color_centre1, x)
        print(colorC23)
        ############
        num =3
        admat = FinalMerge.adMat(num, colors, thresh, flag1)
        print(admat)
        model2, number1 = FinalMerge.mergeColor(model_new, num, admat)
        print(np.size(model2))
        number, model1=FinalMerge.modelEnhance(model2, num)
        print("part 101")
        ###################################################

#        model1 = model_new
        #################################################
        serialized_data = json.dumps({"colors": colors.tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
        socket.write_message(serialized_data)
        
