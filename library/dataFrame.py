#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909

#dataframe 是表格型数据结构，是共享同一个index的多列记录
import pandas as pd
import numpy as np
import datetime as dt

data=pd.DataFrame({'name':['wangyan','wangjia','wangjinbao'],'homeTown':['Hebei','Hubei','Fujian']})

print(data)
print (data['name'])
print(data.homeTown)
print(data.ix[2])
data.index.name='No.'
print(data)
# del data['name']
data.append(pd.Series(['apple','banana','peach'],name='fruite'),ignore_index=True)
print(data)
dates=pd.date_range('20150101',periods=7)
RandomData=pd.DataFrame(np.random.randn(7,3),index=dates,columns=['a','b','c'])
print(RandomData)