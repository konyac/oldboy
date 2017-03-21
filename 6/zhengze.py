#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

# 从头匹配
# re.match()

# 简单
# 分组

# 浏览全部字符串，匹配第一个复合规则的字符串
# re.search()

# 将匹配到的所有内容都放置在一个字符串中
# origin = "hello alex sadf dsaf"
# r = re.match("h\w+",origin)
# print(r.group())  # hello  获取匹配所有结果
# print(r.groups())  #('h',)  #获取模型中匹配到的分组结果 没有分组则为空元组，
# r = re.match("(?P<n1>h)(?P<n2>\w+)",origin)  #获取模型中匹配到的分组中所有执行力key的组 ?P<KEY>VALUE   {'n2': 'ello', 'n1': 'h'}
# print(r.groupdict())   #?P<KEY>VALUE   {'n2': 'ello', 'n1': 'h'}

# origin = "hello alex alix bcd dsfa lefg abc 199"
# r = re.search("al(\w+)",origin)
# print(r.group()) #alix
# print(r.groups()) #()
# print(r.groupdict()) #{}
# origin = "hello alex alix bcd dsfa lefg abc 199"
# r = re.search("a(\w+).*(?P<key>\d)$",origin)
# print(r.group()) #alex
# print(r.groups()) #('lex',)
# r = re.search("(?P<key1>a)(?P<key2>(\w+))",origin)
# print(r.groupdict()) #{'key1': 'a', 'key2': 'lex'}
# a = "123abc456"
# print(re.search("[0-9]*[a-z]*[0-9]*", a).group())
#
# print(re.search("[0-9]*([a-z]*)([0-9]*)", a).group(0))
# print(re.search("[0-9]*([a-z]*)([0-9]*)", a).group(1))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))

# print(re.search("[0-9]*([a-z]*)([0-9]*)", a).groups())
#
# origin = "hello alex bcd abcd lge acd 19"
# n = re.split("(a\w+)",origin)
# print(n)

content = "1-2*((60-30+(1-40/5*5+3-2*5/3)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"


# def func(string):
#     new_list = re.split("\(([^()]+)\)", string, 1)
#     if len(new_list) > 1:
#         new_string = new_list[0] + str(eval(new_list[1])) + new_list[2]
#         return func(new_string)
#     else:
#         return new_list[0]
#
# print(eval(func(content)))
print(re.split("([+-])","14-40/5*5+3-2*5/3"))