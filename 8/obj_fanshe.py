#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 反射 对象 类的两种
class Do:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("show")


obj = Do("kakaka")
# 反射 传入类的时候，只能找到类的成员
# r = hasattr(Do, "show")  # True
r = hasattr(Do, "name")#nane是对象的普通字段，不是类的因此类没有
print(r)
print(Do.__dict__)

# 反射传入对象 ，可以通过类对象指针找到类的方法 既可以找到对象的属性 也可以通过对象找到类中的方法，因为有类对象指针
x = hasattr(obj, "name")
print(x)
print(obj.__dict__)
y = hasattr(obj, "show")
print(y)