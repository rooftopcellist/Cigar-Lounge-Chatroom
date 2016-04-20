#!/usr/bin/python

class ConvLog(object):
	
	def __init__(self):
		self.data = []
		
	def add(self, s):
		self.data.append(s)
		
	def __str__(self):
		if len(self.data) == 0:
			return 'EMPTY.'
		else:
			return '\n'.join(self.data)
		