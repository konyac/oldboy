#!/usr/bin/env python
# _*_ coding:utf-8 _*_
li = []
for i in range(10):
    def f1():
        return i


    li.append(f1)  # 放进去的是一个一个的函数f1，未执行的。

print(li)
print(li[0])
print(li[0]())
# 输出为 9  根据作用域链  f1 未执行，因此变量i未赋值。 但是最后执行li[0]()回调f1（） return i 这时候就需要向上查找了，i 最后为9

# 同上
li = [lambda :x for x in range(10)]#一个一个函数的lambda函数放到列表中，没有被执行。执行的时候x变为9了。
print(li[0]()) # 为9
