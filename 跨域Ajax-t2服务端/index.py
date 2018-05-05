#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("t2.ajax")
        # self.write("alert('s2.ajax')")
        callback = self.get_argument("callback")#服务器端获取客户发来请求的callback，以这个callback命名函数
        self.write("%s([11,22,33]);" % callback)#跨域访问的服务器，把要发送的数据包到一个函数里面，在客户端执行函数就行了。


    def post(self, *args, **kwargs):
        self.write("t2.ajax")


settings = {
    "template_path": "views",
    "static_path": "statics",

}

app = tornado.web.Application([("/index", IndexHandler),
                               ], **settings)

if __name__ == "__main__":
    app.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
