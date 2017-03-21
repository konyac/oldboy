#!/usr/bin/env python
# -*- coding:utf-8 -*-

# abs取绝对值
i = abs(-123)
print(i)

# all,循环参数，如果每个元素都为真，那么all的返回值为真
r1 = all([111, 222, 333, 0])
r2 = all([11, 22, 33, -1])  # 只要不是0就是真
r3 = all(["aa", "aa", [11, {}]])  # 只判断最外层
print(r1, r2, r3)

# 什么是假的。False,0,None,"",[],(),{},用bool值.
print(bool(0), bool(None), bool(-1), bool("123"), bool(""))

# any，只要有一个为真，则为真
r4 = any([None, [], 0])
r5 = any([11, 22, 33, -1])  # 只要不是0就是真
r6 = any(["aa", "aa", [11, {}]])  # 只判断最外层
print(r4, r5, r6)


# ascii,去对象的类中，找__repr__,获取返回值.
# 2版本中没有
class foo():
    def __repr__(self):
        return "hello"


obj = foo()
r = ascii(obj)
print(r)

# bin 二进制
# hex 十六进制
# oct 八进制
# int 十进制
print(bin(11))
print(oct(8))
print(hex((111)))
# 其他进制的数转成十进制
print(int("0b1011", base=2))  # 必须是字符串，可以不带o b x .base= 对应的原来进制
print(int("72", base=8))
print(int("ac1", base=16))

# bool判断真假，把一个对象转化成bool值，None,"",[],{}

# bytes 字节
# bytearray 字节列表
# 字节和字符串的转化
print(bytes("string", encoding="utf-8"))

# chr() 接收一个十进制数字，找到这个数字对应的ASCII码中对应的字符
# ord() 接收一个字符，找到ASCII码种对应的十进制数字
# 一个字节8位，2**8，ASCII码，256种。验证码
print(chr(78))
print(ord("A"))

# callable，一个对象是否可以被执行，所有的后面能够加括号，去执行一段代码，就是可以执行的
# compile()编译一个字符串成Python可以执行的代码，编译代码
# complex复数
# dir()
# help()
# divmod()除取余数
# eval()可以执行计算一个字符串形式的表达式，有返回值
print(eval("1+2+3"))
# exec()没有返回值，只是执行一段Python代码
exec("for i in range(10):print(i)")


# filter(函数，可迭代的对象)过滤,接收两个参数，一个是函数，一个是可迭代的对象，迭代每一次都执行这个函数，一旦返回True，把元素放到返回值中，迭代的对象。只有循环的时候能够直接打印出来
def fun1(x):
    if x > 22:
        return True
    else:
        return False


ret = filter(fun1, [11, 22, 33, 44])
ret2 = filter(lambda x: x > 22, [11, 22, 33, 44])
for i in ret:
    print(i)
for i in ret2:
    print(i)


# map(函数，可迭代的对象),批量的操作
def fun2(x):
    return x + 100


ret4 = map(lambda x: x + 100, [1, 2, 3, 4, 5, 6])
ret3 = map(fun2, [1, 2, 3, 4, 5, 6])
for i in ret3:
    print(i)
for i in ret4:
    print(i)