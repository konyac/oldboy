#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

#json.loads 练习，将形似python数据类型列表或字典的字符串转换成 列表或者字典
# # s = "{'data':'invilad','status':'1000'}"  # json 认为里面必须是双引号才会处理，否则会报错，这样会报错
# s1='{"data":"invilad","status":"1000"}' # json 认为里面必须是双引号才会处理，否则会报错，不会报错
# s2="""{"data":"invilad","status":"1000"}""" # json 认为里面必须是双引号才会处理，否则会报错，不会报错
# l = "[1,2,3]"
# # ret = json.loads(s)  # loads 将形似python数据类型列表或字典的字符串转换成 列表或者字典
# ret2=json.loads(s1)
# ret3=json.loads(s2)
# # print(ret, type(ret))
# print(ret2,type(ret2))
# print(ret3,type(ret3))


#dumps 方法  将python数据类型列表或字典转换成形似列表或者字典的字符串
# n = {'status': '1000', 'data': 'invilad'}
# m = [1, 2, 3]
# ret1 = json.dumps(n)  # dumps 将python数据类型列表或字典转换成形似列表或者字典的字符串
# print(ret1,type(ret1))  # {"data": "invilad", "status": "1000"} <class 'str'>
# ret1 = json.dumps(m)
# print(ret1,type(ret1)) # [1, 2, 3] <class 'str'>

#dump 和load 的用法
# n = {'status': '1000', 'data': 'invilad'}
# m = [1, 2, 3]
# # json.dump(n,open("json_test",'w'))# dump 功能就是 先转换为字符串，再写入文件
# r = json.load(open("json_test",'r'))# load 功能就是 读取文件字符串 并转化为python数据类型
# print(r,type(r))


