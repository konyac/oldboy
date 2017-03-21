#!/usr/bin/env python
# -*- coding:utf-8 -*-
import shutil,os,sys
# shutil.copyfileobj(open("db","r"),open("db2","a"))
# shutil.copyfile("db2","db3")
# shutil.copytree(os.path.dirname(__file__),os.path.dirname(os.path.dirname(__file__))+"/copy",ignore=shutil.ignore_patterns('*.py',"*.pyc"))
# shutil.rmtree(os.path.dirname(__file__)+"/copy")
shutil.make_archive(os.path.dirname(__file__)+"/back_db3","gztar",root_dir=os.path.dirname(__file__)+"/db3")