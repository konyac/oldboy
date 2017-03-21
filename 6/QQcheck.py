#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree as ET #XML 模块

url="http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode="
qq=input("请输入QQ号：")
url+=qq
req = requests.get(url)
print(type(req))
res = req.text #获取get到的字符串

#解析xml格式内容
#xml接受一个参数：字符串，格式化为特殊的对象
node = ET.XML(res)
print(type(node))
print(node.text)
if node.text == "Y":
    print("在线")
elif node.text == "N":
    print("离线")
elif node.text == "V":
    print("隐身")

