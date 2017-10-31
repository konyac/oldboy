#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from xml.etree import ElementTree as ET
# root = ET.Element("famliy")
# son1=ET.Element("son",{"name":"大儿子"})
# son2=ET.Element("son",{"name":"小儿子"})
#
# grandson1 = ET.Element('grandson', {'name': '大孙子'})
# grandson2 = ET.Element('grandson', {'name': '小孙子'})
#
# son1.append(grandson1)
# son2.append(grandson2)
# root.append(son1)
# root.append(son2)
# tree=ET.ElementTree(root)
# tree.write('oooo.xml',encoding='utf-8', short_empty_elements=False)
#
# from xml.etree import ElementTree as ET
#
# # 创建根节点
# root = ET.Element("famliy")
#
#
# # 创建大儿子
# # son1 = ET.Element('son', {'name': '儿1'})
# son1 = root.makeelement('son', {'name': '儿1'})
# # 创建小儿子
# # son2 = ET.Element('son', {"name": '儿2'})
# son2 = root.makeelement('son', {"name": '儿2'})
#
# # 在大儿子中创建两个孙子
# # grandson1 = ET.Element('grandson', {'name': '儿11'})
# grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# # grandson2 = ET.Element('grandson', {'name': '儿12'})
# grandson2 = son1.makeelement('grandson', {'name': '儿12'})
#
# son1.append(grandson1)
# son1.append(grandson2)
#
#
# # 把儿子添加到根节点中
# root.append(son1)
# root.append(son1)
#
# tree = ET.ElementTree(root)
# tree.write('oooo.xml',encoding='utf-8', short_empty_elements=False)

# 利用 makeelement创建 Element类的对象 创建一个新文件
#
# 利用 makeelement创建 Element类的对象 创建一个新文件

from xml.etree import ElementTree as ET
root=ET.Element("famliy")

son1=ET.SubElement(root,"son",attrib={'name': '儿1'})
son2=ET.SubElement(root,"son",attrib={'name': '儿2'})
grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
grandson1.text="孙子"
et=ET.ElementTree(root)
et.write("test.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)