import tornado.web
import tornado.ioloop
import main
import config
import tornado.websocket

class AppHandler(tornado.web.RequestHandler):
	def get(self):
		self.finish("in get")


def make_app():
	return tornado.web.Application(main.make_handler(AppHandler))


if __name__ == "__main__":
	app = make_app()
	app.listen(config.PORT, address= config.HOST)
	print("app started in " + str(config.PORT))
	tornado.ioloop.IOLoop.current().start()

