#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
#
# # ######## md5 ########
#
# hash = hashlib.md5()
# hash.update(bytes("admin",encoding="utf-8"))
# print(hash.hexdigest())
#
# # ######## sha1 ########
#
# hash = hashlib.sha1()
# hash.update(bytes("admin",encoding="utf-8"))
# print(hash.hexdigest())
#
# # ######## sha256 ########
#
# hash = hashlib.sha256()
# hash.update(bytes("admin",encoding="utf-8"))
# print(hash.hexdigest())
#
# # ######## sha384 ########
#
# hash = hashlib.sha384()
# hash.update(bytes("admin",encoding="utf-8"))
# print(hash.hexdigest())
#
# # ######## sha512 ########
#
# hash = hashlib.sha512()
# hash.update(bytes("admin",encoding="utf-8"))
# print(hash.hexdigest())

# ######## md5 加盐########
#
# hash = hashlib.md5(bytes("salt;%#%salt",encoding="utf-8"))
#
# hash.update(bytes("admin",encoding="utf-8"))
# print(hash.hexdigest())

obj = hashlib.md5(bytes("salt;%#%salt", encoding="utf-8"))  # 这里是输入的盐值  ##创建hash对象，md5:(message-Digest Algorithm 5)消息摘要算法,得出一个128位的密文
print(obj)  # <md5 HASH object @ 0x0000000000A1F800>
obj.update(bytes("mypasswd123", encoding="utf-8"))  # 更新哈希对象以字符串参数 其实就是你的明文密码
print(obj.digest())  ##返回摘要，作为二进制数据字符串值  b'\x04\x80)\x17\\\xf8dPA\xbc\xd9@e\xeb&\x0f'
print(obj.hexdigest())  # 返回十六进制数字字符串  048029175cf8645041bcd94065eb260f