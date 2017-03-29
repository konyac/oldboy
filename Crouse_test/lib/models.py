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

    def Register(self, name, pwd):
        self.username = name
        self.password = pwd
        path = os.path.join(settings.Base_admin_dir, self.username)
        if os.path.exists(path):
            return False
        else:

            pickle.dump(self, open(path, 'xb'))  # xb如果没有就新建一个
            return True

    def Login(self, name, pwd):
        if name == self.username and pwd == self.password:
            return True
        else:
            return False


class Crouse:
    def __init__(self, name, cost, teacher, admin):
        self.crouse_name = name
        self.crouse_teacher = teacher
        self.crouse_cost = cost
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin.username


class Teacher:
    def __init__(self, name, age, admin):
        self.teacher_name = name
        self.teacher_age = age
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin.username
