#! python
#coding: utf-8

import math

inputData = list(map(float, input('треба два невідємні числа: ').split()))

a = inputData[0]
b = inputData[1]

if (a < 0) | (b <= 0):
	print ('дані не такі')
	exit()
else:
	x = (math.sqrt(a * b)) / (math.exp(a) * b) + (a * math.exp((2 * a) / b))
	print(str(x))
	