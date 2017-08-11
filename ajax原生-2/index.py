#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        # self.render("index.html")
        self.write("{'status':111，'message':'mmmmm'}")

settings = {
    "template_path": "views",
    "cookie_secret": "alex"  # cookie加密要添加的
}

app = tornado.web.Application([("/index", IndexHandler),
                              ],**settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
