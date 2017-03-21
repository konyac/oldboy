#!/usr/bin/env python
# -*- coding:utf-8 -*-
#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
lis=[11,22,33,44,55,66,77,88,99,90]
"""
a1=[]
a2=[]
d3={'k1':a1,'k2':a2}
for i in range(0,len(lis)):
    if lis[i]>66:
        a1.append(lis[i])
    elif lis[i]<66:
        a2.append(lis[i])
    else:
        pass
print d3
"""
dic={"k1":[],"k2":[]}
for i in lis:
    if i>66:
        dic["k1"].append(i)
    else:
        dic["k2"].append(i)
print (dic)

