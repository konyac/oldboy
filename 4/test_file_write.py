#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 以只读的模式打开文件write.txt，没有则创建，有则覆盖内容
# file = open("write.txt","w")
# # 在文件内容中写入字符串test write
# file.write("aaa")
# # 关闭文件
# file.close()
# 以只读模式打开一个不存在的文件wr_lines.txt
f = open("wr_lines.txt", "w", encoding="utf-8")
# 写入一个列表
f.writelines(["11", "22", "33"])
# 关闭文件
f.close()
