#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import os
import json

rep = {"status": False, "data": "", "summary": ""}


class Indexhandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        pass


class RenHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("renzheng.html")

    def post(self, *args, **kwargs):
        pass


class ProHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("product.html")

    def post(self, *args, **kwargs):
        pass

class GroupHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("group.html")

    def post(self, *args, **kwargs):
        pass

class ComHandler(tornado.web.RequestHandler):  # 继承类RequestHandler

    def get(self, *args, **kwargs):
        self.render('company.html')

class EditproHandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        name = self.get_argument('name', None)
        name = name
        self.render("edit.html",name=name)

class Ren2Handler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):

        self.render("renzheng2.html")


class UploadHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        try:
            file_metas = self.request.files["img"]
            for meta in file_metas:
                file_name = meta['filename']
                file_path = os.path.join('statics', 'upload', file_name)
                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
            rep['status'] = True
            rep['data'] = file_path
        except Exception as ex:
            rep['summary'] = str(ex)
        self.write(json.dumps(rep))


settings = {
    "template_path": "views",  # 模板路径的配置
    "static_path": "statics",  # 静态文件的位置
    'static_url_prefix': '/statics/',#静态文件地址别名

}
# 路由映射，路由系统
application = tornado.web.Application([(r"/index", Indexhandler),
                                       (r"/upload_image", UploadHandler),
                                       (r"/company", ComHandler),
                                       (r"/renzheng", RenHandler),
                                       (r"/renzheng2", Ren2Handler),
                                       (r"/product", ProHandler),
                                       (r"/edit-product", EditproHandler),
                                       (r"/group", GroupHandler),
                                       ],
                                      **settings)  # 创建一个对象

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
