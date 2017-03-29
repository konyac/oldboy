#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys, pickle

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.models import *
from conf import settings


def create_curriculum(admin_obj):
    curriculum_list = []
    if os.path.exists(settings.Teacher_dir):
        teacher_show = pickle.load(open(settings.Teacher_dir, "rb"))
        for i, item in enumerate(teacher_show, 1):  # 从1开始
            print(i, item.teacher_name)
        while True:
            curriculum_name = input("请输入课程名(q退出)：")
            if curriculum_name == "q":
                break
            curriculum_cost = input("请输入费用：")
            curriculum_teacher = input("请输入老师编号：")
            curriculum_obj = Curriculum(curriculum_name, curriculum_cost,
                                        teacher_show[int(curriculum_teacher) - 1].teacher_name, admin_obj)
            curriculum_list.append(curriculum_obj)
        if os.path.exists(settings.Curriculum_dir):
            exist_curriculum = pickle.load(open(settings.Curriculum_dir, "rb"))
            curriculum_list.append(exist_curriculum)
        pickle.dump(curriculum_list, open(settings.Curriculum_dir, "wb"))
    else:
        print("还没有老师请先创建老师")


def create_teacher(admin_obj):
    teacher_list = []
    while True:
        name = input("教师名字：(q退出)")
        if name == "q":
            break
        age = input("年龄")
        teacher_obj = Teacher(name, age, admin_obj)  # 创建老师
        teacher_list.append(teacher_obj)
    if os.path.exists(settings.Teacher_dir):
        exists_teacher = pickle.load(open(settings.Teacher_dir, "rb"))
        teacher_list.extend(exists_teacher)
    pickle.dump(teacher_list, open(settings.Teacher_dir, "wb"))


def login(user, pwd):
    path = os.path.join(settings.Base_admin_dir, user)  # 用户名创建一个路径
    if os.path.exists(path):  # 判断路径是否存在，存在就是说明用户正确。
        admin_obj = pickle.load(open(path, "rb"))  # 获取用户名对应的对象。
        if admin_obj.login(user, pwd):  # 执行这个对象的登陆方法
            print("登录成功")
            while True:
                inp = input("1、创建课程。2、创建老师(其他退出)\n>>>")
                if inp == "1":
                    create_curriculum(admin_obj)
                    continue
                elif inp == "2":
                    create_teacher(admin_obj)
                    continue
                else:
                    break
        else:
            print("密码错误")
    else:
        print("账号不存在")


def register(user, pwd):
    admin_obj = Admin()
    if admin_obj.register(user, pwd):
        print("管理员注册成功")
    else:
        print("管理员已存在")


def main():
    inp = input("管理员1、登陆。2、注册。(其他退出)\n>>>")
    user = input("账号：")
    pwd = input("密码:")
    if inp == "1":
        login(user, pwd)
    elif inp == "2":
        register(user, pwd)
    else:
        pass


if __name__ == "__main__":
    main()
