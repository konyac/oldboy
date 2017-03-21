#!/usr/bin/env python
# -*- coding:utf-8 -*-
import zipfile
z=zipfile.ZipFile("test2.tar.gz","r")
# z.write("db")
# z.close()
z.extractall()
z.close()
import subprocess