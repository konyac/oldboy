#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import json

container = []


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        name = self.get_argument("name", None)
        age = self.get_argument("age", None)
        print(name, age)
        if name and age:
            container.append({name: age})
        self.render("cors.html")

    def post(self, *args, **kwargs):
        # self.render("cors.html")
        resp = json.dumps(container)
        self.write(resp)


settings = {
    "template_path": "views",
    "cookie_secret": "alex"  # cookie加密要添加的
}

app = tornado.web.Application([("/index", IndexHandler),
                               ], **settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
