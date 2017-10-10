#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @特性方法名.setter   设置 方法的返回值

class Foo:
    country = "zhongguo "

    def __init__(self, name):
        self.name = name  # 普通字段
        # name = name     # 找不到

    @property  # 特性。 可以当做字段让对象调用
    def cat(self):
        temp = "%s sb" % self.name
        print(temp)
        return(temp)


    @cat.setter  # 这个cat函数用来设置值的。
    def cat(self, value):
        self.name = value #重新设置self.name
        print(value)


    def show(self):
        print("show")


obj = Foo("LIUJIANZUO")
ret = obj.cat #第一次调用
print(ret) #输出返回值
obj.cat = "new_name"#修改返回值
ret=obj.cat #第二次调用
print(ret) #再次输出返回值
# 特性 property 和 property setter 可以控制向访问普通字段一样访问 方法