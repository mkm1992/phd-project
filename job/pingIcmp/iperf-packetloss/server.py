import iperf3
import numpy as np
server = iperf3.Server()
server.bind_address = '10.10.10.1'
server.port = 6969
server.verbose = False
while True:
	server.run()