#!/usr/bin/env python
# -*- coding:utf-8 -*-
#需求new_dict 和old_dict 字典的key相同的，new_dict的【key】值==》old_dict【key】
#old中存在，new中不存在，old中删除
old_dict={
    "#1":11,
    "#2":22,
    "#3":100,
}
new_dict={
    "#1":33,
    "#4":22,
    "#7":100,
}
old_set=set(old_dict.keys())
new_set=set(new_dict.keys())
he_set=old_set.intersection(new_set)
de_set=old_set.difference(new_set)
# print(he_set,de_set)
for o in he_set:
    old_dict[o]=new_dict[o]
# print(old_dict)
for p in de_set:
    del old_dict[p]
print(old_dict)
