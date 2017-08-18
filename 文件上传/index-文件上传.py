#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import os

IMG_LIST = []


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("file.html", img_list=IMG_LIST)

    def post(self, *args, **kwargs):
        file = self.request.files.get('img')# 文件是放到列表里的，一个文件是一个字典。
        print(file,type(file))
        for meta in file:
            # file_name 是上次的文件名
            file_name = meta["filename"]
            with open(os.path.join("static", "img", file_name), "wb") as up:  # 保存文件
                # 保存文件
                up.write(meta["body"])
            IMG_LIST.append(file_name)
        self.redirect("/file")


settings = {
    "static_path": "static",#这里的名字如果改动的话，必须和文件目录名字一同改，并且，只能使用{{static_url('css/index.css')}}来访问了。
    "template_path": "views",
    "static_url_prefix": "/static/",#想要用别名的话，前提还得保证静态文件的目录名字叫static，static_path 还是static。也就是前提都是默认的才能用。

}

app = tornado.web.Application([("/file", IndexHandler),
                               ], **settings)

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
