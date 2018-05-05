#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from zhonghang.backend.core.request_handler import BaseRequestHandler
from newchouti.backend.utils.pager import Pagination
from zhonghang.models import zhonghang_orm as ORM
from zhonghang.backend.utils import response
from zhonghang.forms import account
from sqlalchemy import and_, or_
import datetime, json, io
from zhonghang.backend.utils import decrator


class LoginHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.render('manager/login1.html')

    def post(self, *args, **kwargs):
        rep = response.BaseResponse()
        form = account.LoginForm()

        if form.valid(self):
            conn = ORM.session()
            obj = conn.query(ORM.Admin,ORM.Staff.name).filter(
                or_(
                    and_(ORM.Admin.username == form._value_dict['user'],
                         ORM.Admin.password == form._value_dict['pwd']),
                    and_(ORM.Staff.tel == form._value_dict['user'],
                         ORM.Staff.password == form._value_dict['pwd']),

                )).first()
            if not obj:
                rep.message = {'user': '用户名或密码错误'}
                self.write(json.dumps(rep.__dict__))
                return
            self.session['is_login'] = True
            self.session['user_info'] = obj.__dict__
            rep.status = True
        else:
            rep.message = form._error_dict
            print(form._error_dict)
        print(rep.__dict__)
        self.write(json.dumps(rep.__dict__))


class StaffHandler(BaseRequestHandler):

    def get(self, page=1):
        conn = ORM.session()
        all_count = conn.query(ORM.Record).count()
        obj = Pagination(page, all_count)
        result = conn.query(ORM.Record.nid,
                            ORM.Customer.name,
                            ORM.S_Bank.bank_name,
                            ORM.Customer.account,
                            ORM.Record.main_account,
                            ORM.Record.linkman,
                            ORM.Record.linkman_id,
                            ORM.Record.linkman_tel,
                            ORM.Status.status_name,
                            ).join(ORM.Customer, isouter=True).join(ORM.Status, isouter=True)[obj.start:10]

        str_page = obj.string_pager('/index/')
        print(result, str_page)
        self.render('manager/staff.html', str_page=str_page)


class ManagerHandler(BaseRequestHandler):
    # @decrator.auth_login_redirect
    def get(self, page=1):
        conn = ORM.session()
        all_count = conn.query(ORM.Record).count()
        obj = Pagination(page, all_count)
        result = conn.query(ORM.Record.nid,
                            ORM.Customer.name,
                            ORM.S_Bank.bank_name,
                            ORM.Customer.account,
                            ORM.Record.main_account,
                            ORM.Record.linkman,
                            ORM.Record.linkman_id,
                            ORM.Record.linkman_tel,
                            ORM.Status.status_name,
                            ).join(ORM.Customer, isouter=True).join(ORM.Status, isouter=True)[obj.start:10]

        str_page = obj.string_pager('/index/')
        print(result, str_page)
        self.render('manager/manager1.html', str_page=str_page)


class ResetHandler(BaseRequestHandler):
    def get(self):
        print(self.session.session_container)

        self.render('manager/reset.html')
