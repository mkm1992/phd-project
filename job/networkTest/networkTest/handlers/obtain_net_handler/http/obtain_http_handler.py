import tornado.web


class Handler(tornado.web.RequestHandler):
	def prepare(self):
		print("in perpare")

	def get(self):
		url = self.get_argument('url')
		
