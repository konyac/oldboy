#!/usr/bin/env python
# -*- coding:utf-8 -*-
#定义函数统计一个字符串中大写字母、小写字母、数字的个数，并返回结果
def func(str):
    ret=[0,0,0]
    for i in str:
        if i.isupper():
            ret[0]+=1
        elif i.islower():
            ret[1]+=1
        elif i.isdigit():
            ret[2]+=1
        else:
            pass
    return ret
# print(func("A1B2C3a4b5c"))
