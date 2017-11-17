#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
from newchouti.backend import commons
from newchouti.backend.utils import message
from newchouti.models import chouti_orm as ORM
import datetime, json, io
from newchouti.forms import account
from newchouti.backend.core import request_handler
from sqlalchemy import and_, or_
from newchouti.backend.utils import response, check_code,message
from newchouti.backend.core.request_handler import BaseRequestHandler


class CheckCodeHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        stream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(stream, "png")
        self.session["CheckCode"] = code
        self.write(stream.getvalue())


class LoginHandler(BaseRequestHandler):
    # def get(self):
    #     self.render("cors.html", )


    def post(self, *args, **kwargs):
        rep = response.BaseResponse()
        form = account.LoginForm()
        # print(USER_LIST, username)
        # self.render("cors.html", user_list=USER_LIST,news_list=NEWS_LIST)  # 重点坑渲染的时候带参数

        if form.valid(self):
            print(form._value_dict, self.session['CheckCode'])
            if form._value_dict['code'].lower() != self.session['CheckCode'].lower():
                rep.message = {'code': '验证码错误'}
                self.write(json.dumps(rep.__dict__))
                return
            conn = ORM.session()
            obj = conn.query(ORM.UserInfo).filter(
                or_(
                    and_(ORM.UserInfo.email == form._value_dict['user'],
                         ORM.UserInfo.password == form._value_dict['pwd']),
                    and_(ORM.UserInfo.username == form._value_dict['user'],
                         ORM.UserInfo.password == form._value_dict['pwd'])
                )
            ).first()
            if not obj:
                rep.message = {'user': '用户名邮箱或密码错误'}
                self.write(json.dumps(rep.__dict__))
                return
            self.session['is_login'] = True
            self.session['user_info'] = obj.__dict__
            rep.status = True
        else:
            rep.message = form._error_dict

        self.write(json.dumps(rep.__dict__))


class RegisterHandler(BaseRequestHandler):
    # 获取用户输入的所有内容
    # 拿到code跟发送的code匹配
    # 根据邮箱匹配
    # 成功，
    def post(self, *args, **kwargs):
        rep = response.BaseResponse()
        form = account.RegisterForm()
        if form.valid(self):
            current_date = datetime.datetime.now()
            limit_day = current_date - datetime.timedelta(minutes=1)
            conn = ORM.session()
            is_valid_code = conn.query(ORM.SendCode).filter(ORM.SendCode.email == form._value_dict['email'],
                                                            ORM.SendCode.code == form._value_dict['email_code'],
                                                            ORM.SendCode.ctime > limit_day).count()
            if not is_valid_code:
                rep.message['email_code'] = '邮箱验证码不正确或过期'
                self.write(json.dumps(rep.__dict__))
                return
            has_exists_email = conn.query(ORM.UserInfo).filter(ORM.UserInfo.email == form._value_dict['email']).count()
            if has_exists_email:
                rep.message['email'] = '邮箱已经存在'
                self.write(json.dumps(rep.__dict__))
                return
            has_exists_username = conn.query(ORM.UserInfo).filter(
                ORM.UserInfo.username == form._value_dict['username']).count()
            if has_exists_username:
                rep.message['email'] = '用户名已经存在'
                self.write(json.dumps(rep.__dict__))
                return
            form._value_dict['ctime'] = current_date
            form._value_dict.pop('email_code')
            # 优化下插入的数据。去掉emai_code 加入创建时间
            obj = ORM.UserInfo(**form._value_dict)#传了个字典，和= 一样的。

            conn.add(obj)
            conn.flush()
            conn.refresh(obj)

            user_info_dict = {'nid': obj.nid, 'email': obj.email, 'username': obj.username}

            conn.query(ORM.SendCode).filter_by(email=form._value_dict['email']).delete()#删掉发送表中的记录
            conn.commit()
            conn.close()

            self.session['is_login'] = True
            self.session['user_info'] = user_info_dict#把用户信息放到session中
            rep.status = True

        else:
            rep.message = form._error_dict

        self.write(json.dumps(rep.__dict__))


class SendCodeHandler(BaseRequestHandler):
    def post(self, *args, **kwargs):
        rep = response.BaseResponse()
        form = account.SendMsgForm()
        # print(email)
        if form.valid(self):
            email = form._value_dict['email']
            conn = ORM.session()

            has_exists_email = conn.query(ORM.UserInfo).filter(ORM.UserInfo.email == form._value_dict['email']).count()
            if has_exists_email:
                rep.summary = "此邮箱已经被注册"
                self.write(json.dumps(rep.__dict__))
                return
            current_date = datetime.datetime.now()
            code = commons.generate_verification_code()
            # print(code)

            count = conn.query(ORM.SendCode).filter_by(**form._value_dict).count()
            if not count:
                insert = ORM.SendCode(code=code,
                                      email=email,
                                      ctime=current_date)
                conn.add(insert)
                conn.commit()
                rep.status = True
                #首次注册
                message.send_email([email,],code)
            else:
                limit_day = current_date - datetime.timedelta(hours=1)
                times = conn.query(ORM.SendCode).filter(ORM.SendCode.email == email,
                                                        ORM.SendCode.ctime > limit_day,
                                                        ORM.SendCode.times >= 10,
                                                        ).count()
                if times:
                    rep.summary = "'已经超过今日最大次数（1小时后重试）'"
                else:
                    unfreeze = conn.query(ORM.SendCode).filter(ORM.SendCode.email == email,
                                                               ORM.SendCode.ctime < limit_day).count()
                    if unfreeze:
                        conn.query(ORM.SendCode).filter_by(email=email).update({"times": 0})

                    conn.query(ORM.SendCode).filter_by(email=email).update({"times": ORM.SendCode.times + 1,
                                                                            "code": code,
                                                                            "ctime": current_date},
                                                                           synchronize_session="evaluate")
                    conn.commit()
                    rep.status = True
                    # 再次注册
                    message.send_email([email,],code)
            conn.close()
        else:
            rep.summary = form._error_dict['email']
        self.write(json.dumps(rep.__dict__))
