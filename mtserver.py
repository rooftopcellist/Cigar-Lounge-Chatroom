"""
Program: Cigar Lounge Chatroom
Author: Christian Adams
This program is a multithreaded chatroom server.  It allows you to connect from multiple 'mtclient.py' programs.  It is also possible to connect from a different computer using an mtclient.py program, but the host would have to be manually changed.  

One downside to this program is that it must print the whole log each time, which gets costly for long conversations. Note: make a GUI that shows the conversation log and have each client append each message as it comes in and have the server only send one message at a time.   
"""

#!/usr/bin/python
from socket import *
from time import ctime
from threading import Thread
from convLog import ConvLog


class ClientHandler(Thread):
	#Manages client requests
	def __init__(self, client, record):
		Thread.__init__(self, name = "")
		self._client = client
		self._record = record
		
		
	def run(self):
		self._client.send(ctime() + '\nWelcome to the Cigar Lounge.')
		self._name = self._client.recv(BUFSIZE)
		self._client.send(str(self._record))
		while True:
			message = self._client.recv(BUFSIZE)
			if not message:
				print "Client Disconnected"
				self._client.close()
				break
			else:
				message = self._name + ' ' + ctime() + '\n' + message
				self._record.add(message)
				self._client.send(str(self._record))



HOST = 'localhost'
PORT = 1234
ADDRESS = (HOST, PORT)
BUFSIZE = 1024

record = ConvLog()
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDRESS)
s.listen(5)

while True:
	print 'Waiting for connection...'
	client, address = s.accept()
	print'... accepted connection from:', address
	handler = ClientHandler(client, record)
	handler.start()
	

