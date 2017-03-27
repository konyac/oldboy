#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
try:
    inp=input("输入数字：")
    print(int(inp))
except Exception as e:
    print(e)
"""
"""
实例：IndexError
dic = ["wupeiqi", 'alex']
try:
    dic[10]
except IndexError as e:
    print(e)
"""
"""
KeyError实例
dic = {'k1':'v1'}
try:
    dic["k20"]
except KeyError as e:
    print(e)
"""
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
# except Exception as e:
#     print(e)