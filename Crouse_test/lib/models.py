#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle, os, time
from conf import settings


class Admin:
    """
    管理员类，注册、登陆。
    """

    def __init__(self):
        self.username = None
        self.password = None

    def register(self, name, pwd):
        self.username = name
        self.password = pwd
        path = os.path.join(settings.Base_admin_dir, self.username)
        if os.path.exists(path):
            return False
        else:

            pickle.dump(self, open(path, 'xb'))  # xb如果没有就新建一个
            return True

    def login(self, name, pwd):
        if name == self.username and pwd == self.password:
            return True
        else:
            return False


class Student:
    """
    管理员类，注册、登陆。
    """

    def __init__(self):
        self.username = None
        self.password = None

        self.curriculum = []
        self.study = {}

    def select_curriculum(self, curriculum_obj):
        if curriculum_obj in self.curriculum:
            return False
        else:
            self.curriculum.append(curriculum_obj)
            return True

    def curriculum_study(self, curriculum):
        if curriculum not in self.curriculum:
            return False
        elif curriculum not in self.study:
            self.study[curriculum] = 1
            return True
        else:
            self.study[curriculum] += 1
            return True


    def register(self, name, pwd):
        self.username = name
        self.password = pwd
        path = os.path.join(settings.Student_dir, self.username)
        if os.path.exists(path):
            return False
        else:

            pickle.dump(self, open(path, 'xb'))  # xb如果没有就新建一个
            return True

    def login(self, name, pwd):
        if name == self.username and pwd == self.password:
            return True
        else:
            return False


class Curriculum:
    def __init__(self, name, cost, teacher, admin):
        self.curriculum_name = name
        self.curriculum_teacher = teacher
        self.curriculum_cost = cost
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin.username


class Teacher:
    def __init__(self, name, age, admin):
        self.teacher_name = name
        self.teacher_age = age
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin.username
