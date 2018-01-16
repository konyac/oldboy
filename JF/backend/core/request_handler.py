#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from JF.session.session import SessionFactory


class BaseRequestHandler(tornado.web.RequestHandler):

    def initialize(self):

        self.session = SessionFactory.get_session_obj(self)
