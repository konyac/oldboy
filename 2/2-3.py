#!/usr/bin/env python
# -*- coding:utf-8 -*-
#输出商品列表，用户输入序号，显示用户选中的商品
# 商品 li = ["手机", "电脑", '鼠标垫', '游艇']
li=["手机", "电脑", '鼠标垫', '游艇']
'''
for i in range(0,len(li)):
    print i,li[i]
inp=int(raw_input("请选择："))
print li[inp]
'''
for i,j in enumerate(li,1):
    print (i,j)
inp=int(input("请选择："))
print (li[inp-1])