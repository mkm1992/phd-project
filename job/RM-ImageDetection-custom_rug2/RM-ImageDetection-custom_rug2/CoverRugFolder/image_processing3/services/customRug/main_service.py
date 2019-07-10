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
import time
class MainService:
    def __init__(self, url, flag):
        self.url = url
        self.flag = int(flag)
        #self.thresh = int(thresh)
    def start_clustering(self, socket):    
        start = time.time()
        num_flg = 6
        im  = DominantService.pilimread(self.url)
        img = CV2Service.cv2imread(self.url)
        img_correct = np.copy(img)
        x = DominantService.getColors(im)
        thresh = 35
        num_max = 0
        if self.flag <1 :
            print('hi')
            model2, img1 = DominantService.RGB(x, img, thresh)
            #colorC1 = np.copy(x)
        else:
            print('bye')
            model2, img1, colorC1, x, num_max, color1 = DominantService.HSV(x, img, thresh)
        print("part 1 is finished")
#        if sum(model2[model2==0]) < 10:
#            num_flg= num_flg -1
        new_im, img1 =  Color2Service.modeling2color(model2, img1)
        color2, x1, num_max = Color2Service.color2get(new_im, thresh, x, self.flag, num_max)
        #color_centre1 = Color2Service.mergeColor(color_centre1, color12)
        model3 = Color2Service.finalModel(thresh, color2, img1, model2, self.flag, 3)
        colors12 = Color2Service.colorConcat(color2, color1)
        print("part 2 is finished")
#        if sum(model3[model3==0]) < 10:
#            num_flg= num_flg -1
        new_im, img1 =  Color2Service.modeling2color(model3, img)
        color3 = Color3Service.color3get(new_im, thresh, x, x1, self.flag, num_max)
        model4 = Color2Service.finalModel(thresh, color3, img1, model3, self.flag, 4)
        colors123 = Color3Service.colorConcat(color3, colors12)
        print("part 3 is finished")
#        if sum(model4[model4==0]) < 10:
#            num_flg= num_flg -1
        ##################################################################################
        new_im, img1 =  Color2Service.modeling2color(model4, img)
        color4 = Color3Service.color4get(new_im, thresh+10, colors123, self.flag, num_max)
        model5 = Color2Service.finalModel(thresh+10, color4, img1, model4, self.flag, 5)
        colors1234 = Color3Service.colorConcat(color4, colors123)
        print("part 4 is finished")
#        if sum(model5[model5==0]) < 10:
#            num_flg= num_flg -1
        new_im, img1 =  Color2Service.modeling2color(model5, img)
        color5 = Color3Service.color4get(new_im, thresh+20, colors1234, self.flag, num_max)
        model6 = Color2Service.finalModel(thresh+20, color5, img1, model5, self.flag, 6)
        colors12345 = Color3Service.colorConcat(color5, colors1234)
        print("part 5 is finished")
#        if sum(model6[model6==0]) < 10:
#            num_flg= num_flg -1
        new_im, img1 =  Color2Service.modeling2color(model6, img)
        print("6-1 finised")
        color6 = Color3Service.color4get(new_im, thresh+20, colors12345, self.flag, num_max)
        print("6-2 finised")
        model6 = Color2Service.finalModel(thresh+20, color6, img1, model6, self.flag, 7)
        print("6-3 finised")
#        model6 = ImageAlter.enhancing(model6, 7)
        colors123456 = Color3Service.colorConcat(color6, colors12345)
        print("part 6 is finished",num_flg)
        colorCen = ColorCenter.colorCent(model6, img_correct, num_flg)
        print(np.shape(model6))
        print(np.shape(img_correct))
        print('shapes')
        model_new = Color2Service.reshaping(model6)
        s = DominantService.size_img(img)
        colors =colors123456
        
        ############
        num = num_flg+1
        admat = FinalMerge.adMat(num, colorCen, thresh, self.flag)
        print(admat)
        model66, number1 = FinalMerge.mergeColor(model_new, num, admat)
        print(np.size(model2))
        number, model1=FinalMerge.modelEnhance(model66, number1)
       
        print("Merge part")
        end  = time.time()
        print(end -start)
        ###################################################

#        model1 = model_new
#        number =6
        #################################################
        serialized_data = json.dumps({"colors": colorCen[0:number+1].tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
        socket.write_message(serialized_data)
        
