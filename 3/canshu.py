#!/usr/bin/env python
# -*- coding:utf-8 -*-
# def f1(a):
#     print(a,type(a))
# f1(1)
# f1("stringss")
# f1([11,11,22,33,44])

#动态参数1,参数类型为元组
# def fun1(*args):
#     print(args,type(args))
# fun1(123,"12jkj",{"k1":"hahah","k2":"hehheh"})
# #动态参数2，参数类型字典
# def fun2(**kwargs):
#     print(kwargs,type(kwargs))
# li={"k1":7878,"k2":222,"ad":11}
# fun2(**li)
# fun2(k1=123,k2="12jkj",k3={"k1":"hahah","k2":"hehheh"})
# #动态参数3，参数是两个都可以
# def fun3(*args,**kwargs):
#     print(args,type(args))
#     print(kwargs,type(kwargs))
# fun3(123,"kkk",k1=88,m2=33,n2="1111")

def fun4(**kwargs):
    print(kwargs,type(kwargs))
    # print(kwargs,type(kwargs))
li={"k1":34,"k2":11}
fun4(**li)


#全局变量一般以大写命名，局部变量以小写命名
#全局变量
p=234
def f1():
    #局部变量
    a=123
    p=999 #全局变量在内部被修改。只在内部起作用
    global p #应用到全局变量。
    print(p)
    print(a)
def f2():
    #局部变量
    a=456
    print(p)
    print(a)
f1()
f2()
