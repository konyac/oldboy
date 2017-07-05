#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop

class Mainhandler(tornado.web.RequestHandler):#继承类RequestHandler
    def get(self):
        # self.write("hello world")
        self.render("s2.html")

settings = {
    "template_path":"template",#模板路径的配置
    "static_path":"static",#静态文件的位置
}
#路由映射，路由系统
application = tornado.web.Application([(r"/index",Mainhandler)],**settings)#创建一个对象

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()