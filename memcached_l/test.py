#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import memcache

# mc = memcache.Client(['127.0.0.1:11211'], debug=True)
# mc.set("foo", "bar",10)
# ret = mc.get('foo')
# print(ret)

# 10、gets 和 cas
mc = memcache.Client(['127.0.0.1:11211'], debug=True,cache_cas=True)
# mc.set('foo',100)
print(mc.get('foo'))