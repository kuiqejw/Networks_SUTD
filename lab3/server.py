#!/usr/bin/python2

"""
Networks Lab 3: UDP Socket Programming

Server code.
"""

from socket import *
import sys
def run():
	count = 0
	try:
		while True:
			print('Wait to receive message')
			data, addrs = sock.recvfrom(4096)
			print("Data: {}".format(data))
			print("Addresses: {}".format(addrs))
			if data:
				segidarr = data.split(',')
				segid = segidarr[0]
				print('seg id' + segid + 'received')
				count += 1
	except timeout:
		print('No of packets received: ' + str(count))
	   
sock = socket(AF_INET, SOCK_DGRAM)
sock.settimeout(5)
sock.bind(('10.0.0.2', 5555))
while True:
	run()
