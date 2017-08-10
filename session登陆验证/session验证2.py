#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import hashlib, time

container = {}


class Session:
    def __init__(self, handler):
        self.handler = handler
        self.random_str = None

    def __genarate_random_str(self):  # 只有类里面能调用
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding="utf-8"))
        random_str = obj.hexdigest()  # 生成一个随机字符串
        return random_str

    def set_value(self, key, value):
        # 在container中加入随机字符串
        # 定义属于自己的数据
        # 在客户端中写入随机字符串
        # 判断，请求的用户是否已有随机字符串
        # random_str = self.handler.get_cookie("__kakaka__")
        if not self.random_str: #将每次的写入值，写到同一个key中，即同一个随机字符串中
            random_str = self.handler.get_cookie("__kakaka__")
            if not random_str:#第一次登陆，客户端没有cookie，设置cookie。
                random_str = self.__genarate_random_str()
                # self.random_str = random_str
                container[random_str] = {}
            else:#不是第一次登陆，客户端有cookie
                if random_str in container.keys():#客户端的中的cookie在服务器container中，已经有这个随机字符串了
                    pass
                else:#客户端的cookie不是服务器container中的。
                    random_str = self.__genarate_random_str()
                    container[random_str] = {}
            self.random_str = random_str#重新给self.random_str 负责
        container[self.random_str][key] = value #设置key value
        self.handler.set_cookie("__kakaka__", self.random_str) #写入cookie。设置完成

    def get_value(self, key):
        # 获取客户端的随机字符串
        # 从container中读取专属于我的数据
        # 专属信息[key]
        random_str = self.handler.get_cookie("__kakaka__")
        if not random_str:  # 没有拿到session 随机字符串
            return None
        user_info_dict = container.get(random_str, None)
        if not user_info_dict:  # 拿到的session字符串不在我的container中
            return None
        value = user_info_dict.get(key,None)
        return value


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        if self.get_argument("u", None) in ["alex", "eric"]:
            obj = Session(self)
            obj.set_value("is_login", True)
            obj.set_value("name", self.get_argument("u", None))
            print(container)
            self.redirect("/manager")
        else:
            self.write("请登陆")


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        obj = Session(self)
        if obj.get_value("is_login"):
            self.write("成功"+obj.get_value("name"))
        else:
            self.write("失败")


setting = {
    "template_path": "views",  # 模板路径
    "static_path": "static",  # 静态文件
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
}
application = tornado.web.Application(
    [("/login", LoginHandler),
     ("/manager", ManagerHandler)], **setting
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
