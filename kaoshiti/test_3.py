#!/usr/bin/env python
# -*- coding:utf-8 -*-
#获取两个列表l1=[11,22,33],l2=[22,33,44]中相同的元素集合
l1=[11,22,33]
l2=[22,33,44]
s1=set(l1)
s2=set(l2)
new=s1.intersection(s2)
print(list(new))