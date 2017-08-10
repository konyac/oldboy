#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import json

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        dic = {"status":True,"message":""}
        username = self.get_argument("username")
        password = self.get_argument("password")
        if username=="alex" and password=="123":
            pass
        else:
            dic["status"]=False
            dic["message"]="用户名或密码错误"
        # print(username,password)
        dic_str = json.dumps(dic)
        self.write(dic_str)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        self.render("index.html")

settings = {
    "template_path": "views",
    "static_path":"statics",
    "cookie_secret": "alex"  # cookie加密要添加的
}

app = tornado.web.Application([("/index", IndexHandler),
                               ("/login", LoginHandler)],**settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
