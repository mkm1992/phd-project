import tornado.web
from services.carpetting.carpetting_service import CarpettingService

class Handler(tornado.web.RequestHandler):
	def prepare(self):
		print("in perpare")

	def get(self):
		image = CarpettingService.carpetting_process(self.get_argument('url'))
		self.set_header("Content-type", "image/jpeg")
		self.write(image)
