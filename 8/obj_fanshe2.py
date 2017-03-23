#!/usr/bin/env python
# -*- coding:utf-8 -*-
#导入模块
m=__import__("s2",fromlist=True)
#去模块中找类
class_name=getattr(m,"Do")
print(class_name)
#根据模块创建对象
obj=class_name("alex")
#去对象中找name对应的值
m=getattr(obj,"name")
print(m)