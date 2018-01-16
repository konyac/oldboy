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
