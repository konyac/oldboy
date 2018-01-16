#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=True,cache_cas=True)
ret=mc.gets('foo')
print(ret)
input("...")
mc.cas('foo',88)