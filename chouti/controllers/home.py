#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web

USER_LIST = {"is_login": None}
NEWS_LIST = [{
    "title": "万科重生：深铁会比华润更积极 因为深铁想从万科得到更多 ",
    "content": "马拉多纳在1986年世界杯夺冠归国后对总统阿尔方辛说，“这次比那次(1978)更有价值，因为我们代表的是一个民主国家。”"
}, {
    "title": "重庆最能聊的哥第二弹:温柔小刹车】那个最会聊的重庆司机又来了！上次吐槽导航，这次跟大家分享了踩刹车的心得。被人称“温柔小刹车”，师傅表示，有的司机踩的不是刹车，是杀父仇人。",
    "content": "特朗普内部的政治斗争在过去几个月从未停息。现在，以美国财长姆努钦为代表的高盛系，和白宫首席策略师班农为代表的民粹右翼"

}]


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("home/index.html", user_list=USER_LIST, news_list=NEWS_LIST)
