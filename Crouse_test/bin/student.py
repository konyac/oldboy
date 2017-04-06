#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pickle, os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.models import *
from conf import settings


def login(user, pwd):
    student_path = os.path.join(settings.Student_dir, user)
    if os.path.exists(student_path):
        student_obj = pickle.load(open(student_path, "rb"))
        if student_obj.login(user, pwd):
            print("登录成功")
            while True:
                inp = input("1、上课。2、选课。3、查看课表。(其他退出)")
                if inp == "1":
                    study_curriculum(student_obj)
                    continue
                elif inp == "2":
                    select_curriculum(student_obj)
                    continue
                elif inp == "3":
                    curriculum_info(student_obj)
                    continue
                else:
                    break
        else:
            print("登录失败")
    else:
        print("学生账号不存在")


def register(user, pwd):
    student_obj = Student()

    if student_obj.register(user, pwd):
        print("学生注册成功")
    else:
        print("学生已存在")


def curriculum_info(student_obj):
    print("已选课程信息：")
    if student_obj.curriculum:
        for i in student_obj.curriculum:
            print(i.curriculum_name, i.curriculum_teacher, i.curriculum_cost)
    else:
        print("课表为空")
    print("已上课表信息：")
    if student_obj.study:
        for i in student_obj.study:
            print(i.curriculum_name, str(student_obj.study[i]) + "次")
        pass
    else:
        print("已上课表为空")


def study_curriculum(student_obj):
    for i, item in enumerate(student_obj.curriculum, 1):
        print(i, item.curriculum_name, item.curriculum_teacher, item.curriculum_cost)
    while True:
        inp = input("输入上课序号:(q退出)")
        if inp == "q":
            break
        else:
            if student_obj.curriculum_study(student_obj.curriculum[int(inp) - 1]):
                print("上课成功")
                continue
            else:
                print("还没选课")
                continue
    pickle.dump(student_obj, open(os.path.join(settings.Student_dir, student_obj.username), "wb"))


def select_curriculum(student_obj):
    print("所有课程")
    curriculum_obj = pickle.load(open(settings.Curriculum_dir, "rb"))
    for i, item in enumerate(curriculum_obj, 1):
        print(str(i) + ":", item.curriculum_name, item.curriculum_cost, item.curriculum_teacher)
    while True:
        inp = input("请输入选课序号：(q退出)")
        if inp == "q":
            break
        else:
            select_curriculum_obj = curriculum_obj[int(inp) - 1]
            if student_obj.select_curriculum(select_curriculum_obj):
                print("选课成功")
                continue
            else:
                print("已有课程，不用在选")
    pickle.dump(student_obj, open(os.path.join(settings.Student_dir, student_obj.username), "wb"))


def main():
    inp = input("学生 1、登录。2、注册(任意推出)\n>>>")
    user = input("账号：")
    pwd = input("密码：")
    if inp == "1":
        login(user, pwd)
    elif inp == "2":
        register(user, pwd)
    else:
        pass


if __name__ == "__main__":
    main()
