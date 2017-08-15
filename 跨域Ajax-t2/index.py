#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("t2.ajax")
        # self.write("alert('s2.ajax')")
        self.write("func([11,22,33]);")#跨域访问的服务器，把要发送的数据包到一个函数里面，在客户端执行函数就行了。


    def post(self, *args, **kwargs):
        self.write("t2.ajax")


settings = {
    "template_path": "views",
    "static_path": "static",

}

app = tornado.web.Application([("/index", IndexHandler),
                               ], **settings)

if __name__ == "__main__":
    app.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
