import tornado.web
from services.custom.custom_service import CustomService

class Handler(tornado.web.RequestHandler):
	def prepare(self):
		print("in perpare")

	def get(self):
		image = CustomService.carpetting_process(self.get_argument('url'))
		self.set_header("Content-type", "image/jpeg")
		self.write(image)
