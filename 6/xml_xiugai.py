#!/usr/bin/env python
# -*- coding:utf-8 -*-
from xml.etree import ElementTree as ET

#打开文件读取xml内容
# root=ET.XML(open("first.xml","r",encoding="utf-8").read())
str_xml = open('first.xml', 'r').read()

# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root=ET.XML(str_xml)

############ 操作 ############
#顶层标签
print(type(root))
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
tree = ET.ElementTree(root)
tree.write("newnew.xml", encoding='utf-8')