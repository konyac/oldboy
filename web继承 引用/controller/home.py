#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web

LIST_INFO=[11,22,33]

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("extend/cors.html")


class FuckHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("extend/fuck.html",list_info = LIST_INFO)

class LayoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("master/layout.html")