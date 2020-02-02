import iperf3
client = iperf3.Client()
client.bind_address = '10.10.10.2'
client.server_hostname = '10.10.10.1'
client.port = 6969
client.blksize = 1234
client.num_streams = 10
client.zerocopy = True
client.verbose = False
client.reverse = True
client.protocol = 'udp'
result = client.run()
print(result.lost_packets)
print(result.lost_percent)