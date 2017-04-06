#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess
# ret = subprocess.call("ipconfig")
# ret=subprocess.check_call(["ipconfig"])
# bin=bytes(ret,encoding="gbk")
# print(str(bin,encoding="utf-8"))
# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out=subprocess.check_output("dir",shell=True)
ret=str(out,encoding="gbk")
print(ret)