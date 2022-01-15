from services.carpettingImage.cv2_service import CV2Service
from services.carpettingImage.filling_service import FloorFillService
from services.coverRug.filling_service import CoverRug
from services.coverRug.perspective_service import RugPerspectivePoint
import base64
import numpy as np
import cv2
from matplotlib import pyplot as plt
###############
class MainService():
    def __init__(self, url):
        self.url = url
        self.read_back_floor()
    def read_back_floor(self):
        self.backFloor = self.imread_local("./public/floor/n7.png")

    def imread(self, url):
        image = CV2Service.imread_remote(url)
        img_array = np.array(bytearray(image), dtype=np.uint8)
        return CV2Service.cvtColor(CV2Service.imdecode(img_array))

    def imread_local(self, url):
        return CV2Service.imread_local(url)
    def image2str(self, image):
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        nparr = np.fromstring(base64.b64decode(jpg_as_text), np.uint8)
        img2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return jpg_as_text
    def start_clustering(self, socket):
        self.mainFloor = self.imread(self.url)
        index = RugPerspectivePoint.find_point(self.backFloor)
        pts1, pts2 =  RugPerspectivePoint.obtain_perspective(index, self.backFloor)
        dst = RugPerspectivePoint.map_perspective(self.backFloor, self.mainFloor, pts1, pts2)
        image = CoverRug.covering(self.backFloor, dst)  
#        plt.imshow(image)
#        plt.show()
        socket.write_message(self.image2str(image))
    


