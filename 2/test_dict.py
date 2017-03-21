#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dict字典的特殊方法

user_info={"name":"alex",
"age":18,
"gender":"M"
}
print (len(user_info))#长度
#user_info.clear()#清空字典，清楚所有内容
print (user_info.get("name"))
print (user_info.get("name1",123)) #  """ 根据key获取值，d是默认值 """如果key不存在，返回默认值，不会报错
print (user_info["name"]) #如果不存在会报错
# print (user_info.has_key("name")) #""" 是否有key """
a=user_info.pop("age")#获取并在字典中移除,可以将key赋值给一个变量
print (user_info,a)
a=user_info.popitem()#移除key values 赋值给一个元祖中
print (user_info)

# user_info.iteritems()
# print (user_info)
user_info.update({"kkk": "jjk"})#更新
print (user_info)

#@staticmethod,类方法
user_info_new=dict.fromkeys(["k","name"],"alex")
print (user_info_new)