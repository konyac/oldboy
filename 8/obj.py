#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 　打印self的内存地址

class Oldboy(object):
    def fecht(self, backend):
        print(backend, self)

    def add_record(self, backend, record):
        pass


"""
self: 对象名
    调用方法的时候，python默认会把对象实例 赋值个self传入 方法
"""
obj1 = Oldboy()
print("obj1:", obj1)  # obj1: <__main__.Oldboy object at 0x0000000000B41400>
obj1.fecht("bbbbackend")  # bbbbackend <__main__.Oldboy object at 0x0000000000B41400>

# 　打印self的内存地址
