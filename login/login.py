#!/usr/bin/env python
# -*- coding:utf-8 -*-
def login(username, password):
    """
    判断用户名，密码是否正确
    :param username: 用户名
    :param password: 密码
    :return: True：正确登陆，False：用户名或密码错误，无法登陆
    """
    with open("db", "r", encoding="utf-8") as f:
        for line in f:
            line_list = line.strip().split(":")
            if username == line_list[0] and password == line_list[1]:
                return True
    return False

def register():
    """
    新用户注册判断用户名是否存在，密码位数是否正确
    :return: True：注册成功
    """
    user = input("请输入用户名：")
    while True:
        ret = user_exist(user)  # 判断用户名是否存在
        if ret:
            print("用户名已存在！")
            user = input("请重新输入用户名：")
            continue
        else:
            break
    pwd = pwd_rule()  # 密码规则验证及获取输入密码
    with open("db", "a") as f:
        if f.tell() != 0:
            temp = "\n" + user + ":" + pwd
            f.write(temp)
            return True
        else:
            temp = user + ":" + pwd
            f.write(temp)
            return True

def user_exist(username):
    '''
    验证密码用户名是否重复
    :param username: 用户名
    :return: True：用户名重复
    '''
    with open("db", "r", encoding="utf-8") as f:
        for line in f:
            line_list = line.strip().split(":")
            if username == line_list[0]:
                return True
    return False

def change_pwd(username, password):
    """
    修改密码
    :param username: 原始账户
    :param password: 原始密码
    :return: True：修改成功。
    """
    with open("db", "r", encoding="utf-8") as f:
        data = f.readlines()
        # print(data)
        for i in range(len(data)):
            line_list = data[i].strip().split(":")
            if username == line_list[0] and password == line_list[1]:  # 判定账户输入正确
                print("验证成功，开始设定新密码\n")
                new_pwd = pwd_rule()
                print(new_pwd)
                data[i] = username + ":" + new_pwd + "\n"  # 设定新密码行
                with open("db", "w", encoding="utf-8") as n:
                    n.writelines(data)  # 重新写进去
                    return True
    print("验证失败")
    return False

def del_user(username, password):
    with open("db", "r", encoding="utf-8") as f:
        data = f.readlines()
        # print(data)
        for i in range(len(data)):
            line_list = data[i].strip().split(":")
            if username == line_list[0] and password == line_list[1]:  # 判定账户输入正确
                print("验证成功，确定删除用户\n")
                inp = input("y/s?")
                if inp == "y":
                    del data[i]
                    with open("db", "w", encoding="utf-8") as n:
                        n.writelines(data)  # 重新写进去
                        print("删除成功")
                        return True
                else:
                    print("取消删除")
                    return True

    print("验证失败")
    return False

def pwd_rule():
    """
    新密码的输入，判定密码规则是否符合
    :return: 返回密码
    """
    while True:
        password = input("请输入密码：")
        if len(password) < 6:  # 密码少于6位需要重新输入
            print("密码至少6位")
            # password = input("重新输入密码：")
            continue
        pwd_again = input("请再次输入：")  # 密码2次确认。2次输入错误重新输入。
        if password == pwd_again:
            return password
        else:
            print("两次输入不一样")
            continue

def confirm(chose):
    """
    操作选项
    :param chose: 选项
    :return: 无
    """
    while True:
        if chose == 1:
            flag = False
            while True:
                user = input("请输入用户名：")
                pwd = input("请输入密码：")
                ret = login(user, pwd)
                if ret:
                    print("登陆成功")
                    flag = True
                    break
                else:
                    print("登陆失败，重新登陆")
                    continue
            if flag:
                break
        elif chose == 2:
            ret = register()
            if ret:
                print("注册成功")
                break

        elif chose == 3:
            user = input("请输入用户名：")
            pwd = input("请输入密码：")
            if change_pwd(user, pwd):
                print("密码修改成功")
                break
        elif chose == 4:
            user = input("请输入用户名：")
            pwd = input("请输入密码：")
            if del_user(user, pwd):
                print("操作完成")
                break
        elif chose == 5:
            print("退出")
            break
        else:
            new_chose = int(input("输入错误，重新选择：\n"))
            chose = new_chose
            continue

def main():
    print("欢迎登陆SB系统！")
    print("请选择：\n1、登陆\n2、注册\n3、修改密码\n4、删除用户\n5、退出")
    inp = int(input())
    confirm(inp)

if __name__ == "__main__":
    main()