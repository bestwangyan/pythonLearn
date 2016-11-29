#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
from pylab import *
from scipy.cluster.vq import *
import numpy as np

list1=[88.0,77.0,96.0,85.0]
list2=[92.0,99.0,95.0,94.0]
list3=[91.0,87.0,99.0,95.0]
list4=[78.0,99.0,97.0,81.0]
list5=[88.0,78.0,98.0,84.0]
list6=[100.0,95.0,100.0,92.0]

data=vstack((list1,list2,list3,list4,list5,list6))
centroids,variance=kmeans(data,2)
print('聚类中心:'+str(centroids))
print(variance)
result,var2=vq(data,centroids)
print(result)
print(var2)