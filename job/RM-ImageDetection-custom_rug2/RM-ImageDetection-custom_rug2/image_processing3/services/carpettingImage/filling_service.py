import numpy as np
from services.carpettingImage.cv2_service import CV2Service
class FloorFillService:
    def fill1(perspective_carpet, back_floor):
        #perspective_carpet = perspective_carpet[450:2000, 1000:2000, :]
        imax,jmax,ch = np.shape(back_floor)
        img3 = np.copy(back_floor)
        img2gray = CV2Service.rgb2gray(img3)
        for ii in range(0, imax):
            for jj in range(0, jmax):
                if img2gray[ii, jj] == 0: 
                    back_floor[ii, jj, :] = perspective_carpet[ii, jj, :]
        return back_floor
    def fill2(perspective_carpet, back_floor):
        #perspective_carpet = perspective_carpet[450:2000, 1000:2000, :]
        imax,jmax,ch = np.shape(back_floor)
        img3 = np.copy(back_floor)
        img2gray = CV2Service.rgb2gray(img3)
        for ii in range(0, imax):
            for jj in range(0, jmax):
                if img2gray[ii, jj] == 0: 
                    back_floor[ii, jj, :] = perspective_carpet[ii-1200, jj, :]
        return back_floor


