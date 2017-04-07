#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, hashlib

sk = socket.socket()
sk.connect(("127.0.0.1", 9999))


def login(user, pwd):
    sk.sendall(bytes("login", encoding="utf-8"))
    if str(sk.recv(1024), encoding="utf-8") == "login":
        l_account = user + "$" + md5(pwd) + "\n"
        sk.sendall(bytes(l_account, encoding="utf-8"))
        if str(sk.recv(1024), encoding="utf-8") == "1":
            return True
        else:
            return False
    else:
        pass


def md5(args):
    hash = hashlib.md5(bytes("salt%#%salt", encoding="utf-8"))
    hash.update(bytes(args, encoding="utf-8"))
    return hash.hexdigest()


def register(user, pwd):
    password = md5(pwd)
    account = user + "$" + password + "\n"
    sk.sendall(bytes("reg", encoding="utf-8"))
    if str(sk.recv(1024), encoding="utf-8") == "acc":
        sk.sendall(bytes(account, encoding="utf-8"))
        ret = str(sk.recv(1024), encoding="utf-8")
        if ret == "1":
            return 1
        elif ret == "0":
            return 0
        else:
            return 2


def command():
    sk.sendall(bytes("comm", encoding="utf-8"))
    while True:
        ret = str(sk.recv(1024), encoding="utf-8")
        if ret == "#":
            inp = input(ret+"(q退出)：")
            sk.sendall(bytes(inp,encoding="utf-8"))
            out=str(sk.recv(1024),encoding="gbk")
            if out=="exit":
                break
            print(out)
            sk.sendall(bytes("over",encoding="utf-8"))

def main():
    while True:
        inp = input("欢迎。1、注册。2、登陆(q退出)\n>>>")
        if inp == "1":
            user = input("用户名：")
            pwd = input("密码：")
            if register(user, pwd) == 1:
                print("注册成功")
            elif register(user, pwd) == 0:
                print("用户已经注册")
        elif inp == "2":
            user = input("用户名：")
            pwd = input("密码：")
            if login(user, pwd):
                print("登陆成功")
                while True:
                    inp=input("1、执行命令.2、上次文件(q退出)\n>>>")
                    if inp == "1":
                        command()
                    elif inp == "2":
                        pass
                    else:
                        break


            else:
                print("登陆失败")
        else:
            break


if __name__ == "__main__":
    main()
