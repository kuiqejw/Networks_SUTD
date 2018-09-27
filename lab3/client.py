#!/usr/bin/python2

"""
Networks Lab 3: UDP Socket Programming

Client code.
"""

from socket import *
import argparse
import time
import sys

if __name__=="__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-r', type=float, dest='rate',
		help='Packet rate in Mbps (eg; -r 1.5 is 1.5 Mbps)')

	args = parser.parse_args()

	if args.rate == None:
		print("USAGE:")
        	print("python2 client.py -r 3.0:")
	else:
	        print("Client rate is {} Mbps.".format(args.rate))
	        sock = socket(AF_INET, SOCK_DGRAM)
	        server_address = ('10.0.0.2', 5555)
	        message = '1'
		count = 0
		try:
			while(count <=5):
				sock.sendto(str(count) + "," + message*int(float(args.rate)*25000), server_address)
				count += 1
		finally:
			time.sleep(1)
			print >>sys.stderr, 'closing socket'
		sock.close()


