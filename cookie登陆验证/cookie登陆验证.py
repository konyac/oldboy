#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.current_user()
        self.render('login.html', **{'status': ''})

    def post(self, *args, **kwargs):
        username = self.get_argument("name", None)
        password = self.get_argument("pwd", None)
        # print(username,password)
        if username == "alex" and password == "123":

            self.set_secure_cookie("login_user", "武藤兰")
            self.redirect("/manager")
        else:
            self.render("login.html", **{"status": "用户名或密码错误"})


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        login_user = self.get_secure_cookie("login_user", None)
        if login_user:
            self.write(login_user)
        else:
            self.redirect("/login")


setting = {
    "template_path": "views",  # 模板路径
    "static_path": "static",  # 静态文件
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
}
application = tornado.web.Application(
    [("/login", LoginHandler),
     ("/manager", ManagerHandler)], **setting
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
