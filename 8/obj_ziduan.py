#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 普通字段和静态字段
class Province:
    # 静态字段
    country = "中国"


    def __init__(self, name):
        # 普通字段
        self.name = name

    # 直接访问普通字段


obj = Province('河北省')
print(obj.name)  # 直接访问静态字段
rt=Province.country
print(rt)
