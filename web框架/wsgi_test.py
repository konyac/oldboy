#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from wsgiref.simple_server import make_server


def Run(environ, start_response):
    # wsgi帮我们把所有的请求处理完了，处理完之后放到environ 和start_response参数里
    # 请求发来的内容都封装到这里
    start_response("200 OK", [("Content-Type", "text/html")])
    return "<h>hello stop</h>"


if __name__ == "__main__":
    httpd = make_server("", 8000, Run)
    print("Serving HTTP on port 8000")
    httpd.serve_forever()
