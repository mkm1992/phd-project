# -*- coding: utf-8 -*-

import json
import numpy as np
import time
import os
from services.obtainNet.throughput_service import throughputService
from services.obtainNet.text2json_service import text2jsonService
class MainService:
	def __init__(self, url, type):
		self.url = url
		self.type = int(type)
	def start_clustering(self, socket):
		throughputService.CfunctionReciever()
		dict1,out_file = text2jsonService.conversion()
		print("hiiii")
		serialized_data =json.dump(dict1, out_file, indent = 4) 
		print(dict1)
		socket.write_message(dict1)
        
