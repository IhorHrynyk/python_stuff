#! python
#coding: utf-8


def shortestLen (myString):
	
	words = myString.split()
	wordLen = len(myString)

	for word in words:
		if len(word) < wordLen:
			wordLen = len(word)

	return wordLen

myStr = input('type here:')
print('shortest length is', shortestLen(myStr))
