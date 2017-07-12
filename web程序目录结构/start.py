#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
from controller import home


settings = {
    "template_path": "views",  # 模板路径
    "static_path": "statics",  # 静态文件
    "cookie_secret": "alex"  # cookie加密要添加的
}

# 路由映射，路由系统
app = tornado.web.Application([("/index/(?P<page>\d*)", home.IndexHandler)], **settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
