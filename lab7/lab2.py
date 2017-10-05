#! python
#coding: utf-8

import sys

def isPalindrom (myString):
	
#	print(myString)

	myString = myString.lower()
	myString = myString.replace(" ", "")
	myString = myString.replace(",", "")
	myString = myString.replace("'", "")
	myString = myString.replace(".", "")

#	print(myString)	

	if myString == myString[::-1]:
		return True
	else:
	 	return False


myStr = str(sys.argv[1])
print(isPalindrom(myStr))
