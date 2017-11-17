#!/usr/bin/env python
# -*- coding:utf-8 -*-
from newchouti import config
from hashlib import sha1
import os
import time

#创建随机字符串
create_session_id = lambda: sha1(bytes('%s%s' % (os.urandom(16), time.time()), encoding='utf-8')).hexdigest()

class SessionFactory:


    @staticmethod
    def get_session_obj(handler):
        """
        静态方法。返回不同的session类。
        :param handler: self
        :return: 
        """
        obj = None

        if config.SESSION_TYPE == "cache":
            obj = CacheSession(handler)
        elif config.SESSION_TYPE == "memcached_l":
            obj = MemcachedSession(handler)
        elif config.SESSION_TYPE == "redis":
            obj = RedisSession(handler)
        return obj


class CacheSession:
    session_container = {}
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        #检测客户端cookie是否有随机字符串。
        if client_random_str and client_random_str in CacheSession.session_container:#有且是我设定的
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            CacheSession.session_container[self.random_str] = {}

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(CacheSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret = CacheSession.session_container[self.random_str].get(key, None)
        return ret

    def __setitem__(self, key, value):
        CacheSession.session_container[self.random_str][key] = value

    def __delitem__(self, key):
        if key in CacheSession.session_container[self.random_str]:
            del CacheSession.session_container[self.random_str][key]


class RedisSession:
    def __init__(self, handler):
        pass


class MemcachedSession:
    def __init__(self, handler):
        pass