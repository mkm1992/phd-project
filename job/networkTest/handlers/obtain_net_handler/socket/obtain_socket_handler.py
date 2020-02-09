import tornado.websocket
#from services.customRug.main_service import MainService
from services.obtainNet.main_service import MainService
import json

class Handler(tornado.websocket.WebSocketHandler):
	
	def check_origin(self, origin):
	    return True

	def open(self):
		print("socket open")

	def on_message(self, message):
		print(message)
		msg = json.loads(message)
		print(msg, "after convert to json", msg['url'])
		mainService = MainService(msg['url'], msg['type'])
		mainService.start_clustering(self)
		self.write_message("your request is processing")

	def on_close(self):
		print("socket closed")
