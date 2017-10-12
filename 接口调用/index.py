#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# !/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib.parse import urlencode
from urllib import request


# ----------------------------------
# 12306火车票查询调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/22
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "4df98176fa229e7797b19166f347cd7b"

    # 1.站到站查询（含票价）
    request1(appkey, "GET")

    # 2.12306订票②：车次票价查询
    request2(appkey, "GET")

    # 3.车次查询
    request3(appkey, "GET")

    # 4.站到站查询
    request4(appkey, "GET")

    # 5.12306实时余票查询
    request5(appkey, "GET")

    # 6.12306订票①：查询车次
    request6(appkey, "GET")

    # 7.火车票代售点查询
    request7(appkey, "GET")

    # 8.列车站点列表
    request8(appkey, "GET")


# 站到站查询（含票价）
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/s2swithprice"
    params = {
        "start": "",  # 出发站
        "end": "",  # 终点站
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content=str(content,encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 12306订票②：车次票价查询
def request2(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/ticket.price.php"
    params = {
        "train_no": "",  # 列次编号，对应12306订票①：查询车次中返回的train_no
        "from_station_no": "",  # 出发站序号，对应12306订票①：查询车次中返回的from_station_no
        "to_station_no": "",  # 出发站序号，对应12306订票①：查询车次中返回的to_station_no
        "date": "",  # 默认当天，格式：2014-12-25
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 车次查询
def request3(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/s"
    params = {
        "name": "",  # 车次名称，如：G4
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 站到站查询
def request4(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/s2s"
    params = {
        "start": "",  # 出发站
        "end": "",  # 终点站
        "traintype": "",  # 列车类型，G-高速动车 K-快速 T-空调特快 D-动车组 Z-直达特快 Q-其他
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print( "request api error")


# 12306实时余票查询
def request5(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/yp"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json
        "from": "",  # 出发站,如：上海虹桥
        "to": "",  # 到达站,如：温州南
        "date": "",  # 出发日期，默认今日
        "tt": "",  # 车次类型，默认全部，如：G(高铁)、D(动车)、T(特快)、Z(直达)、K(快速)、Q(其他)

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 12306订票①：查询车次
def request6(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/ticket.cc.php"
    params = {
        "from": "",  # 出发站名称：如上海虹桥
        "to": "",  # 到达站名称：如温州南
        "date": "",  # 默认当天，格式：2014-07-11
        "tt": "",  # 车次类型，默认全部，如：G(高铁)、D(动车)、T(特快)、Z(直达)、K(快速)、Q(其他)
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 火车票代售点查询
def request7(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/dsd"
    params = {
        "province": "",  # 省份,如：浙江
        "city": "",  # 城市，如：温州
        "county": "",  # 区/县，如：鹿城区
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 列车站点列表
def request8(appkey, m="GET"):
    url = "http://apis.juhe.cn/train/station.list.php"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


if __name__ == '__main__':
    main()
