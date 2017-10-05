#! python
#coding: utf-8

import sys

myString = str(sys.argv[1])

i = 0

for char in myString :
	if char in ['a', 'o', 'u', 'i', 'e', 'y'] :
		i += 1

print(i)
