import iperf3

def serverIperf():
	server = iperf3.Server()
	server.run()
serverIperf()