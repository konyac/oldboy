#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# effect_row=cursor.execute("select * from userinfo WHERE name = %s",('abb',))
effect_row=cursor.execute("insert into userinfo (name,password) VALUES (%s,%s)",("ooxx",111111))

print(effect_row)
tag = cursor.lastrowid
print(tag)
# 获取第一行数据,游标已经设置在执行的结果中了，
row_1 = cursor.fetchone()

# 获取前n行数据
# row_2 = cursor.fetchmany(2)
# 获取所有数据
# row_3 = cursor.fetchall()
print(row_1)
# print(row_2)
# print(row_3)
conn.commit()
cursor.close()
conn.close()