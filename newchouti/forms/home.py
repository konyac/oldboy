#!/usr/bin/env python
# -*- coding:utf-8 -*-

from newchouti.backend.form.forms import BaseForm
from newchouti.backend.form.fields import StringField
from newchouti.backend.form.fields import IntegerField
from newchouti.backend.form.fields import EmailField


class IndexForm(BaseForm):

    def __init__(self):
        self.title = StringField()
        self.content = StringField(required=False)
        self.url = StringField(required=False)
        self.news_type_id = IntegerField()

        super(IndexForm, self).__init__()


class CommentForm(BaseForm):

    def __init__(self):
        self.content = StringField()
        self.news_id = IntegerField()
        self.reply_id = IntegerField(required=False)

        super(CommentForm, self).__init__()
