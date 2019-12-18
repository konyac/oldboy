# coding:utf-8
us = input('请输入用户名：')
pw = input('请输入密码：')
nu = 0
while True:
    nu = nu + 1
    if us == 'cuicui' and pw == '6466278':
        print('登陆成功！\n')
        break
    elif nu == 3:
        print('登陆错误次数过多，禁止登陆！\n')
        break
    else:
        print('用户名密码错误，请重新输入')
        us = input("请输入用户名：")
        pw = input('请输入密码：')
