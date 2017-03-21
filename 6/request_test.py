#!/usr/bin/env python
# -*- coding:utf-8 -*-
#我们接收的网页请求过来是字符串或者字节
#
# from urllib import request
#
# f = request.urlopen("http://www.cnblogs.com/") #获取网站内容，作为对象
# # f = request.urlopen("http://yujuanfudan.blog.163.com/")
# ret = f.read() #对象的read方法读出来，和文件类型
# print(type(ret)) #初始时bytes类型
# print(str(ret, encoding="utf-8")) #转成字符串类型

# import urllib.request
#
# #发送get请求
# # f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
# # result = f.read().decode('utf-8')
# # print(result)
#
# #发送携带请求头的GET请求
# req = urllib.request.Request('http://www.example.com/')
# req.add_header('Referer', 'http://www.python.org/')
# r = urllib.request.urlopen(req)
#
# result = f.read().decode('utf-8')

import requests,json
res=requests.get("http://www.weather.com.cn/adat/sk/101010500.html")
res.encoding="utf-8"
result=res.text #通过text拿到一个字符串
print(result,type(result))
dic=json.loads(result) #通过json.loads转化成字典
print(dic,type(dic))
