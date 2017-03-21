#!/usr/bin/env python
# -*- coding:utf-8 -*-
# read
# 以只读的方式打开文件hello.txt
# f = open("hello.txt", "r")
# # 读取文件内容赋值给变量c
# c = f.read()
# # 关闭文件
# f.close()
# # 输出c的值
# print(c)

# # readline
# # 以只读模式打开文件hello.txt
# f = open("hello.txt","r")
# # 读取第一行  strip 去除空行
# c1 = f.readline().strip()
# # 读取第二行
# c2 = f.readline().strip()
# # 读取第三行
# c3 = f.readline().strip()
# # 关闭文件
# f.close()
# # 输出读取文件第一行内容
# print(c1)
# # 输出读取文件第二行内容
# print(c2)
# # 输出读取文件第三行内容
# print(c3)
# 以只读的方式打开文件hello.txt

f = open("hello.txt", "r")
# 将文件所有内容赋值给c
c = f.readlines()
# 查看数据类型
print(type(c))
# 关闭文件
f.close()
# 遍历输出文件内容 # n.strip()去除空行
for n in c:
    print(n.strip())
