import json 
import os
	# the file to be converted 
class text2jsonService:
	def conversion():
		path1 = os.getcwd()
		filename = os.getcwd()+"/services/obtainNet/src2/tmp/test.txt" #os.path.join(path1,"src2\tmp\test.txt")
		dict1 = {} 
		with open(filename) as fh: 
			for line in fh: 
				command, description = line.strip().split(None, 1) 
				dict1[command] = description.strip() 
		out_file = open("test2.json", "w") 
		print('mojdeh hi')
		return dict1, out_file