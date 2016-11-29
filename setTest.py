#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909

import numpy as n

aset=set('sunrise')
bset=set('sunset')

print("&:"+str(aset&bset))
print("|:"+str(aset|bset))
print("-:"+str(aset-bset))
print("^:"+str(aset^bset))
#集合可以进行各种运算
aset-=set('sun')
print(aset)
#集合可以进行比较(< > = !=  in \not in )
print(aset not in bset)
print(set('sun') < bset)
print(aset != bset)

#集合有很多内建函数可以使用

aset.discard('S') #删除一个元素，如果不存在，do nothing
bset.remove("S") #删除一个元素，如果不存在，报错