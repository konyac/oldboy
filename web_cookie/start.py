#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie("value","2222")
        print(self.cookies)
        self.render("index.html")
settings = {
    "template_path": "views",  # 模板路径
    "static_path": "static",  # 静态文件

}

# 路由映射，路由系统
# app = tornado.web.Application([("/index/(?P<page>\d*)", home.IndexHandler)], **settings)
app = tornado.web.Application([("/index", IndexHandler)], **settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
