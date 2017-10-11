#! python
#coding: utf-8

str1 = list(input('first:'))
str2 = list(input('second:'))

str1 = set(str1)
str2 = set(str2)

count = 0;
for char in str2:
	if char in str1:
		count = count + 1

if count <= len(str1):
	print(True)
else:
	print(False)
