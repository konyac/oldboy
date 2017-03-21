#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
#     li = ["alec", " aric", "Alei", "Tony", "rain"]
#     tu = ("alec", " aric", "Alei", "Tony", "rain")
#     dic = {'k1': "alei", 'k2': ' aric',  "k3": "Alei", "k4": "Tony"}

li = ["alec", " Aric", "Alei", "Tony", "rain"]
tu = ("alec", " Aric", "Alei", "Tony", "rain")
dic = {'k1': "alei", 'k2': ' aric',  "k3": "Alec", "k4": "Tony"}
li_new = []
tu_new = []
dic_new={}
for i in li:
    i=i.strip()
    #if判断顺序，从前往后，or，自己成功就行了，and。
    if (i.startswith("a") or i.startswith("A")) and i.endswith("c"):
        li_new.append(i)
    else:
        pass
for i in tu:
    i=i.strip()
    if (i.startswith("a") or i.startswith("A")) and i.endswith("c"):
        tu_new.append(i)
    else:
        pass
for i,j in dic.items():
    j=j.strip()
    if (j.startswith("a") or j.startswith("A")) and j.endswith("c"):
        # dic_new.update({i:j})
        dic_new[i]=j
    else:
        pass
print (li_new)
print (tu_new)
print (dic_new)