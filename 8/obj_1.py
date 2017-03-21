#!/usr/bin/env python
# -*- coding:utf-8 -*-
# class Oldboy(object):
#
#     def fecht(self,backend):
#         print(backend)
#     def add_record(self,backend):
#         print(backend)
#
# obj1=Oldboy()
# # obj1.backend="www.olddriver.com"
# obj1.fecht("www.olddriver.com")

class Oldboy(object):
    def __init__(self,bk):
        self.name="alex"
        self.favor=bk
        print(self.name,self.favor,id(self))
obj=Oldboy("www.olddriver.com")
print(id(obj))