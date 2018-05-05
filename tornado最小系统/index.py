#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop





class Indexhandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        pass



settings = {
    "template_path": "views",  # 模板路径的配置
    "static_path": "statics",  # 静态文件的位置
    'static_url_prefix': '/statics/',#静态文件地址别名


}
# 路由映射，路由系统
application = tornado.web.Application([(r"/index", Indexhandler)], **settings)  # 创建一个对象


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
