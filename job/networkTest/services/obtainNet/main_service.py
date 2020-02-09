# -*- coding: utf-8 -*-

import json
import numpy as np
import time
import os


class MainService:
	def __init__(self, url, type):
		self.url = url
		self.type = int(type)
		#self.thresh = int(thresh)
	def start_clustering(self, socket):
		str1 = "ping "+self.url;   
		f = os.popen(str1)
		now = f.read()
		print(now)
		print(type(now))
		# with open("Output.txt", "w") as text_file:
		#     text_file.write(now)
		#################################################
		a =2;
		serialized_data = json.dumps({"throughput": a})
		socket.write_message(serialized_data)
        
