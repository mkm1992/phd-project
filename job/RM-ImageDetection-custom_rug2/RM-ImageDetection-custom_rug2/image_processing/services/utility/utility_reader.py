# -*- coding: utf-8 -*-
import numpy as np
from services.carpettingImage.cv2_service import CV2Service

class UtilityReader:
    def imread(url):
            image = CV2Service.imread_remote(url)
            img_array = np.array(bytearray(image), dtype=np.uint8)
            return CV2Service.cvtColor(CV2Service.imdecode(img_array))