#! python
#coding: utf-8

import math

inputData = list(map(float, input('давайте писати дані: ').split()))

x = inputData[0]
u = inputData[1]
b = inputData[2]

f = (1 / (b * math.sqrt(2 * math.pi))) * math.exp(-(((x - u) ** 2) / (2 * b ** 2)))

print(str(f))
