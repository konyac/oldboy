#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
from chouti.backend import commons
from chouti.backend.utils import message
from chouti.models import chouti_orm
import datetime, json

from chouti.backend.utils import session
from sqlalchemy import and_, or_


class LoginHandler(session.Base):
    # def get(self):
    #     self.render("cors.html", )

    def post(self, *args, **kwargs):
        ret = {'status': 0, 'data': '', "error": ''}
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        # print(USER_LIST, username)
        # self.render("cors.html", user_list=USER_LIST,news_list=NEWS_LIST)  # 重点坑渲染的时候带参数
        con = chouti_orm.session()
        is_user = con.query(chouti_orm.UserInfo).filter(or_(
            and_(chouti_orm.UserInfo.username == username,
                 chouti_orm.UserInfo.password == password),
            and_(chouti_orm.UserInfo.email == username,
                 chouti_orm.UserInfo.password == password)
        )).first()
        if (is_user):
            self.session['is_login'] = True
            self.session['username'] = is_user.username
            self.session['email'] = is_user.email
            self.write(json.dumps(ret))
        else:
            ret['status'] = 1
            ret['error'] = '用户名或密码错误'
            self.write(json.dumps(ret))


class RegisterHandler(session.Base):
    # 获取用户输入的所有内容
    # 拿到code跟发送的code匹配
    # 根据邮箱匹配
    # 成功，
    def post(self, *args, **kwargs):
        ret = {'status': 0, 'data': '', "error": ''}

        code = self.get_argument('code')
        email = self.get_argument('id')
        username = self.get_argument('username')
        password = self.get_argument('idpwd')
        conn = chouti_orm.session()
        is_code = conn.query(chouti_orm.SendCode).filter(chouti_orm.SendCode.code == code,
                                                         chouti_orm.SendCode.email == email).first()
        if is_code:
            is_user = conn.query(chouti_orm.UserInfo).filter(chouti_orm.UserInfo.username == username).first()
            is_email = conn.query(chouti_orm.UserInfo).filter(chouti_orm.UserInfo.email == email).first()
            if is_user:
                ret['status'] = 2
                ret['error'] = '用户名已存在'
                self.write(json.dumps(ret))
            elif is_email:
                ret["status"] = 3
                ret['error'] = '邮箱已存在'
                self.write(json.dumps(ret))
            elif len(password) < 6:
                ret['status'] = 4
                ret['error'] = '密码格式不对'
                self.write(json.dumps(ret))
            else:
                obj = chouti_orm.UserInfo(username=username, email=email, password=password, status=1,
                                          ctime=datetime.datetime.now())
                conn.add(obj)
                conn.commit()
                self.session['is_login'] = True
                self.session['username'] = username
                self.session['email'] = email
                self.write(json.dumps(ret))
        else:
            ret['status'] = 1
            ret['error'] = '邮箱验证码错误'
            self.write(json.dumps(ret))


class SendCodeHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        ret = {'status': True, 'data': '', "error": ''}
        email = self.get_argument('id', None)
        # print(email)
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
