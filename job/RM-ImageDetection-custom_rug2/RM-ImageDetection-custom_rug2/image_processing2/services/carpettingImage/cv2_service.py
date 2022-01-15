import cv2
import numpy as np
from skimage.transform import resize
from services.utility.utility_service import UtilityService
from services.customRug.image_service import ImageAlter
########################################################################
class CV2Service:
    def imread_remote(url):
        return UtilityService.image_reader(url)

    def imread_local(url):
        return cv2.imread(url)

    def imdecode(img_array):
            return cv2.imdecode(img_array, -1)

    def cvtColor(img):
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
    def cvtColor1(img):
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img1
    def cvtColorHsv(img):
        img1 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        return img1

    def rgb2gray(rgb):
        r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    def cv2imread(url):
        image = CV2Service.imread_remote(url)
        img_array = np.array(bytearray(image), dtype=np.uint8)
        img1  = CV2Service.cvtColor(CV2Service.imdecode(img_array))
        imag1 = img1#ImageAlter.crop(img1)
        img =  imag1#[4:-4,4:-4,:]
        return img

        
    def carpet_extend(carpet, carpType):
        carp = cv2.resize(carpet,(500,500))
        r,c,a = np.shape(carpet)
        carpet = carpet[20:r-20,20:c-20,:]
        r,c,a = np.shape(carpet)
        imcarp = np.empty([10 * r, 15 * c, 3], dtype='uint8')
        imcarp2 = np.empty([10*r,c,3],dtype='uint8')
        if carpType ==1:
            for i in range(0,r*10):
                    imcarp2[i,:,:]= carpet[np.mod(i,r),:,:]
            for j in range(0,c*15):
                    imcarp[:,j,:]= imcarp2[:,np.mod(j,c),:]
        elif carpType ==2 :            
            for i in range(0,r*10):
                    if np.mod(np.int((i-np.mod(i,r))/r),2)==0:
                            imcarp2[i,:,:]= carpet[np.mod(i,r),:,:]
                    else:
                            imcarp2[i,:,:]= carpet[r-1-np.mod(i,r),:,:]

            for j in range(0,c*15):
                if np.mod(np.int((j-np.mod(j,c))/c),2)==0:
                    imcarp[:,j,:]= imcarp2[:,np.mod(j,c),:]
                else:
                    imcarp[:,j,:]= imcarp2[:,c-1-np.mod(j,c),:]
        elif carpType == 3:
            for i in range(0,r*10):
                imcarp2[i,:,:] = carpet[np.mod(i,r), :, :]
            for j in range(0,c*15):
                if np.mod(np.int((j-np.mod(j,c))/c),2)==0:
                    imcarp[:,j,:]= imcarp2[:,np.mod(j,c),:]
                else:
                    imcarp[:,j,:]= imcarp2[:,c-1-np.mod(j,c),:]


        else:
            for i in range(0,r*10):
                    if np.mod(np.int((i-np.mod(i,r))/r),2)==0:
                            imcarp2[i,:,:]= carpet[np.mod(i,r),:,:]
                    else:
                            imcarp2[i,:,:]= carpet[r-1-np.mod(i,r),:,:]
            for j in range(0,c*15):
                    imcarp[:,j,:]= imcarp2[:,np.mod(j,c),:]


        return imcarp

    def perspective_maker1(extended_carpet):
        rows,cols,ch = extended_carpet.shape
        pts1 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
        pts2 = np.float32([[0, np.int(rows/7)], [np.int(4 * cols / 7), 0], [np.int(cols / 5), rows], [cols, np.int(rows / 3)]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(extended_carpet,M,(cols,rows))
        image = np.copy(dst)
        im1 = resize(image, (3000, 5000), anti_aliasing=True)
        im2 = np.uint8(im1 * 255)
        im2 = im2 [450:2000, 1000:2000, :]
        return im2
    def perspective_maker2(extended_carpet):
        rows,cols,ch = extended_carpet.shape
        pts1 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
        pts2 = np.float32([[np.int(cols/3),0],[np.int(2*cols/3),0],[0,np.int(3*rows/6)],[cols,np.int(3*rows/6)]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(extended_carpet,M,(cols,rows))
        image = np.copy(dst)
        im1 = resize(image, (3000, 5500), anti_aliasing=True)
        im2 = np.uint8(im1 * 255)
        im2 = im2[100:1500,1800:4300,:]
        return im2



    def Cv2resizing(image,col, row):
        return cv2.resize(image,(col,row))
    def image2byte(image):
        success, encoded_image = cv2.imencode('.png', image)
        content2 = encoded_image.tobytes()
        return content2
