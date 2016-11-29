#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
#a股的可以用 TuShare
from matplotlib.finance import _quotes_historical_yahoo
#from datetime import date
import datetime
import pandas as pd
import numpy as np
today=datetime.date.today()
start=(today.year-1,today.month,today.day)
quotes=_quotes_historical_yahoo('BIDU',start,today)
datelist=[]
for i in range(0,len(quotes)):
    dateNormal=datetime.date.fromordinal(int(quotes[i][0]))
    dateFormat=datetime.datetime.strftime(dateNormal,'%Y%m%d')
    datelist.append(dateFormat)


fields=['date','open','close','high','low','volume']
quoteDf1=pd.DataFrame(quotes,columns=fields,index=range(1,len(quotes)+1))
quoteDf2=pd.DataFrame(quotes,columns=fields,index=datelist)
quoteDf2=quoteDf2.drop(['date'],axis=1)
#print(quoteDf2['open'])
#print(df)
print(quoteDf2)
print(quoteDf2.index)
print(quoteDf2.columns)
print(quoteDf2.values)
print(quoteDf2.describe)
print(quoteDf2.sort)
print(quoteDf2.head(10))
print(quoteDf2.tail(10))
print(quoteDf2[u'20161011':u'20161015'])
print(quoteDf2['open'])
print(quoteDf2.close)
print(quoteDf2.loc[:,['open','close']])
print(quoteDf2.loc[u'20161011':u'20161015',])
print(quoteDf2.loc[u'20161011':u'20161015',['open','close']])
print(quoteDf2.loc[u'20161011':u'20161011',['open']])
print(quoteDf2.at[u'20161011','open'])
print(quoteDf2.iloc[-5:,[0,1,3]])
print(quoteDf2.iloc[-1,1])
print(quoteDf2.iloc[-1,1])
print(quoteDf2[(quoteDf2.index>=u'20161001')&(quoteDf2.close>180)])
print(len(quoteDf2))
print(quoteDf2[(quoteDf2.index>=u'20161001')&(quoteDf2.close>165)])
print(quoteDf2.close.mean())
print(quoteDf2[(quoteDf2.close>180)&(quoteDf2.index>=u'20161001')].open)
#print(pd.DataFrame(quoteDf2[(quoteDf2.index>=u'20161001')&(quoteDf2.close>165)]).mean(columns="volume"))

status=np.sign(np.diff(quoteDf2.close))
print(status)
print(status[np.where(status==1)].size)
print(status.mean())
print(quoteDf2.sort(columns="close"))
print(quoteDf2[(quoteDf2.close>180)&(quoteDf2.index>=u'20161001')].sort_index(axis=0,ascending=False))
print(quoteDf2[(quoteDf2.close>180)&(quoteDf2.index>=u'20161001')].sort_values(by=["close","open"],ascending=False))

monthTemp=[]
yearTemp=[]
for i in range(len(quoteDf2)):
    monthTemp.append(datetime.datetime.strptime(quoteDf2.index[i],"%Y%m%d").month)
    yearTemp.append(datetime.datetime.strptime(quoteDf2.index[i], "%Y%m%d").year)

quoteDf2['month']=monthTemp
quoteDf2['year']=yearTemp
print(quoteDf2.month.value_counts())
print(quoteDf2["month"].value_counts())
#print quoteDf2.groupby("month").count().close
#print quoteDf2.groupby("month").sum().volume
#print(quoteDf2.groupby("month").mean().close)  #mean sum max min
g=quoteDf2.groupby("month")
print(g.volume.sum())