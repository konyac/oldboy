#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pickle, time, os


class Teacher:
    def __init__(self, name, age, admin):
        self.name = name
        self.age = age
        self.__assets = 0
        self.admin = admin
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
