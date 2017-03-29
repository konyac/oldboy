#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle,os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lib.models import  *
from conf import  settings

def course_info(student_obj):
    for item in student_obj.course_list:
        print(item.course_name, item.teacher.name)


def select_course(student_obj):
    course_list = pickle.load(open(settings.course_db_dir,"rb"))
    for num,item in enumerate(course_list,1):
        print(num,item.course_name,item.cost,item.teacher.name)

    while True:
        num = input("请选择课程序号(q 离开)：")
        if num == "q":
            break
        selected_course_obj = course_list[int(num) - 1]
        if selected_course_obj not in student_obj.course_list:
            student_obj.course_list.append(selected_course_obj)
    pickle.dump(student_obj,open(os.path.join(settings.Base_studens_dir,student_obj.username),"wb"))
def login(user,pwd):
    if os.path.exists(os.path.join(settings.Base_studens_dir,user)):
        student_obj = pickle.load(open(os.path.join(settings.Base_studens_dir,user),"rb"))
        if student_obj.login(user,pwd):
            while True:
                inp = input("1. 选课 2.上课 3.查看课程信息 (其他退出)\n>>>")
                if inp == "1":
                    select_course(student_obj)
                    continue
                elif inp == "2":
                    pass
                elif inp == "3":
                    course_info(student_obj)
                    continue
                else:
                    break

        else:
            return 1
    else:
        return 0

def register(user,pwd):
    obj = Student()
    obj.register(user,pwd)

def main():
    inp = input("学生1、 登陆  2 、注册\n>>>")
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    if inp == "1":
        ret = login(user, pwd)
        if ret:
            print("登陆失败")
        elif ret == 0:
            print("用户不存在")
    elif inp == "2":
        register(user, pwd)

if __name__ == '__main__':
    main()