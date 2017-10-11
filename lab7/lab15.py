#! python
#coding: utf-8

import string
import random

length = random.randrange(8, 20)
password = []

for i in range(length):
	password.append(random.choice(string.ascii_letters))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
chars = ['_', '%', '*', '!', '?', '^', '#', '@', '|', '(', ')', '[', ']', '{', '}', '/']

password.insert(random.randrange(length - 1), str(nums[random.randrange(len(nums) - 1)]))
if random.randrange(length - 1) % 2 == 0:
	password.insert(random.randrange(length - 1), str(nums[random.randrange(len(nums) - 1)]))

password.insert(random.randrange(length - 1), chars[random.randrange(len(chars) - 1)])
if random.randrange(length - 1) % 2 == 0:
	password.insert(random.randrange(length - 1), chars[random.randrange(len(chars) - 1)])	

print(''.join(password))
