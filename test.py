# #! /usr/bin/python
# # coding=utf-8
# # FileName: *.py
# # Author:Wang Yan
# # CreationDate:
# from __future__ import division#就可以正常了
# dir(__builtins__)
# input()#raw_input之后进行eval()计算，只接受合法的python变量 例如字符串需要引号
# raw_input()#只以字符串类型接收输入
# range()#返回列表，生成真实的列表，
# xrange()#返回一个生成器，用多少返回多少，生成器是具有next方法的对象
# #xrange内存占用比较低，适合处理大数据量的数据。两者的用法是一样的。
# # python3中已经没有xrange函数，range函数使用了内存更节省的这种方式
# #如果在python3中需要range生成列表，只能显式调用 list(xrange(1,5))
# #生成器解析和列表解析
# [i for i in range(100) if i%3==0]#生成一个列表
# (i for i in range(100) if i%3==0)#生成一个生成器
# # http://www.regexr.com/ 正则表达式计算工具
# # http://deerchao.net/tutorials/regex/regex.htm 正则表达式30分钟教程
#
#
#

# # !/usr/bin/python
# # -*- coding: utf-8 -*-
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# chatbot = ChatBot("myBot")
# chatbot.set_trainer(ChatterBotCorpusTrainer)
#
# # 使用英文语料库训练它
# chatbot.train("chatterbot.corpus.chinese")
#
# # 开始对话
# while True:
#     print(chatbot.get_response(input(">")))

import requests,time,codecs
def pinyin2hanzi(pinyin="pinyin"):
    base_url = "https://olime.baidu.com/py"
    playload = {
        "input":pinyin,
        "inputtype":"py",
        "bg":0,
        "ed":1,
        "result":"hanzi",
        "resultcoding":"unicode",
        "ch_en":0,
        "clientinfo":"web",
        "version":1
    }
    json_data = requests.get(base_url,params=playload).json()
    print(json_data)
    return json_data["result"][0][0][0]

if __name__ == '__main__':
    print(__name__)
    while 1:
        try:
            print(pinyin2hanzi(raw_input("请输入拼音：")))
        except:
            print("exception")
            break