#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 通过类访问有：静态字段
# 通过对象访问有：普通字段、类的方法。
# 谁的东西谁访问
class Foo:
    country = "zhongguo "  # 静态字段，类中
    def __init__(self, name):
        self.name = name  # 普通字段，对象中
        # name = name     # 找不到
    def show(self):
        print("show")

# 获取静态字段
print(Foo.country)  ## 规范：1、谁里面的东西谁自己访问，2、除了类中的方法

obj = Foo("liujianzuo")
x = hasattr(obj, "name")  # 判断对象中的name字段值

y = hasattr(obj, "show")
print(x, y)

