#!/usr/bin/env python
# -*- coding:utf-8 -*-
#list列表方法练习
name_list = ['alex', 'seven', 'eric']

name_list.append("seven") #在末尾追加
name_list.append("seven")
name_list.append("seven")
print (name_list)
print (name_list.count("seven"))#统计出现的次数
#iterable可迭代的,只要能够通过for循环的 都是可迭代的。
temp=[11,"bb",222]
name_list.extend(temp) #本身后面添加可迭代的参数
print (name_list)
print (name_list.index(11))#索引
name_list.insert(1,"sb")#在某个位置插入
print (name_list)
a=name_list.pop()#尾部删掉，可赋值给别人
print (name_list,a)
x=name_list.remove("seven")#只移除找到的第一个，不可赋值
print (name_list,x)
name_list.reverse()#反转
print(name_list)
name_list2=[1,2,44,52,4,2,55,2]
name_list3=["kksaj","jalkdjl","ax","bb"]
name_list3.sort()#排序，里面的元素必须一致
print(name_list3)
name_list4=["eirc","andy","ALex"]
del name_list4[1]#删除列表指定位置的元素，索引位置,可用切片
print(name_list4)