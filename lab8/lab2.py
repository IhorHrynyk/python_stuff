# python
# coding: utf-8

def insertionSort(a):
   for index in range(1,len(a)):

     currentvalue = a[index]
     position = index

     while position > 0 and a[position - 1] > currentvalue:
         a[position] = a[position - 1]
         position = position - 1

     a[position] = currentvalue

myList = [54,26,93,17,77,31,44,55,20]
insertionSort(myList)
print(myList)
