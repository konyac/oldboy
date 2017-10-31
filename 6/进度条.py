#!/usr/bin/env python
# -*- coding:utf-8 -*-
#进度条案例
import time,sys
for i in range(101):
   #显示进度条百分比  #号从1开始 空格从99递减
   hashes = '#' * int(i / 100.0 * 100)
   spaces = ' ' * (100 - len(hashes))
   sys.stdout.write("\r[%s] %s%%" % (hashes + spaces, i))  #必须两个%%才是，因为一个%是取模，python解释器会默认过滤
   sys.stdout.flush() #强制刷新屏幕缓冲区使其一行输出
   time.sleep(0.05)