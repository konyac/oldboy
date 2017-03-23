#!/usr/bin/env python
# -*- coding:utf-8 -*-
class C:

    __name = "公有静态字段"

    def func(self):
        print(C.__name)

class D(C):

    def show(self):
        print(C.__name)


print(C.__name)       # 类访问            ==> 报错误

obj = C()
obj.func()     # 类内部可以访问     ==> 正确

obj_son = D()
obj_son.show() # 派生类中可以访问   ==> 报错误

 # 私有静态字段