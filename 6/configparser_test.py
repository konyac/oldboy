#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import configparser
# con=configparser.ConfigParser()#创建对象
# con.read("oo.ini",encoding="utf-8")#读配置文件
# # ret=con.sections()#所有选项节点，放到列表中
# ret=con.get("mysqld","port")
# print(ret,type(ret))

import configparser
con=configparser.ConfigParser()
con.read("oo.ini",encoding="utf-8")
has_op=con.has_option("mysql","port")
con.set("mysql","port2","3308")
print(has_op)
con.write(open("oo.ini","w",encoding="utf-8"))
