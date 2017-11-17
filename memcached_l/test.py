#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import memcache

mc = memcache.Client(['192.168.1.115:11211'], debug=True)
# mc.set("foo", "bar",10)
ret = mc.get('foo')
print(ret)