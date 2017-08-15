#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("cors.html")

    def post(self, *args, **kwargs):
        favor = self.get_arguments("favor") #checkbox取值的时候要用get_arguments
        name = self.get_argument("name",None)
        xb = self.get_argument("xb",None)
        sl = self.get_argument("sel",None)
        print(favor, name, xb,sl)
        self.redirect("/index")

settings = {
    "static_path": "static",
    "template_path": "views",
    "static_url_prefix": "static",
}

app = tornado.web.Application([("/index", IndexHandler),
                               ], **settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
