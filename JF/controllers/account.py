#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
from JF.backend import commons
from JF.backend.utils import message
from JF.models import jifen_orm as ORM
import datetime, json, io
from JF.forms import account
from sqlalchemy import and_
from JF.backend.utils import response, check_code, message
from JF.backend.core.request_handler import BaseRequestHandler


class LoginHandler(BaseRequestHandler):
    def get(self):
        self.render("login.html", )

    def post(self, *args, **kwargs):
        rep = response.BaseResponse()
        form = account.LoginForm()

        if form.valid(self):
            conn = ORM.session()
            obj = conn.query(ORM.UserInfo).filter(and_(ORM.UserInfo.username == form._value_dict['user'],
                                                       ORM.UserInfo.password == form._value_dict['pwd'])
                                                  ).first()
            if not obj:
                rep.message = {'user': '用户名或密码错误'}
                self.write(json.dumps(rep.__dict__))
                return
            self.session['is_login'] = True
            self.session['user_info'] = obj.__dict__
            rep.status = True
        else:
            rep.message = form._error_dict

        self.write(json.dumps(rep.__dict__))
