import tornado.web
from services.cover.cover_service import CoverService

class Handler(tornado.web.RequestHandler):
	def prepare(self):
		print("in perpare")

	def get(self):
		image = CoverService.cover_process(self.get_argument('url'))
		self.set_header("Content-type", "image/jpeg")
		self.write(image)
