#!/usr/bin/python
# UDP client 

import socket
cnt=1
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
	data = raw_input("Type something(q or Q to exit): ")
	if (data <> 'q' and data <> 'Q'):
		while (cnt <10):
			client_socket.sendto(data, ("localhost",54321))
			cnt=cnt+1
		cnt=1
	else:
		break
client_socket.close()
