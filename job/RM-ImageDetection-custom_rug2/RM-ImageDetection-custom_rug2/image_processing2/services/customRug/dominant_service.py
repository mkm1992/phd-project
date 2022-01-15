import numpy as np
from io import BytesIO
from PIL import Image, ImageDraw
from services.utility.utility_service import UtilityService
from services.carpettingImage.cv2_service import CV2Service
from services.customRug.image_service import ImageAlter
#from numba import jit, float64, int32, double, void



class DominantService:
    def pilimread(url):
        image_url=UtilityService.image_reader(url)
        im = Image.open(BytesIO(image_url))
        return im
    def croping(img):
        imag1 = ImageAlter.crop(img)
        imgC =  imag1[10:-10,10:-10,:]
        return imgC
    def getColors(im):
        x =max(im.getcolors(im.size[0]*im.size[1]))
        cl = im.getcolors(im.size[0]*im.size[1])
        cl1 =sorted(cl, reverse=True)
#        if x[1]==(255,255,255):
#            x = cl1[1]
        for i in range(0, len(cl1)):
            x = cl1[i]
            if x[1][0]<240 and x[1][1]<240 and x[1][2]<240:
                print(i)
                i = len(cl1)
                break
        #thresh = 30
        return x 


    def RGB(x, img, thresh):
        color12 = np.zeros([3])
        color12[0] =x[1][0]
        color12[1] =x[1][1]
        color12[2] =x[1][2]
        img21 = np.zeros([img.shape[0] , img.shape[1]])
        img1 = np.copy(img)
        print('rgb')
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if ImageAlter.dist1(color12, img[i,j,:])<thresh:
                    img21[i,j]=1 
                if (x[1][0]<50 and x[1][1]<50 and x[1][2]<50) and (img[i,j,0]<60 and img[i,j,1]<60 and img[i,j,2]<60 ):
                    img21[i,j] =1
        print("color12")
        print(color12)
        print("color12")
        model2 =ImageAlter.enhancing(img21, 2)
        return model2, img1
    #@jit(int32[:,:], int32[:,:,:], int32[:], int32, int32, int32[:](int32, int32[:,:,:],int32))
    
    def HSV(x, img, thresh):
        num_max = 0
        imgb = CV2Service.cvtColor1(img)
        imgH = CV2Service.cvtColorHsv(imgb)
        im = Image.fromarray(DominantService.croping(imgH))
        img1 = np.copy(imgH)
        #color1 = DominantService.meanColoring(im, thresh, 1)
        x =max(im.getcolors(im.size[0]*im.size[1]))
        cl = im.getcolors(im.size[0]*im.size[1])
        cl1 =sorted(cl, reverse=True)
        for i in range(0, len(cl1)):
                x = cl1[i]
                if x[1][2]<250:
                    print(i)
                    num_max = i
                    i = len(cl1)
                    break
        
        print('hsv')
        color12 = np.zeros([3])
        color12[0] =x[1][0]
        color12[1] =x[1][1]
        color12[2] =x[1][2]
        img21 = np.zeros([img.shape[0] , img.shape[1]])
        colorC1 = np.zeros([3])
        count = 0
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                if color12[2]> 230 or color12[2]< 50:
                    distance_cen = ImageAlter.dist_v(color12, imgH[i,j,:])
                else:
                    distance_cen = ImageAlter.dist1(color12, imgH[i,j,:])
                if distance_cen < thresh:
                    img21[i,j]=1   
                    colorC1 += img[i,j,:]
                    count +=1
        colorC1 = np.round(colorC1/count)
        model2 =ImageAlter.enhancing(img21, 2)
        return model2, img1, colorC1, x, num_max, color12
    def size_img(img):
        s = np.zeros(2)
        s[0] =img.shape[0]
        s[1] = img.shape[1]
        return s
    def meanColoring(im, thresh, flag):
        cl = im.getcolors(im.size[0]*im.size[1])
        cl1 =sorted(cl, reverse=True)
        x =max(im.getcolors(im.size[0]*im.size[1]))
        i = 0
            
        for i in range(0, len(cl1)):
            x = cl1[i]
            if flag ==1 and (x[1][2]<230 or x[1][2]> 50 ):
                print(i)
                i = len(cl1)
                break
        count  = 1
        color = np.dot(x[1],x[0])
        sigma = x[0]
        for j in range(i+1,len(cl1)):
            x1 = cl1[j]
            if ImageAlter.dist1(x1[1][:],x[1][:])<thresh/2:
                count += 1
                color += np.dot(x1[1],x1[0]) 
                sigma += x1[0]
        color1 = np.dot(color,1/sigma) 
        return color1
            