#!/usr/bin/env python
# -*- coding:utf-8 -*-
from newchouti import config
from hashlib import sha1
import os
import time
import memcache, json, redis

# 创建随机字符串
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
        # 检测客户端cookie是否有随机字符串。
        if client_random_str and client_random_str in CacheSession.session_container:  # 有且是我设定的
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


pool = redis.ConnectionPool(host='127.0.0.1', port=6379)  # 链接池
r = redis.Redis(connection_pool=pool)


class RedisSession:
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        # 检测客户端cookie是否有随机字符串。
        if client_random_str and r.exists(self.random_str):  # 有且是我设定的
            self.random_str = client_random_str  # 正确的随机字符串
        else:
            self.random_str = create_session_id()
            # CacheSession.session_container[self.random_str] = {}
            r.hset(self.random_str, None, None)

        r.expire(self.random_str, config.SESSION_EXPIRES)  # 每次都要设置延时，实时更新过期时间

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(RedisSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        result = r.hget(self.random_str, key)
        # return result.decode("utf-8")
        if result:
            return str(result, encoding="utf-8")
        else:
            return result

    def __setitem__(self, key, value):
        if type(value) == dict:
            r.hset(self.random_str,key,json.dumps(value))
        else:
            r.hset(self.random_str, key, value)

    def __delitem__(self, key):
        r.hdel(self.random_str, key)


conn = memcache.Client(['127.0.0.1:11211'], debug=True)


class MemcachedSession:
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        # 检测客户端cookie是否有随机字符串。
        if client_random_str and conn.get(client_random_str):  # 有且是我设定的
            self.random_str = client_random_str  # 正确的随机字符串
        else:
            self.random_str = create_session_id()
            # CacheSession.session_container[self.random_str] = {}
            conn.set(self.random_str, json.dumps({}), config.SESSION_EXPIRES)

        conn.set(self.random_str, conn.get(self.random_str), config.SESSION_EXPIRES)  # 每次都要设置延时，实时更新过期时间

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(MemcachedSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret_str = conn.get(self.random_str)
        ret_dict = json.loads(ret_str)
        result = ret_dict.get(key, None)

        # ret = CacheSession.session_container[self.random_str].get(key, None)
        return result

    def __setitem__(self, key, value):
        ret = conn.get(self.random_str)
        ret_dict = json.loads(ret)  # 取到mc中的字典
        ret_dict[key] = value  # 加入进入
        conn.set(self.random_str, json.dumps(ret_dict), config.SESSION_EXPIRES)  # 设置到mc中
        # CacheSession.session_container[self.random_str][key] = value

    def __delitem__(self, key):
        # if key in CacheSession.session_container[self.random_str]:
        #     del CacheSession.session_container[self.random_str][key]
        ret_str = conn.get(self.random_str)
        ret_dict = json.loads(ret_str)
        del ret_dict[key]  # 删除
        conn.set(self.random_str, json.dumps(ret_dict), config.SESSION_EXPIRES)  # 删除完之后再设置到mc中
