#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# from gevent import monkey; monkey.patch_all()
import gevent
import requests

def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = len(resp.text)
    print('%d bytes received from %s.' % (data, url))

gevent.joinall([
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])