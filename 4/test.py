#!/usr/bin/env python
# -*- coding:utf-8 -*-
#函数传参，传引用
# def func(args):
#     args.append(123)
# li=[11,22]
# func(li)
# print li

def func2(args):
    args=123
li=[11,22,33]
func2(li)
print(li)
