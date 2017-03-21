#!/usr/bin/env python
# -*- coding:utf-8 -*-

#在3.5中可以直接输出，一个字符一个字符来。按照字符来循环
li="李帅"
for i in li:
    print(i)
#在2.7中，按照字节来循环。一个汉字6个字节。


#bytes获取自己
#str(字节类型，编码)
#将字符转化成字节
a="联社"
b=bytes(a,encoding="utf-8")
b2=bytes(a,encoding="gbk")
print(b,b2)
#将字节转化成字符串
new_b=str(b,encoding="utf-8")
new_b2=str(b2,encoding="gbk")
print(new_b,new_b2)

# li=["kk","jkjkj","sdfj"]
# new_dict=dict(enumerate(li))
# print new_dict