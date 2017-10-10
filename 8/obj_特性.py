#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 特性  @propety可以使用对象向访问字段一样访问这个方法。
class Foo:
    country = "zhongguo "  # 静态字段

    def __init__(self, name):
        self.name = name  # 普通字段
        # name = name     # 找不到

        # 将方法伪造成字段

    @property  # 特性。 可以当做字段让对象调用，调用时就不用加()
    def cat(self):  # 不能加参数，加了就报错
        temp = "%s sb" % self.name
        print(temp)
        return temp

    def show(self):
        print("show")


obj = Foo("LIUJIANZUO")
print(obj.name)
print(obj.cat)
