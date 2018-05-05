#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from zhonghang.backend.form.forms import BaseForm
from zhonghang.backend.form.fields import StringField


class LoginForm(BaseForm):

    def __init__(self):
        self.user = StringField()
        self.pwd = StringField()
        super(LoginForm, self).__init__()