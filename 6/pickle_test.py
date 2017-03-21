#!/usr/bin/env python
# -*- coding:utf-8 -*-

#dump dumps 转化写入文件的练习
# accounts = {
#     1000: {
#         'name': 'Alex LI',
#         'email': 'lijie3721@126.com',
#         'passwd': 'abc123',
#         'balance': 15000,
#         'phone': 13651054608,
#         'bank_acc': {
#             'ICBC': 14324234,
#             'CBC': 235234,
#             'ABC': 35235423
#         }
#     },
#     1001: {
#         'name': 'CaiXin Guo',
#         'email': 'caixin@126.com',
#         'passwd': 'abc145323',
#         'balance': -15000,
#         'phone': 1345635345,
#         'bank_acc': {
#             'ICBC': 4334343,
#         }
#     },
# }
#
# import pickle
#
# # dumps 直接传存储对象，也就是先转成制服穿在传进文件
# # f = open("pickle_test.db", "wb")
# # f.write(pickle.dumps(accounts))
# # f.close()
# #dump除了传存储对象还有打开的文件句柄，同事完成
# f = open("pickle_test2.db", "wb")
# pickle.dump(accounts, f)
# f.close()

#load loads读文件的练习
import pickle

# f = open("pickle_test.db", "rb")
#
# acc = pickle.loads(f.read())
# f.close()
# print(acc,type(acc))
f = open("pickle_test2.db", "rb")
acc_load = pickle.load(f)
print(acc_load)