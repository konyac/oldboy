#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

def md5(args):
    hs=hashlib.md5()
    hs.update(bytes(args,encoding="utf-8"))
    return hs.hexdigest()


def register(us,pw):
    with open("db","a",encoding="utf-8") as f:
        temp=us+"|"+md5(pw)+"\n"
        f.write(temp)
def login(us,pw):
    with open("db","r",encoding="utf-8") as f:
        for i in f:
            u,p=i.strip().split("|")
            if u==us and md5(pw)==p:
                return True
ch=int(input("1.登陆\n2.注册"))
if ch==2:
    user=input("用户名：")
    pwd=input("密码：")
    register(user,pwd)
if ch==1:
    user = input("用户名：")
    pwd = input("密码：")
    r=login(user,pwd)
    if r:
        print("登陆成功")
    else:
        print("登陆失败")
