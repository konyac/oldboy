#!/usr/bin/env python
# -*- coding:utf-8 -*-

#str字符串方法练习
a="alex"
ret=a.capitalize() #不用添加参数，字符串首字母变大写，str(object='') -> string
print(ret)
ret1=a.center(20,"*") #内容居中，width：总长度；fillchar：空白处填充内容，默认无。S.center(width[, fillchar]) -> string
print(ret1)
a2="alex is alph"
ret2=a2.count("al") #计算子序列个数,def count(self, sub, start=None, end=None):,可定义开始和结束位置。S.count(sub[, start[, end]]) -> int
ret3=a2.count("a",0)
print(ret2,ret3)

ret4=a2.endswith("alp",0,-1)  #""" 是否以 xxx 结束 """endswith(self, suffix, start=None, end=None):，可定义开始和结束的位置，S.endswith(suffix[, start[, end]]) -> bool
print(a2.startswith("a")) #""" 是否以 xxx 开始 """ startswith(self, prefix, start=None, end=None):，可定义开始和结束的位置，S.startswith(prefix[, start[, end]]) -> bool
print(ret4)
a3="hello\t999" #""" 将tab转换成空格，默认一个tab转换成8个空格 """def expandtabs(self, tabsize=None):可以定义空格个数，S.expandtabs([tabsize]) -> string
print (a3)
print (a3.expandtabs(20))

s="hello alex"
s.find("al") #""" 寻找子序列位置，如果没找到，返回 -1 """def find(self, sub, start=None, end=None):可以定义开始和结束的位置，S.find(sub [,start [,end]]) -> int
print (s.find("al"))
s1="hello {0},age {1}" #{0},{1}可以充当占位符
a4=s1.format("alex",18) #""" 字符串格式化，动态参数，将函数式编程时细说 """def format(*args, **kwargs):S.format(*args, **kwargs) -> string
print (s1,a4)
print (s.index("ll")) #""" 子序列位置，如果没找到，报错 """ def index(self, sub, start=None, end=None):可以定义开始和结束的位置，S.index(sub [,start [,end]]) -> int
num1="dasfsdfaa"
num2="jkljljl"
num3="57876"
num4="kkk*  &687689"
num5=" "
num6="Alss Sss 888&&&L  "
num7="ALJL"
print (num1.isalnum()) #""" 是否是字母或数字组成"""必须要字母和数字组成的字符串，含有其他字符返回FalseS.isalnum() -> bool
print (num2.isalpha())#""" 是否全是字母 """
print (num3.isdigit()) #""" 是否全是数字 """
print (num4.islower()) # """ 这里面的字母是否小写 """可以包含其他字符
print (num5.isspace())#是否全是空格，且自少有一个字符
print (num6.istitle()) #是否是标题，所有首字母都是大写
print (num7.title())#变成标题
print (num7.isupper())#是否全是大写
li=["alex","eric"]
li2=("alex","eric")
print ("_".join(li2))#""" 连接 """def join(self, iterable):  参数是可迭代的，循环li的元素，让每个元素用“_”连接起来

pp="alexKKK000***1111"
print (pp.ljust(20,"*"))#""" 内容左对齐，右侧填充 """width：总长度；fillchar：空白处填充内容，默认无。-> string
print (pp.rjust(20,"*"))#内容右对齐
print (pp.lower())#字母全部变成小写-> string
print (pp.upper())#字母全部变成大写-> string
print (pp.swapcase())#小写变大写，大写变小写
kb="    kkkkfasdfa  jkljlk    "
print (kb.lstrip())#""" 移除左侧空白 """
print (kb.rstrip())#""" 移除右侧空白 """
print (kb.strip())#""" 移除两侧的空白 """

sb="alex SB alex SB"
print (sb.partition("SB"))#""" 分割，前，中，后三部分 """添加到一个元祖里面S.partition(sep) -> (head, sep, tail)
print (sb.replace("SB","HH"))#""" 替换 """count参数是替换几个的意思
print (sb.replace("SB","HH",1))

fg="alexalex"
print (fg.split("e"))#""" 分割， maxsplit最多分割几次 """S.split([sep [,maxsplit]]) -> list of strings
print (fg.split("e",1))
fg1="alex\nalex"
print (fg.splitlines())#""" 根据换行分割 """




