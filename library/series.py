#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
#Series 由数据和索引组成 一维数据
from pandas import Series

aSer=Series([1,2.0,'a']) #series 自带索引
print(aSer)
type(aSer)
bser=Series(['apple','banana','peach'],index=['a','b','c'])
print(bser)
print(bser.index)
print(bser.values)
print(bser.count())
aSer.name='key-value'
aSer.index.name='key'
print(aSer)#本身和索引都具有name属性

adic={'a':'apple','b':'banana','c':'peach'}
aIndex=['a','c','d']
aaser=Series(adic,index=aIndex)#数据对齐
print(aaser)
print(aaser.isnull())
