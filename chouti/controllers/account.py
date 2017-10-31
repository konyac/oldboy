#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
from chouti.backend import commons
from chouti.backend.utils import message
from chouti.models import chouti_orm
import datetime, json

from chouti.backend.utils import session


class LoginHandler(session.Base):
    # def get(self):
    #     self.render("cors.html", )

    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        pwd = self.get_argument("pwd", None)
        # print(USER_LIST, username)
        # self.render("cors.html", user_list=USER_LIST,news_list=NEWS_LIST)  # 重点坑渲染的时候带参数


class RegisterHandler(session.Base):
    # 获取用户输入的所有内容
    # 拿到code跟发送的code匹配
    # 根据邮箱匹配
    # 成功，
    def post(self, *args, **kwargs):
        ret = {'status': True, 'data': '', "error": ''}

        code = self.get_argument('code')
        email = self.get_argument('id')
        username = self.get_argument('username')
        password = self.get_argument('idpwd')
        conn = chouti_orm.session()
        is_code = conn.query(chouti_orm.SendCode).filter(chouti_orm.SendCode.code == code,
                                                         chouti_orm.SendCode.email == email).first()
        if is_code:
            obj = chouti_orm.UserInfo(username=username, email=email, password=password, status=1,ctime=datetime.datetime.now())
            conn.add(obj)
            conn.commit()
            self.session['is_login'] = True
            self.session['username'] = username
            self.session['email'] = email
            self.write(json.dumps(ret))
        else:
            ret.status = False
            ret.error = '邮箱验证码错误'
            self.write(json.dumps(ret))


class SendCodeHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        ret = {'status': True, 'data': '', "error": ''}
        email = self.get_argument('em', None)
        print(email)
        if email:
            code = commons.generate_verification_code()
            message.send_email([email, ], code)
            conn = chouti_orm.session()
            obj = chouti_orm.SendCode(email=email, code=code, stime=datetime.datetime.now())
            conn.add(obj)
            conn.commit()
        else:
            ret['status'] = False
            ret['error'] = '邮箱格式错误'
        self.write(json.dumps(ret))
