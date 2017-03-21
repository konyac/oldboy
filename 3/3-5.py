#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

# def fun(args):
#     if len(args)>2:
#             ret=args[0:2]
#             return ret
#     else:
#         return args
#     # return args 也可以不写else直接这样写
# inp=[11,22,33,44,55]
# print fun(inp)

def fun2(args):
    if len(args)>2:
        del args[2:]
li=[11,22,33,444,55]
fun2(li)
print(li)

