#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pickle, os, time

from conf import settings

class Teacher:
    """
    封装老师的相关信息
    """

    def __init__(self, name, age, admin):
        self.name = name
        self.age = age
        self.__assets = 0
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin  # 封装的admin对象，里面有用户名 密码

    def gain(self, cost):
        """
        增加资产
        :param cost: 增加的数量
        :return:
        """
        self.__assets += cost

    def decrease(self, cost):
        """
        减少资产
        :param cost: 减少的数量
        :return:
        """
        self.__assets += cost


class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def login(self, user, pwd):
        """
        管理员登陆
        :param user:
        :param pwd:
        :return:
        """
        if self.username == user and self.password == pwd:
            return True
        else:
            return False

    def register(self, user, pwd):
        """
        管理员注册
        :param user:
        :param pwd:
        :return:
        """
        self.username = user
        self.password = pwd

        path = os.path.join(settings.Base_admin_dir,self.username)

        pickle.dump(self, open(path, 'xb'))  # 将 对象一起dump进去。 亮点。。  笨方法是在主函数里面dump


class Course:
    """
    课程相关信息
    """
    def __init__(self, course_name, cost, teacher_obj, admin):
        self.course_name = course_name
        self.cost = cost
        self.teacher = teacher_obj
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin


class Student:
    """
    学生相关信息
    """
    def __init__(self):
        self.username = None
        self.password = None

        self.course_list = []
        self.study_dict = {}

    def select_course(self, course_obj):
        """
        学生选课
        :param course_obj:
        :return:
        """
        self.course_list.append(course_obj)

    def study(self, course_obj):
        """
        学生上课
        :param course_obj:
        :return:
        """
        class_result = course_obj.have_lesson()

        if course_obj in self.study_dict.keys():

            self.study_dict[course_obj].append(class_result)
        else:
            self.study_dict[course_obj] = [class_result, ]

    def login(self, user, pwd):
        """
        学生登陆
        :param user:
        :param pwd:
        :return:
        """
        if self.username == user and self.password == pwd:
            return True
        else:
            return False

    def register(self, user, pwd):
        """
        学生注册
        :param user:
        :param pwd:
        :return:
        """
        self.username = user
        self.password = pwd

        path = os.path.join(settings.Base_studens_dir,self.username)

        pickle.dump(self, open(path, 'xb'))




