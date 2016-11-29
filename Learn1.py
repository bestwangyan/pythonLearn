#! /user/bin/python
# coding=utf-8
import sys
from sys import argv#一般不推荐这种方式,不易读,容易冲突
import myModule
print("Hello world")
print(u'Hello world\nHello China\n'u'我和我滴祖国,一刻也不能分开')
print("""This is the most exiting time in the history of your country
and even the most grandest hope seems in your reach""")

i = int(raw_input('Please enter a number:'))
s = str(raw_input('Please enter a string:'))
print("########### if else test ###########")
if i > 100:
    print('a big number')
elif i > 50:
    print('a normal number')
else:
    print('a small number')
print(str(i) + s)

print("########### while test ###########")
while i > 50:
    print("current value of i is :" + str(i))
    i -= 1
else:
    print('\n\n while test ended, and the value of i is :{0}'.format(str(i)))

print("########### for test ###########")
for i in range(0, 10):
    print("current value of i is :{0}".format(str(i)))


myModule.sayHi("Wang Yan")
print(myModule.MaxNumber(a=100,b=160))
print(myModule.sayHi.__doc__)
print(str(sys.argv)+" \n"+str(sys.path))
print(dir(myModule))


exec("print 'hello world'")
print(eval('3*3'))
a=100
assert a==100
a=99

