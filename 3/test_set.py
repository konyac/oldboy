#!/usr/bin/env python
# -*- coding:utf-8 -*-
# s1=set() #创建空的set集合
# s2={11,22,33,44,55}  #直接创建set集合
# print(s2)
# l1=[11,22,33,44,22,11]
# l2=(11,22,11,22,333)
# l3="123"
# s3=set([11,22,33,22]) #传送可迭代的对象，转换成set集合
# s4=set(l3)
# print(set(l2))

se={11,22,33,55}
print(se)
se.add(44) #添加
print(se)
se.clear() #清除所有元素
print(se)
be={11,22,33}
ce={22,55}
print(be.difference(ce))#找be中存在。ce中不存在的set集合，返回值
print(ce.difference(be))#找ce中存在，be中不存在的set集合，返回值
be.difference_update(ce)#找be中存在，ce中不存在的，更新自己
print(be)
ae={11,22,33,444,555}
ae.discard(444) #移除元素,如果没有的话不报错
ae.remove(555)#移除元素,没有的话报错
print(ae)
ee={11,22,33,555}
fe={22,555,666,7,7665}
print(ee.intersection(fe)) #取A和B的交集，返回新值。原来的A和B不变，取交集，新创建一个set
ee.intersection_update(fe) #A和B的交集，不返回值，直接更新自己成这个交集，取交集，修改原来set
print(ee)
je={11,212,33,515}
ke={22,555,666,7,7665}
print(je.isdisjoint(ke))#判断Ａ和Ｂ有没有交集，有交集返回False，么有交集返回True
me={11,212,33,515}
ne={11,33}
print(ne.issubset(me))#判读A是否是B的子序列。是否是子集
print(me.issuperset(ne))#判读A是否是B的父序列。是否是父集
oe={11,212,33,55}
print(oe.pop()) #随机取一个值，去掉，并且可以返回这个值
print(oe)
pe={11,22,33,555}
qe={22,555,666,7,7665}
print(pe.difference(qe))
print(qe.difference(pe))
print(pe.symmetric_difference(qe))#将不共有的元素，组成一个set集合，差集，创建新对象
pe.symmetric_difference_update(qe)#将不共有的元素，组成一个set集合,并更新原有集合，差集，改变原来
print(pe)
re={11,22,33,555}
se={22,555,666,7,7665}
print(re.union(se))#A和B合并到一起，并集
me={22,555,666,545422}
me.update([22,9,8])#更新,多个元素，集合、元组，set
print(me)