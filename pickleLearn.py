#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# Author:Wang Yan
# CreationDate:
import cPickle as p

testList = ['you', 'me', 'him', 'her']

pFile = file('pFile', 'w')
p.dump(testList, pFile, protocol=0)  # 0文本模式 1 二进制模式
pFile.close()

del testList

pFile = file('pFile')
backList = p.load(pFile)

print(backList)
