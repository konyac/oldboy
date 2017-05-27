#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file = open("test.txt", "r",encoding="gbk")
# date = file.read()
# file.close()
# print(date)
with open("output.txt", "r",encoding="utf-8") as f:
    # print(f.tell())
    print(f.read(2))
    print(f.tell())
    # print(f.read())
    # f.seek(0)
    # print(f.read(3))
    # f.write("帅哥")

    # print(f.tell())
    # print(f.read())
    # f.write("哈哈")
    # print(f.tell())
    # f.seek(1)
    # print(f.read(1))
    # f.write("哈哈哈哈哈哈")
    # f.seek(0)
    # print(f.readline())
    # print(f.readline())
    # print(f.tell())


