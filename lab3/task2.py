#! python
# coding: utf-8

t = input("you have fahrenheits or celsius? type 'f' or 'c' ")

if t == 'f':

	f = int(input("enter a temperature: "))
	c = (f - 32) * 5.0/9.0
	print ("temperature: ", f, " fahrenheit = ", c, " C")

elif t == 'c':

	c = int(input("enter a temperature: "))
	f = 9.0/5.0 * c + 32
	print ("temperature: ", c, " celsius = ", f, " fahrenheits")
