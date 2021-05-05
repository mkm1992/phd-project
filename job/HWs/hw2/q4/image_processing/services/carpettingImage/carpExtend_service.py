import numpy as np
from skimage.transform import resize
import cv2
class CarpetPerspective:
    def Carpet150(mat1):
        mat1 = cv2.resize(mat1,(500,500))
        r,c,a=np.shape(mat1)
        mat1 = mat1[20:r-20,20:c-20,:]
        r,c,a=np.shape(mat1)
        imcarp = np.empty([10*r,15*c,3],dtype='uint8')
        for i in range(0,r*10):
            for j in range(0,c*15):
                imcarp[i,j,:]= mat1[np.mod(i,r),np.mod(j,c),:]
        return imcarp
    def PerspectiveMaker(imcarp):
        rows,cols,ch = imcarp.shape
        pts1 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
        pts2 = np.float32([[0,np.int(rows/7)],[np.int(4*cols/7),0],[np.int(cols/5),rows],[cols,np.int(rows/3)]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(imcarp,M,(cols,rows))
        image = np.copy(dst)
        im1=resize(image, (3000, 5000),   anti_aliasing=True)
        im2 = np.uint8(im1*255)
        return im2

