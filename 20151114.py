# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:23:36 2015

@author: hyc
"""

n = int(raw_input('Please enter an integer:'))
if n > 0:
    print 'U entered an positive number'
elif n == 0:
    print 'U entered zero'
elif n < 0:
    print 'U entered an negative number'
else :
    print 'Wrong enter'
