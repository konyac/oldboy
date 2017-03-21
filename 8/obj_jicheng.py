#!/usr/bin/env python
# -*- coding:utf-8 -*-
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