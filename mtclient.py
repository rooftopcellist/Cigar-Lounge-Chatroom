#!/usr/bin/python

from socket import *

HOST = 'localhost'
PORT = 1234
BUFSIZE = (1024)
ADDRESS = (HOST, PORT)


s = socket(AF_INET, SOCK_STREAM)   # Specifies the family and type of connection (TCP) of the socket & assigns it to 's'
s.connect(ADDRESS)          		# Connections to Server through port 1234 on the localhost (127.0.0.1)

print s.recv(BUFSIZE)			#prints server's greeting
name = raw_input('Enter your name: ')
s.send(name)

while True:
	record = s.recv(BUFSIZE)
	if not record:
		print 'Server disconnected'
		break
	print record
	message = raw_input('You: ')
	if not message:
		print 'Server disconnected'
		break
	s.send(message + '\n')
s.close()

