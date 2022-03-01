#<server hostname> <server port> <time>


import sys
import socket
from mininet.cli import CLI
import time
# from mininet.net import Mininet
# from mininet.link import TCLink
# from mininet.topo import Topo


if __name__ == "__main__":
	if len(sys.argv) != 4:
		print('Error: missing or additional arguments')
	server_hostname = sys.argv[1]
	server_port = sys.argv[2]
	execution_time = sys.argv[3]
	if server_port < 1024 or server_port > 656535:
		print('Error: port number must be in the range 1024 to 65535')
		sys.exit()
# Iperfer must establish a TCP connection with the server and
# send data as quickly as possible for time seconds. Data should be
# sent in chunks of 1000 bytes and the data should be all zeros.
# Keep a running total of the number of bytes sent.
	server_address = (server_hostname, server_port)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(server_address)
	data = b"0" * 1000
	bytes_sent = 0
	timeout = time.time() + execution_time
	while True:
		if time.time() > timeout:
			break
		client_socket.send(data)
		bytes_sent += 1000
	client_socket.close()

  
