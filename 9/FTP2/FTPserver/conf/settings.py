#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
BIND_HOST = "127.0.0.1"
BIND_PORT = 9992

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_HOME = "%s\\var\\users" % BASE_DIR

USER_ACCOUNT = {
    "alex":{
        "password":"c4ca4238a0b923820dcc509a6f75849b",
        "storage_limit":2097152,
    },
    "cui":{
        "password":"c4ca4238a0b923820dcc509a6f75849b",
        "storage_limit":2097152,
    },
}