#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)#链接池

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar',ex=10)
print(str(r.get('foo'),encoding='utf-8'))
