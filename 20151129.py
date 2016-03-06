# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:51:38 2015

@author: hyc
"""

class Employee:
    '所有员工的基类'
    empCount = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
        
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
        
    def dispayEmployee(self):
        print "Name:",self.name, "   Salary:",self.salary

emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",5000)
emp1.dispayEmployee()
emp2.dispayEmployee()
print "Total Employee %d" %Employee.empCount