#!/usr/bin/env python
# -*- coding:utf-8 -*-
from xml.etree import ElementTree as ET

# root=ET.XML(open("first.xml","r",encoding="utf-8").read())
# print(root.tag)
# for node in root:
#     print(node.tag,node.attrib,node.find("rank").text)

from xml.etree import ElementTree as ET

############ 解析方式一 ############
"""
# 打开文件，读取XML内容
str_xml = open('first.xml', 'r').read()

# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ET.XML(str_xml)
"""
############ 解析方式二 ############

# 直接解析xml文件
tree = ET.parse("first.xml")
# print(type(tree))
# 获取xml文件的根节点
root = tree.getroot()
# print(type(root))


### 操作

# 顶层标签
# print(root.tag)


# # 遍历XML文档的第二层
# for child in root:
#     # 第二层节点的标签名称和标签属性
#     print(child.tag, child.attrib)
#     # 遍历XML文档的第三层
#     for i in child:
#         # 第二层节点的标签名称和内容
#         print(i.tag,i.text)
for node in root.iter("year"):
    print(node.tag,node.text)