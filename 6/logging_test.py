#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging

# logging.basicConfig(filename="log.log",
#                     format="%(asctime)s-%(name)s-%(levelname)s -%(module)s:  %(message)s",
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=10
#                     )
# logging.debug("debug")
# logging.error("error")

file1_1=logging.FileHandler("11_1.log","a")
fmt=logging.Formatter