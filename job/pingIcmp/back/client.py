import iperf3

def clientIperf(ip):
	client = iperf3.Client()
	client.duration = 1
	client.server_hostname = ip
	client.port = 5201
	result = client.run()
	print(result)
	return result.sent_Mbps
result = clientIperf('localhost')
print(result)
