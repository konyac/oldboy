#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
from backend import commons
from backend.utils import message

class LoginHandler(tornado.web.RequestHandler):
    # def get(self):
    #     self.render("cors.html", )

    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        pwd = self.get_argument("pwd", None)
        # print(USER_LIST, username)
        # self.render("cors.html", user_list=USER_LIST,news_list=NEWS_LIST)  # 重点坑渲染的时候带参数

class SendCodeHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        email = self.get_argument('em',None)
        print(email)
        if email:
            code = commons.generate_verification_code()
            message.send_email([email,],code)





