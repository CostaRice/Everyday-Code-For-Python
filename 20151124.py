# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:27:05 2015
@author: hyc
"""

import math
pi = 0
for i in range(101,1000):
   if i % 17 == 0:
       pi+= 1
print pi
max = 10
sum = 0
extra = 0
     
for num in range(1, max):
   if num % 2 and not num % 3:
       sum += num
   else:
       extra += 1
     
print sum

