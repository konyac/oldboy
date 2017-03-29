#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pickle, os, time, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.models import *
from conf import settings

def create_course(admin_obj):#创建课程，需要管理员参数
    teacher_list = pickle.load(open(settings.teacher_db_dir,"rb"))#获取老师对象
    for num,item in enumerate(teacher_list,1):#序列化，老师列表
        print(num,item.name,item.age,item.create_time,item.create_admin.username)
    course_list = []#临时选课表
    while True:
        name = input("请输入课程名(q退出)：")
        if name == "q":
            break
        cost = input("请输入课时费：")
        num =  input("选择老师（序号）：")
        obj = Course(name,cost,teacher_list[int(num) - 1],admin_obj)#创建一个课程对象
        course_list.append(obj)#加入到临时课标中
    if os.path.exists(settings.course_db_dir):#课程表保存文件是否存在
        exists_list = pickle.load(open(settings.course_db_dir,"rb"))#取出已存在的列表
        course_list.extend(exists_list)#将已存在的加入到新课表后面
    pickle.dump(course_list,open(settings.course_db_dir,"wb"))#将新课表写入课表文件中
def create_teacher(admin_obj):
    teacher_list = []
    while True:
        teacher_name = input("输入老师姓名（q退出)：")
        if teacher_name == 'q':
            break
        teacher_age = input("输入老师年龄：")
        obj  = Teacher(teacher_name,teacher_age,admin_obj)
        teacher_list.append(obj)
    if os.path.exists(settings.teacher_db_dir):
        exists_list = pickle.load(open(settings.teacher_db_dir,"rb"))
        teacher_list.extend(exists_list)
    pickle.dump(teacher_list,open(settings.teacher_db_dir,"wb"))
def login(user, pwd):
    if os.path.exists(os.path.join(settings.Base_admin_dir,user)):
        admin_obj = pickle.load(open(os.path.join(settings.Base_admin_dir,user), "rb"))
        if admin_obj.login(user, pwd):
            print("登陆成功")
            while True:
                sel = input("1、创建老师 2、创建课程  (随意输入退出)")
                if sel == "1":
                    create_teacher(admin_obj)
                elif sel == "2":
                    create_course(admin_obj)
                else:
                    break
        else:
            return 1
    else:
        return 0


def register(user, pwd):
    admin_obj = Admin()
    admin_obj.register(user, pwd)


def main():
    inp = input("管理员1、 登陆  2 、注册\n>>>")
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
