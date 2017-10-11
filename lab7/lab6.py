#! python
#coding: utf-8

def borderIt (myString):
	
	border = []
	i = 0;
	while i != len(myString):
		border.append('*')
		i = i + 1

	print (''.join(border))
	print ('*', myString, '*')
	print (''.join(border))
	
	

myStr = input('input string:')
borderIt(myStr)
