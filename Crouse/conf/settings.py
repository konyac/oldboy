#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
设置每个对象保存的文件路径
"""
import os,sys
BaseDir = os.path.dirname(os.path.dirname(__file__))
teacher_db_dir = os.path.join(BaseDir,"db","teacher_list")
course_db_dir = os.path.join(BaseDir,"db","course_list")
Base_admin_dir = os.path.join(BaseDir,"db","admin")
Base_studens_dir = os.path.join(BaseDir,"db","students")
