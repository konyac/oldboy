#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
from newchouti.controllers import home
from newchouti.controllers import account
from newchouti.backend import uimethods as mt

settings = {
    "template_path": "views",  # 模板路径的配置
    "static_path": "statics",  # 静态文件的位置
    'static_url_prefix': '/statics/',  # 静态文件地址别名
    'autoreload': True,
    'ui_methods': mt

}
# 路由映射，路由系统
application = tornado.web.Application(
    [(r"/index", home.IndexHandler),
     (r"/login", account.LoginHandler),
     (r"/send_cond", account.SendCodeHandler),
     (r"/register", account.RegisterHandler),
    (r"/upload_image", home.UploadImageHandler),
     (r"/check_code", account.CheckCodeHandler),
(r"/comment", home.CommentHandler),
    (r"/favor", home.FavorHandler),

     ],
    **settings)  # 创建一个对象

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
