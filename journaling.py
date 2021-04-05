#!/usr/bin/python2.7

import datetime

x = 0 

inp = raw_input("What's going on?")
now1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S: ")
inp = now1 + inp 

while x >= 0:
	fh=open("/link/to/your/desired/location", "a")
	fh.write(inp + '\n')
	fh.close()
	inp  = raw_input()





