#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909

import csv,requests,time,sys,os

PHONE_ATTR_JUHE = """http://apis.juhe.cn/mobile/get?phone={phone}&dtype=&key={key}"""
PHONE_ATTR_360 = """http://cx.shouji.360.cn/phonearea.php?number={phone}"""


def get_number_attribution_360(phone):
    """360查询号码归属地"""
    try:
        r = requests.get(PHONE_ATTR_360.format(phone=phone))
        result = r.json()
        # print result

        province = result.get("data").get("province")

        if not province:
            province = "null"
            city = "null"
        else:
            if province in (u"北京", u"天津", u"上海", u"重庆"):
                city = province
            else:
                city = result.get("data").get("city")

        print phone+','+province+','+city
    except:
        time.sleep(5)
        get_number_attribution_360(phone)

if __name__ == "__main__":
    print sys.argv
    if (len(sys.argv)>1):
        filename=sys.argv[1]
    else:
        filename="1127.csv"
    if os.path.exists(str(filename)):
        csvfile=file(str(filename),'r')
        reader=csv.reader(csvfile)
        lineNumber=0
        locationInfo=''
        for line in reader:
            lineNumber=lineNumber+1
            if lineNumber!=1:
                get_number_attribution_360(phone=line[0])
            else:
                print (u"电话，省，市")
        csvfile.close()
    else:
        get_number_attribution_360(phone=filename)
    c = raw_input("enter to end")