# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:21:30 2015

@author: hyc
"""
num= int(raw_input("Please enter an integer: "))
if num < 0:
    isNeg = True
    num  =abs(num)
else:
    isNeg = False
result =''
if num ==0:
    result = '0'
while num > 2:
    result = str(num%2) + result
    num =num/2
if isNeg:
    result = '-'+result
    