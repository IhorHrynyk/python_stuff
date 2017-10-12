# python
# coding: utf-8

def average (a):
	return sum(a) / len(a)

def mediana (a):
	
	a = sorted(a)
	print(a)

	if len(a) % 2 == 0:
		return (a[int( len(a) / 2) - 1] + a[int( len(a) / 2)]) / 2
	else:
		return a[int( len(a) / 2)]	 


myList = [1, 4, 5, 4, 1, 4, 8, 1, 7]
print(average(myList))
print(mediana(myList))
