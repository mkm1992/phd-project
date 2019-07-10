import tornado.websocket
from services.carpettingImage.main_service import MainService
import json

class Handler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("socket open")
    def check_origin(self, origin):
        return True
    def on_message(self, message):
        print(message)
        msg = json.loads(message)
        print(msg, "after convert to json", msg['url'])
        mainService = MainService(msg['url'], msg['type'],  msg['carpType'])
        mainService.start_filling(self)
        #self.write_message("your request is processing")

    def on_close(self):
        print("socket closed")
