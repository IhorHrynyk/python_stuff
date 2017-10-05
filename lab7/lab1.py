#! python
#coding: utf-8

import sys

myString = str(sys.argv[1])
k = int(sys.argv[2])

if k > len(myString):
	print('K is to long, sorry')
else:
	print(myString[k:] + myString[:k])
