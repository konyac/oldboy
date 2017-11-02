#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
每种操作要做的验证项目
'''
from form_check.form.forms import BaseForm
from form_check.form.fields import StringField
from form_check.form.fields import IntegerField
from form_check.form.fields import EmailField


class SendMsgForm(BaseForm):

    def __init__(self):
        self.email = EmailField(custom_error_dict={'required': '注册邮箱不能为空.', 'valid': '注册邮箱格式错误.'})#创建实例对象

        super(SendMsgForm, self).__init__()

class RegisterForm(BaseForm):

    def __init__(self):
        self.username = StringField()
        self.email = EmailField(custom_error_dict={'required': '注册邮箱不能为空.', 'valid': '注册邮箱格式错误.'})
        self.password = StringField()
        self.email_code = StringField()

        super(RegisterForm, self).__init__()

class LoginForm(BaseForm):

    def __init__(self):
        self.user = StringField()
        self.pwd = StringField()
        self.code = StringField()

        super(LoginForm, self).__init__()