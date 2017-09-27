#! python
#coding: utf-8

import decimal

salary = input('скільки вам платять? ')

tax = decimal.Decimal(salary) * decimal.Decimal('0.18') + \
	decimal.Decimal(salary) * decimal.Decimal('0.015') 

print('податок буде ', str(tax))
