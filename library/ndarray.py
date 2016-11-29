#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
#import numpy
from numpy import *

aArray=array([(1,2,3),(4,5,6,7)])
print(aArray)
print(type(aArray))
print(zeros((4,5)))
print(array([arange(1,4),arange(4,7),arange(7,10)]))
aArray.sum()
print(arange(4))

def mul(x,y):
    return (x+1)*(y+1)

bArray=fromfunction(mul,(9,9))
print(bArray)
