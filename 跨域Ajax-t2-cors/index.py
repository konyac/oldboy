#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop

class CorsHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.write("{'status':1,'message':'get'}")


    def post(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin","http://cuicui.com:8001") #加上响应头，响应的值就是你客户端的域名，所有客户域名都符合要求 写成*即可。
        self.write("{'status':1,'message':'post'}")


settings = {
    "template_path": "views",
    "static_path": "static",

}

app = tornado.web.Application([("/cors", CorsHandler),
                               ], **settings)

if __name__ == "__main__":
    app.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
