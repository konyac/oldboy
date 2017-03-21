#!/usr/bin/env python
# -*- coding:utf-8 -*-
#默认的输入会认定为字符串格式，怎样判断输入的是字符串，列表 元组呢,isinstance
def obj_len(args):
    if isinstance(args,str) or isinstance(args,list) or isinstance(args,tuple):
        if len(args)>5:
            return True
        else:
            return False
    else:
        return None
#
# inp = input("input:")
# print(inp)
# if len_5(inp):
#     print("大于5")
# else:
#     print("小于5")
#
# def func(*args):
#
#     print args
#
# # 执行方式一
# func(11,33,4,4454,5)
#
# # 执行方式二，传入列表
# li = [11,2,2,3,3,4,54]
# func(*li)
st="jkljkjlj"
lis=[11,22,33,44,55]
tup=(11,22,33,44,55,66)
print(obj_len(st),obj_len(lis),obj_len(tup))