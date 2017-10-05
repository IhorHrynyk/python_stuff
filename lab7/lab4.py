#! python
#coding: utf-8

import sys

def codeIt (myString):
	
	charStr = list(myString)
	codedStr = []

	for char in charStr :
		if char == 'z':
			codedStr.extend('a')
		else:
			codedStr.extend(chr(ord(char) + 1))

	return ''.join(codedStr)


myStr = str(sys.argv[1])
print(codeIt(myStr))
