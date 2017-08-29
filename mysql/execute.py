#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test1')
# 创建游标
cursor = conn.cursor()
u = input(">>")
p = input(">>")
e = input(">>")
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("insert into user (name,password,email) VALUES ('alex','123','alex@173.com')")

# effect_row = cursor.execute("insert into user (name,password,email) VALUES (%s,%s,%s)",(u,p,e)) #占位符

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,)) #占位符，

# 执行SQL，并返回受影响行数,插入多个元素。放到一个列表中，列表中是一个一个的元组
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

print(effect_row)
# 提交，不然无法保存新建或者修改的数据 #select 等不需要提交
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()