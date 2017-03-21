#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys
# # print(__file__)#文件的路径
# # print(os.path.dirname(__file__))#返回文件的目录，文件的上层
# # print(os.path.dirname(os.path.dirname(__file__)))#上层的上层
# # print(os.path.basename(__file__))#返回文件名
# f1=os.path.basename(__file__)
# f2=os.path.dirname(__file__)
# f3=os.path.join(f2,f1)
# sys.path.append(f3)
# sys.path.append(__file__)
for i in sys.path:
    print(i)
