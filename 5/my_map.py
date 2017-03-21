#!/usr/bin/env python
# -*- coding:utf-8 -*-
def mymap(func, args):
    # func=>f1函数
    # args=>[11,22,33,44,55]
    result = []
    for i in args:
        result.append(func(i))  # func(11)=》f1(11)
    return result

def f1(x):
    return x + 100

r = mymap(f1, [11, 22, 33, 44, 55])
print(r)
