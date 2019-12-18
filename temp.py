#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# # 动态参数，参数转成元组
# def func(*args):
#
#     print (args)
#
#
# # 执行方式一
# func(11,33,4,4454,5)
#
# # 执行方式二
# li = [11,2,2,3,3,4,54]
# func(*li)
#
# # 动态参数
"""
装饰器
def outer(func):
    def inner():
        print("123")
        r=func()
        print("456")
        return r
    return inner

@outer
def index():
    print(1)
    return 111

a=index()
print(a)
"""


# lis = {"islogin":None,"user":[{"11":1234,"2222":22222,"33333":333333},{"11":1234,"2222":22222,"33333":333333},{"11":1234,"2222":22222,"33333":333333}]}
# for i in lis.get("user"):
#     print(i["2222"])\
#
# '''
# md5加密
# import hashlib
# obj = hashlib.md5()
# obj.update(bytes("jdsalfkjalsfj",encoding="utf-8"))
# print(obj.hexdigest())
# '''
#
# class Father:
#     def __init__(self):
#         self.gz()
#     def gz(self):
#         print("father gz")
#
# class Son(Father):
#     def gz(self):
#         print("son gz")

#!/usr/bin/env python
# -*- coding:utf8 -*-
import re   #第一步，要引入re模块
#也就是分组匹配，()里面的为一个组也可以理解成一个整体
a = re.search("a(\d+)", "a466666664a4a4a4dg4g654gb")    #匹配 (a) (\d0-9的数字) (+可以是1个到多个0-9的数字)
b = a.group()
print(a.groups())
print(b)
#打印出 a466666664