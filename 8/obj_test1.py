#!/usr/bin/env python
# -*- coding:utf-8 -*-
class func(object):
    def __init__(self,name,age,nv,doing):
        self.name=name
        self.age=age
        self.nv=nv
        self.doing=doing
    def out(self):
        print(self.name,self.age,self.nv,self.doing)
obj=func("小明","10岁","男","上山去砍柴")
obj.out()

