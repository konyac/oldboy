#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web

LIST_INFO = [
    {
        "username": "alex",
        "email": "cjx222@163.com"
    },
]

class IndexHandler(tornado.web.RequestHandler):
    def get(self, page):
        # if not page:#如果不填page的情况
        #     page =1
        try:
            page = int(page)#page默认接收到的是个字符串，转化成数字型，
        except:#转化失败，填入了字符型或者其他
            page = 1
        if page<1:
            page=1
        # print(page)
        #每页显示5条数据
        #page是当前页
        #第一页显示0:5 LIST_INFO[0:5],切片是包含前面不含后面
        #第二页显示5:10 LIST_INFO[5:10]
        #start (page-1)*5
        #end page*5
        start = (page-1)*5 #显示的起始和结束的公式
        end = page*5
        current_list = LIST_INFO[start:end]
        self.render("home/index.html", list_info=current_list)#home前面不加/

    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        email = self.get_argument("email", None)
        temp = {"username": username, "email": email}
        LIST_INFO.append(temp)
        self.redirect("/index/")
