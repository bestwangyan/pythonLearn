#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# Author:Wang Yan
# CreationDate:20160907
Version = 1.0

# shoppingList=[]
# for i in range(0,50,5):
#     shoppingList.append(i)
#
# for i in shoppingList:
#     print(i)
#
# for i in range(0,len(shoppingList)):
#     print(shoppingList[i])
#
# # for i in range(0,len(shoppingList)):
# #     print(shoppingList.pop())
#
# print("there is {0} items in this list".format(len(shoppingList)))
# print(shoppingList.pop())
# shoppingList.sort(reverse=True)
# for i in shoppingList:
#     print(i)
# print(shoppingList)
#
# print("#元组内容不可修改,其他与list相同")
# zoo = ('wolf', 'elephant', 'penguin')
# print(zoo.index('elephant'))
# for i in zoo[0:-1]:
#     print(i)
#
# mydic={'name':"wangyan",
#        'sex':"male",
#        'birthday':19851230,
#        'zoo':('wolf','elephant','penguin')
#        }
#
# print(mydic)
# print(mydic['name'])
# mydic['email']="bestwangyan@qq.com"
# print(mydic['email'])
# # del mydic['sex']
# for i in mydic:
#     print(i+":"+str(mydic[i]))
#
# if mydic.has_key('sex'):
#     print(mydic['sex'])

# mydic={}.fromkeys(['wangyan','wangjia','wangjinbao'],'HNU')
#
# print(mydic)
# print(mydic.keys(),mydic.values(),mydic.viewitems())

# stuList=['wangyan','wangjia','wangjinbao']
# schoolList=['zq','hg','qz']
#
# stuSchoolDic=dict(zip(stuList,schoolList))
# print stuSchoolDic
# anotherDic={}
# for i in range(0,len(stuList)):
#     anotherDic[stuList[i]]=schoolList[i]
#
# print(anotherDic)

# for key,value in mydic:#不好用这个方法,对于复杂值接不到
#     print(key+":"+str(value))

# name='wangyan'
# print(name.find('y'))
# print(name.ljust(20,"#"))

# week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
# print week[0:5],'\n',week[-7:-2],'\n'
# week.sort()
# print(week)
# t=enumerate(week)
# for e in t:
#     print e
# print()

# str = "Hello world!"
# str2 = u"我爱你中国"
# print("Hello %8s %d,%4.3f,%%" % ("world", 2, 3.1415926))
# print(str.split(" "))
# print(str.istitle(), str.title())
# print(str2.title())

# numbers=[2,3.4,56.78,9,1.1,-3]
# print(sum(numbers)/len(numbers))
# numbers.reverse()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# numbers.sort(key=abs)
# print(numbers)

# numbers=[x for x in range(0,10)]
# print(numbers)
# numbers=[x**2 for x in range(0,10) if x**2<60]
# print(numbers)
# numbers=[(x,y) for x in range(0,2) for y in range(0,2)]
# print(numbers)
#
# myTuple=(1,2,7,3,3.3)
# print(myTuple)
# print(sum(myTuple))

# （1）序列类型函数
#
# enumerate(), reversed(), sorted(), zip()
#
# （2）字符串类型方法
#
# join(), strip(), replace(), split(), translate(),startswith()
#
# 其中translate()需要使用maketrans()方法：
#
# >>> z = str.maketrans(x,y) #in Python 2 from string import maketrans z = maketrans(x,y)
#
# （3）列表类型方法
#
# append(), count(), extend(), insert(), pop(), sort()

# import string
# x="Hello"
# y="World"
#
# z=string.maketrans(x,y)
# print(z)
#
# a=string.translate("Hello",z)
#
# print(a)
# print(x.startswith("H"),y.startswith("H"))

# dict.get() 如果存在的话返回value,如果不存在的话返回none
# dict.update()
# alinfo={"mayun":1000,"lihao":700}
# naliinfo={"lihao":800,"xiaozheng":700}
# alinfo.update(naliinfo)
# print(alinfo)
# naliinfo.clear()#会将引用的也删除掉
# print naliinfo

# aset=set(["mayun","mayun","liyanhong"])
# fset=frozenset(["mahuateng","liyanhong"])
# print aset,'\n',fset
# print aset&fset
# print aset|fset
# print aset-fset
# print aset^fset
#
# 集合运算