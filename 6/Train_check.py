#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree as ET

# 使用第三方模块requests发送HTTP请求，或者XML格式内容
url="http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode="
tr=input("请输入列车号：")
url=url+tr+"&UserID="
req = requests.get(url)
print(type(req))
res = req.text #获取get到的字符串

#解析XML格式内容，将字符串解析成xml
root=ET.XML(res)
for node in root.iter("TrainDetailInfo"):
    # print(node.tag,node.attrib)
    print(node.find("TrainStation").text,node.find("StartTime").text)