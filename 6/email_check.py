#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree as ET
url="http://ws.webxml.com.cn/WebServices/ValidateEmailWebService.asmx/ValidateEmailAddress?theEmail="
em=input("请输入邮箱：")
url+=em
req=requests.get(url)
res=req.text
nod=ET.XML(res)
print(nod.text)
