#!/usr/bin/env python
# -*- coding:utf-8 -*-
# class Foo(object):
#     def __init__(self):
#         self.name = 'wupeiqi'
#
#     def func(self):
#         return 'func'
# obj=Foo()
# print(hasattr(obj, 'name'))
# print(hasattr(obj, 'func'))
# a=getattr(obj,"name")
# print(a,type(a))
# import commons
DD=__import__("commons")
ret=DD.f1()
print(ret)
mod_name=input("请输入模块名：").strip()
print(mod_name,type(mod_name))
if hasattr(DD,mod_name):
    ret2=getattr(DD,mod_name)()
    print(ret2)
else:
    print("False")