#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
def has_space(args):
    if isinstance(args,str) or isinstance(args,list) or isinstance(args,tuple):
        for i in args:
            if i == " ":
                return True
                break
        else:
            return False
    else:
        return None
st="jkljkjlj"
lis=[11,22,33,44,55," "]
tup=(11,22,33,44,55,66," ")
print(has_space(st),has_space(lis),has_space(tup))

