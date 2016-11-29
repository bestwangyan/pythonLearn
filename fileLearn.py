#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# Author:Wang Yan
# CreationDate:
import os

txt='''I love you more than I can say .
don't you know????
'''

f=file('test.txt','a')#读模式（'r'）、写模式（'w'）或追加模式（'a'）
f.write(txt)
f.close()

ff=file('test.txt')
while True:
    l=ff.readline()
    if l=='':
        break
    print(l)
ff.close()

os.rename(current_file_name, new_file_name) #文件重命名

os.remove(file_name) #删除文件

os.mkdir(newdir) #创建目录

os.chdir(newdir) #改变目录

os.getcwd() #获得当前路径

os.rmdir(dirname) #删除目录

