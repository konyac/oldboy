#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from urls import URLS

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 获取用户URL
    url = environ['PATH_INFO']
    if url in URLS.keys():
        func_name = URLS[url]
        ret = func_name()
    else:
        ret = "404"
    return ret

if __name__ == "__main__":
    httpd = make_server('', 8000, RunServer)
    httpd.serve_forever()

