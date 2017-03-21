#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import sys
# for i in sys.path:
#     print(i)
import time
import sys
for i in range(30):
   sys.stdout.write('\r')
   sys.stdout.write("%s%%|%s" % (int(i/30*100),int(i/30*100)*"*"))
   sys.stdout.flush()
   time.sleep(0.3)