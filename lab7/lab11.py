#! python
#coding: utf-8

def sortByLen (myString):
	
	return sorted(myString.split(), key=lambda x: len(x))

myStr = input('type here:')
print(sortByLen(myStr))
