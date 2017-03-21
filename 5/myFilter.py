#!/usr/bin/env python
# -*- coding:utf-8 -*-

def myfilter(func, args):
    #func，函数名，func=func_t
    result = []
    for i in args:
        if func(i):#执行接收的函数，并获取返回值
            result.append(i)
    return result

def func_t(x):
    if x > 22:
        return True
    else:
        return False

r = myfilter(func_t, [11, 22, 33, 44, 55])
print(r)
