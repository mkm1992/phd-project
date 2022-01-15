# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:07:03 2019

@author: mkm1992 "Mojdeh Karbalaee Motalleb"
"""

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
from services.customRug.color_all_service import ColorAllService
import time
class MainService:
    def __init__(self, url, flag):
        self.url = url
        self.flag = int(flag)
    def start_clustering(self, socket):    
        start = time.time()
        num_flg = 6
        number_color = 1
        flag_havingColor =  np.ones([6]);
        num_haveingColor = 1000;
        im  = DominantService.pilimread(self.url)
        img = CV2Service.cv2imread(self.url)
        img_correct = np.copy(img)
        x = DominantService.getColors(im)
        thresh = 35
        num_max = 0
        percentage = 0.003
        s = DominantService.size_img(img)
        model2, img1, colorC1, x, num_max, color1 = ColorAllService.color1(x, img, thresh)
        flag_havingColor[0] = Color3Service.havingColor(model2, flag_havingColor[0], num_haveingColor)
        if flag_havingColor[0] == 0:
            print('wow')
            number  = 1
            #colorCen = ColorCenter.colorCent(model2, img_correct, 1)
            #model1= Color2Service.reshaping(model2)
            model1, number, colorCen, s = ColorAllService.afterFindingColor1(model2, img_correct, 1, colorC1, self.flag, thresh)
            serialized_data = json.dumps({"colors": colorCen[0:number+1].tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
            socket.write_message(serialized_data)
            return
        #print("part 1 is finished",sum(model2[model2==1]))
        colors12, model3, x1, num_max = ColorAllService.color2(model2, img1, thresh, self.flag, num_max, x, color1, flag_havingColor[0])
        flag_havingColor[1] = Color3Service.havingColor(model3, flag_havingColor[0], num_haveingColor)
        if flag_havingColor[1] == 0 and flag_havingColor[0] == 1:
            print('wow')
            number  = 2
            #colorCen = ColorCenter.colorCent(model3, img_correct, 2)
            #model1= Color2Service.reshaping(model3)
            model1, number, colorCen, s = ColorAllService.afterFindingColor1(model2, img_correct, 1, colors12, self.flag, thresh, percentage)
            serialized_data = json.dumps({"colors": colorCen[0:number+1].tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
            socket.write_message(serialized_data)
            return
        #print("part 2 is finished",sum(model3[model3==2]))
        colors123, model4 = ColorAllService.color3(model3, img, self.flag, num_max, thresh, x, x1, colors12, flag_havingColor[1])
        flag_havingColor[2] = Color3Service.havingColor(model4, flag_havingColor[1], num_haveingColor)
        if flag_havingColor[2] == 0 and  flag_havingColor[1] == 1:
            print('wow')
            number  = 3
            #colorCen = ColorCenter.colorCent(model4, img_correct, 3)
            #model1= Color2Service.reshaping(model4)
            model1, number, colorCen, s = ColorAllService.afterFindingColor1(model2, img_correct, 1, colors123, self.flag, thresh, percentage)
            serialized_data = json.dumps({"colors": colorCen[0:number+1].tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
            socket.write_message(serialized_data)
            return
        #print("part 3 is finished",sum(model4[model4==3]))
        modelN = model4
        colorsall = colors123
        #print(colorsall)
        for i in range(4,7):
            modelN, colorsall = ColorAllService.otherColors(img, colorsall, self.flag, num_max, thresh, modelN, flag_havingColor[i-2],i+1)
            #print(colorsall)
            flag_havingColor[i-1] = Color3Service.havingColor(modelN, flag_havingColor[i-2], num_haveingColor)
           # print("part  is finished",sum(modelN[modelN==i]))
            if (flag_havingColor[i-1] == 0 and  flag_havingColor[i-2] == 1)or i ==6:
                print('wow',i)
                model1, number, colorCen, s = ColorAllService.afterFindingColor(modelN, img_correct, i, colorsall, self.flag, thresh)
                #model1, number, colorCen, s = ColorAllService.afterFindingColor(Color2Service.unreshaping(model1,img_correct), img_correct, number, colorCen, self.flag, thresh)
                #number  = i
                serialized_data = json.dumps({"colors": colorCen[0:number+1].tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
                socket.write_message(serialized_data)
                return
                break
            
#            number = 6
        print('finish')
#            model1= Color2Service.reshaping(modelN)
#            serialized_data = json.dumps({"colors": colorsall.tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
#            socket.write_message(serialized_data)
#        model5, colors1234 = ColorAllService.otherColors(img, colors123, self.flag, num_max, thresh, model4, flag_havingColor[2])
#        flag_havingColor[3] = Color3Service.havingColor(model5, flag_havingColor[2], num_haveingColor)
#        if flag_havingColor[3] == 0 and  flag_havingColor[2] == 1:
#            number  = 4
#            model1= Color2Service.reshaping(model5)
#            serialized_data = json.dumps({"colors": colors1234.tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
#            socket.write_message(serialized_data)
#        print("part 4 is finished")
#        model6, colors12345 = ColorAllService.otherColors(img, colors1234, self.flag, num_max, thresh, model5, flag_havingColor[3])
#        flag_havingColor[4] = Color3Service.havingColor(model5, flag_havingColor[2], num_haveingColor)
#        if flag_havingColor[4] == 0 and  flag_havingColor[3] == 1:
#            number  = 5
#            model1= Color2Service.reshaping(model6)
#            serialized_data = json.dumps({"colors": colors12345.tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
#            socket.write_message(serialized_data)
#        print("part 5 is finished")  
#        model6, colors123456 = ColorAllService.otherColors(img, colors12345, self.flag, num_max, thresh, model6, flag_havingColor[4])
#        print("part 6 is finished",num_flg)
#        colorCen = ColorCenter.colorCent(model6, img_correct, num_flg)
#        print(np.shape(model6))
#        print(np.shape(img_correct))
#        print('shapes')
#        model_new = Color2Service.reshaping(model6)
#        s = DominantService.size_img(img)
#        colors =colors123456
#        
#        ############
#        num = num_flg+1
#        admat = FinalMerge.adMat(num, colorCen, thresh, self.flag)
#        print(admat)
#        model66, number1 = FinalMerge.mergeColor(model_new, num, admat)
#        print(np.size(model2))
#        number, model1=FinalMerge.modelEnhance(model66, number1)
#       
#        print("Merge part")
#        end  = time.time()
#        print(end -start)
#        ###################################################
#
##        model1 = model_new
##        number =6
#        #################################################
#        serialized_data = json.dumps({"colors": colorCen[0:number+1].tolist(), "model_1d": model1.tolist(), "shape":s.tolist(), "number":number })
#        socket.write_message(serialized_data)         

        
        