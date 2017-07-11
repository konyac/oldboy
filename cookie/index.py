#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        self.render("index.html")


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html",status_text = "")

    def post(self, *args, **kwargs):
        username = self.get_argument("username")
        password = self.get_argument("pwd")
        if username == "alex" and password == "123":
            self.set_cookie("auth", "1")
            self.redirect("/manager")
        else:
            self.render("login.html",status_text = "登陆失败")


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
    "template_path": "views"
}

app = tornado.web.Application([("/index", IndexHandler),
                               ("/login", LoginHandler),
                               ("/manager", ManagerHandler),
                               ("/logout", LogoutHandler)], **settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
