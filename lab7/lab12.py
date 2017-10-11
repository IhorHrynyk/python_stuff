#! python
#coding: utf-8

def makeNormSpaces (myString):
	
	myString = myString.split()
	words = []
	
	for word in myString:
		words.append(word.strip())

	return ' '.join(words)

myStr = input('type here:')
print(makeNormSpaces(myStr))
