#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
from JF.controllers import account,home


class IndexHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        pass

class spHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("home/sp.html")

    def post(self, *args, **kwargs):
        pass

class resetHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("home/reset.html")

    def post(self, *args, **kwargs):
        pass

class adminHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("admin/admin.html")

    def post(self, *args, **kwargs):
        pass

class adminspHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("admin/adminsp.html")

    def post(self, *args, **kwargs):
        pass


class staffHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("admin/staff.html")

    def post(self, *args, **kwargs):
        pass

class LoginHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        pass

class setHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("admin/set.html")

    def post(self, *args, **kwargs):
        pass

settings = {
    "template_path": "views",  # 模板路径的配置
    "static_path": "static",  # 静态文件的位置
    # 'static_url_prefix': '/statics/',#静态文件地址别名

}
# 路由映射，路由系统
application = tornado.web.Application([(r"/index", home.IndexHandler),
                                       (r"/login", account.LoginHandler),
                                       (r"/userinfo", home.UserInfoHandler),
                                       (r"/reset", resetHandler),
                                       (r"/sp", spHandler),
                                       (r"/admin", adminHandler),
                                       (r"/adminsp", adminspHandler),
                                       (r"/staff", staffHandler),
                                       (r"/set", setHandler),

                                       ], **settings)  # 创建一个对象

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
