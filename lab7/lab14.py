#! python
#coding: utf-8

import re

email = input('email address:')

if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
	print(False)
else:
	print(True)
	