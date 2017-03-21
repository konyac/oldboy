#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#简单的继承
class Animals(object):
    def eat(self):
        print(self.name+" 吃")
    def drnik(self):
        print(self.name+" 喝")
class cat(Animals):
    def __init__(self,name):
        self.name = name
    def jiao(self):
        print(self.name + " miaomiao")
class dog(Animals):
    def __init__(self,name):
        self.name = name
    def jiao(self):
        print(self.name + " wangwang")
o1 = cat("cui")
o1.eat()
o1.drnik()
o1.jiao()
"""
"""
#派生类中有的功能 基类中也有 ： 优先执行派生类中的方法。  即从上到下
class Animals:

    def chi(self):
        print("chi")

    def he(self):
        print("he")

    def piao(self):
        print("%s 票 小泽玛利亚" % self.Name)

class Cat(Animals):
    def __init__(self,name):
        self.Name = name

    def jiao(self):
        print("%s 叫"%(self.Name))

    def piao(self):
        print("%s 票 苍井空" % self.Name)

class Dog(Animals):
    def __init__(self,name):
        self.Name = name

    def jiao(self):
        print("%s 叫"%(self.Name))


mao1 = Cat("小花")
mao1.piao()
"""
"""
# 多继承，1 从左到右去匹配，匹配到就不向右匹配了，  2 派生类中有的就不用了
class Animals:

    def chi(self):
        print("chi")

    def he(self):
        print("he")

    def piao(self):
        print("%s 票 小泽玛利亚" % self.Name)

class Dog_F():
    def __init__(self,name):
        self.Name = name

    def jiao(self):
        print("%s 叫"%(self.Name))

    def piao(self):
        print("%s 票 苍井空" % self.Name)

class Dog(Animals,Dog_F):
    def __init__(self,name):
        self.Name = name

    def jiao(self):
        print("%s 叫"%(self.Name))


dog1 = Dog("小强")
dog1.piao()
"""
class A:
    def bar(self):
        print("bar")
        self.f2()
class B(A):
    def f1(self):
        self.bar()
class C:
    def f2(self):
        print("c")

class D(C,B):
    pass
d1=D()
d1.f1()
