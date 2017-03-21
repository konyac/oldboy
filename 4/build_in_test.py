#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !usr/bin/env python
# coding:utf-8

namespace = {'name': 'wupeiqi', 'data': [18, 73, 84]}

code = '''def hellocute():return  "name %s ,age %d" %(name,data[0],) '''

func = compile(code, '<string>', "exec")

exec(func in namespace)

result = namespace['hellocute']()

print(result)
