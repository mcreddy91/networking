#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
i=0

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   while (i <5):
    print i,' Got connection from', addr
    l=str(i)
    print l
    c.send('Thank you for connecting\n')
    i=i+1
   c.close()                # Close the connection
