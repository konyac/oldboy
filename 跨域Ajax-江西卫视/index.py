#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        self.write("t1.ajax")


settings = {
    "template_path": "views",
    "static_path": "statics",

}

app = tornado.web.Application([("/index", IndexHandler),
                               ], **settings)

if __name__ == "__main__":
    app.listen(8006)
    tornado.ioloop.IOLoop.instance().start()
