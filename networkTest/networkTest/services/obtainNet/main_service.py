# -*- coding: utf-8 -*-
from multiprocessing import Process
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
		start = time.time()
		p1 = Process(target = throughputService.CfunctionReciever())
		p1.start()
		p1.join(5)
		p2 = Process(dict1,out_file = text2jsonService.conversion())
		p2.start()
		if  p1.is_alive():
			p1.terminate()
		print("hiiii")
		serialized_data =json.dump(dict1, out_file, indent = 4) 
		print(dict1)
		socket.write_message(dict1)
        
