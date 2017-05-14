#!/usr/bin/env python
# -*- coding:utf-8 -*-

class User:
    def __init__(self,username,data):
        self.username = username
        self.storage_limit = data["storage_limit"]
        self.cwd = [""]
        self.used_storage = None
