#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# Author:Wang Yan
# CreationDate:20160908
version=1.0

print("########### function test ###########")


def sayHi(pName):
    # type: (str) -> pName
    """

    :rtype: null
    """
    print("hi {0}".format(pName))

i=0
def MaxNumber(a, b):
    global i
    print(i)
    pass
    if a > b:
        return a
    else:
        return b

# python参数
# 位置或者关键字参数
# 可变长的位置参数 *argst    tuple
# 可变长的关键字参数 **argsd dict