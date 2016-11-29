#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:求素数
# Author:Wang Yan
# CreationDate:

import math as m
import cPickle as p
import datetime as dt

primeNumberList= [0,2,]

def searchPrimeNumber(endNumber):
    global primeNumberList
    for i in xrange(0, endNumber):
        for k in xrange(2, int(m.sqrt(i)) + 1):
            if i % k == 0 and i != k:
                break
            elif i%k !=0 and int(m.sqrt(i)) == k:
                primeNumberList.append(i)

    # return primeNumberList

endNumber=raw_input("Pls enter a number greater than zero ,\n\
and I will find all the prompt number less than the number\n\
Please enter:")
startTime=dt.datetime.now()
searchPrimeNumber(int(endNumber))
pfile=file('primeNumbers_'+endNumber+'B','w')
p.dump(primeNumberList,pfile,1)
pfile.close()
del primeNumberList
pfile=file('primeNumbers_'+endNumber+'B')
primeNumberList=p.load(pfile)
print(primeNumberList)
print(str(len(primeNumberList))+" elements has stored in {0} seconds".format(str((dt.datetime.now()-startTime).seconds)))
