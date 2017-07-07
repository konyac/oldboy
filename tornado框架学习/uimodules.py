#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from tornado.web import UIModule


class custom(UIModule):

    def render(self, *args, **kwargs):
        return "123"
