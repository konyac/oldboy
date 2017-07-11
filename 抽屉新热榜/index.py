#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop

USER_LIST = {"is_login": None}
NEWS_LIST = [{
    "title": "万科重生：深铁会比华润更积极 因为深铁想从万科得到更多 ",
    "content": "马拉多纳在1986年世界杯夺冠归国后对总统阿尔方辛说，“这次比那次(1978)更有价值，因为我们代表的是一个民主国家。”"
}, {
    "title": "重庆最能聊的哥第二弹:温柔小刹车】那个最会聊的重庆司机又来了！上次吐槽导航，这次跟大家分享了踩刹车的心得。被人称“温柔小刹车”，师傅表示，有的司机踩的不是刹车，是杀父仇人。",
    "content": "特朗普内部的政治斗争在过去几个月从未停息。现在，以美国财长姆努钦为代表的高盛系，和白宫首席策略师班农为代表的民粹右翼"

}]


class Indexhandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html", user_list=USER_LIST, news_list=NEWS_LIST)



class Loginhandler(tornado.web.RequestHandler):
    # def get(self):
    #     self.render("index.html", )

    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        pwd = self.get_argument("pwd", None)
        if username == "alex" and pwd == "123":  # 一个坑，这里收到的pwd是字符串
            USER_LIST["is_login"] = True
            USER_LIST["username"] = username
        self.redirect("/index")   #跳转的时候不带参数
        # print(USER_LIST, username)
        # self.render("index.html", user_list=USER_LIST,news_list=NEWS_LIST)  # 重点坑渲染的时候带参数


class Publishhandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        title = self.get_argument("title")
        content = self.get_argument("content")
        # print(title, content)
        NEWS_LIST.append({"title": title, "content": content})
        self.redirect("/index")


settings = {
    "template_path": "template",  # 模板路径的配置
    "static_path": "static",  # 静态文件的位置
    # 'static_url_prefix': '/sss/',#静态文件地址别名

}
# 路由映射，路由系统
application = tornado.web.Application(
    [(r"/index", Indexhandler),
     (r"/login", Loginhandler),
     (r"/publish", Publishhandler)],
    **settings)  # 创建一个对象

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
