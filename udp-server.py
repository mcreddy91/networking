#!/usr/bin/python

# UDP server example
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", 54321))

print"started udp server on port 54321"

while 1:
	data, address = server_socket.recvfrom(256)
	print "( " ,address[0], " " , address[1] , " ) said : ", data
