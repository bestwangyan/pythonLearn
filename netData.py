#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
import urllib
web=urllib.urlopen(r'http://www.baidu.com')
html=web.read()
print(html)