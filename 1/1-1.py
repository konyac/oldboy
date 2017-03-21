#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
i=0
while i <= 10:
    time.sleep(1)
    i+=1
    if i == 7:
        continue
    print i
print("end")