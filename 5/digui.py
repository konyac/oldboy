#!/usr/bin/env python
# -*- coding:utf-8 -*-
def func(a1, a2):
    if a1 > 1000:
        return a1
    # print(a1, a2)
    a3 = a1 + a2
    return func(a2, a3)
ret = func(0, 1)
print(ret)
# def func(arg1, arg2):
#     if arg1 == 0:
#         print(arg1, arg2)
#     arg3 = arg1 + arg2
#     print(arg3)
#     func(arg2, arg3)
#
#
# func(0, 1)
