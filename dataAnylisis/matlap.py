#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
#a股的可以用 TuShare
from matplotlib.finance import _quotes_historical_yahoo
from matplotlib import pyplot as plt
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
    dateFormat=datetime.datetime.strftime(dateNormal,'%m%d')
    datelist.append(dateFormat)


fields=['date','open','close','high','low','volume']
quoteDf1=pd.DataFrame(quotes,columns=fields,index=range(1,len(quotes)+1))
quoteDf2=pd.DataFrame(quotes,columns=fields,index=datelist)
quoteDf2=quoteDf2.drop(['date'],axis=1)
quoteDf3=quoteDf2[-5:]

print(quoteDf3)

plt.title("Baidu stock price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.subplot(311)
plt.plot(quoteDf1.index,quoteDf1.close,'rD')
plt.subplot(312)
plt.plot(quoteDf1.index,quoteDf1.close)
plt.subplot(313)
plt.bar(quoteDf1.index,quoteDf1.close)
plt.show()
quoteDf3.to_excel("/home/king/Baidu.xls",sheet_name="Baidu")