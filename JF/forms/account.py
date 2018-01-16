#!/usr/bin/env python
# -*- coding:utf-8 -*-

from newchouti.backend.form.forms import BaseForm
from newchouti.backend.form.fields import StringField

class LoginForm(BaseForm):

    def __init__(self):
        self.user = StringField(custom_error_dict={'required':"请填写用户名","valid":"用户名格式错误"})
        self.pwd = StringField(custom_error_dict={'required':"请填写密码","valid":"密码格式错误"})

        super(LoginForm, self).__init__()