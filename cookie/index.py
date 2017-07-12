#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import time


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html", status_text="")

    def post(self, *args, **kwargs):
        username = self.get_argument("username")
        password = self.get_argument("pwd")
        if username == "alex" and password == "123":
            r = time.time()  # 获取当前时间戳,
            r = r + 10  # 使时间戳在当前时间下+10秒。
            # self.set_cookie("auth","1")设置普通cookie。,cookie的value必须是字符串
            self.set_secure_cookie("auth", "1", expires=r)  # expires 过期时间。expires_days 过期天数
            self.redirect("/manager")
        else:
            self.render("login.html", status_text="登陆失败")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        self.render("index.html")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie("auth", "0")
        self.redirect("/login")


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        co = self.get_cookie("auth")
        if co == "1":
            self.render("manager.html")
        else:
            self.redirect("/login")

    def post(self, *args, **kwargs):
        self.render("manager.html")


settings = {
    "template_path": "views",#模板路径
    "static_path":"statics",
    "cookie_secret": "alex"  # cookie加密要添加的
}
# 路由映射
app = tornado.web.Application([("/index", IndexHandler),
                               ("/login", LoginHandler),
                               ("/manager", ManagerHandler),
                               ("/logout", LogoutHandler)], **settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
