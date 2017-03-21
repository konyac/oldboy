#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = '测试字符'        #默认是utf-8
a_unicode = a.decode('utf-8')  # decode是解码成unicode 括号是脚本内容的默认编码  即：将脚本内容的utf-8解码成unicode
a_gbk = a_unicode.encode('gbk') #encode是编码，将unicode的编码内容编码成指定的，这里是gbk
print(a_gbk)  #用于终端打印
print(u"测试字符二")  #3里面是字符串  2里面是unicode