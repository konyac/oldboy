#!/usr/bin/env python
# -*- coding:utf-8 -*-
from xml.etree import ElementTree as ET


############ 解析方式二 ############
# 直接解析xml文件
tree=ET.parse("first.xml")

#获取xml文件的根节点
root=tree.getroot()

############ 操作 ############
#顶层标签
print(root.tag)
# 循环所有的year节点
for node in root.iter("year"):
    # 将year节点中的内容自增一
    new_year=int(node.text)+1
    node.text=str(new_year)
    #设置属性
    node.set("name","Alex")
    node.set("age","19")
    #删除属性
    del node.attrib["name"]

tree.write("newnew2.xml", encoding='utf-8')