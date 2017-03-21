#!/usr/bin/env python
# -*- coding:utf-8 -*-

# tpl = "i am %s" % "alex" #i am alex
# print(tpl)
# tpl = "i am %s age %d" % ("alex", 18) #i am alex age 18
# print(tpl)
# tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18} #i am alex age 18
# print(tpl)
# tpl = "percent %.2f" % 99.97623  #percent 99.98
# print(tpl)
# tpl = "i am %(pp).2f" % {"pp": 123.425556, } #i am 123.43
# print(tpl)
# tpl = "i am %(pp).2f %%" % {"pp": 123.425556, } # i am 123.43 % # 两个%是%
# print(tpl)
# tpl = "i am %(pp).2f" % {"pp": 123.425556, } # i am 123.43
# tpl = "i am %(pp)-10s jianzuo" % {"pp": "liu", } #左对齐   i am liu        jianzuo
tpl = "i am %(pp)+06d jianzuo" % {"pp": -123, } #右对齐   i am -00123 jianzuo
print(tpl)
tpl = "i am %(pp)6d jianzuo" % {"pp": -123, } #右对齐   i am   -123 jianzuo
print(tpl)
tpl = "i am %(pp)-6d jianzuo" % {"pp": -123, } #右对齐   i am -123   jianzuo
print(tpl)