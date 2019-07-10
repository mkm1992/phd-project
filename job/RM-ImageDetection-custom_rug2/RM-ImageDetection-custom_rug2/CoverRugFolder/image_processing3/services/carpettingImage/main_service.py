from services.carpettingImage.cv2_service import CV2Service
from services.carpettingImage.filling_service import FloorFillService
import base64
import io
import numpy as np
import cv2
from matplotlib import pyplot as plt
from imageio import imread
###############
class MainService():
	def __init__(self, url, type, carpType):
		self.url = url
		self.type = type
		self.read_back_floor()
		self.carpType = carpType
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
	def start_filling(self, socket):
		self.mainFloor = self.imread(self.url)
		extended_carpet = CV2Service.carpet_extend(self.mainFloor, self.carpType)
		perspective_carpet = self.perspective_maker(extended_carpet)
		if self.type ==1:
			image = FloorFillService.fill1(perspective_carpet, self.backFloor)
		else:
			image = FloorFillService.fill2(perspective_carpet, self.backFloor)
		
		socket.write_message(self.image2str(image))

	def perspective_maker(self, extended_carpet):
		if self.type == 1:
			return CV2Service.perspective_maker1(extended_carpet)
		else:
			return CV2Service.perspective_maker2(extended_carpet)		
	def read_back_floor(self):
		if self.type == 1:
			self.backFloor = self.imread_local("./public/floor/img.png")
		else:
			self.backFloor = self.imread_local("./public/floor/img1.png")
