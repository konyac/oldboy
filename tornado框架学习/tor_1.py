#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import uimethod as mt
import uimodules as md

INPUTS_LIST = []


class Mainhandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self):
        # self.write("hello world")
        # 1、打开s1.html文件，读取内容，（包含特殊语法）
        # 2、把这个字符串进行一个分解。将传入的值与html进行结合渲染。
        # 3、渲染完毕得到新的字符串，得到已经替换完毕的字符串。
        # 4、返回给用户。

        name = self.get_argument('ooxx', None)
        if name:
            INPUTS_LIST.append(name)
            # xxxooo = INPUTS_LIST  #  这样不行传入报错
        self.render("s1.html", npm="NPM888", inputs=INPUTS_LIST)  # 不能只写一个列表名称，要把前端用到的变量也定义上

        # self.render("s1.html", inputs=INPUTS_LIST)#post方式

    def post(self, *args, **kwargs):
        name = self.get_argument("ooxx")#获取用户提交的数据
        print(name)
        INPUTS_LIST.append(name)
        self.render("s1.html",inputs=INPUTS_LIST)


#     get方式 url中传输数据。


settings = {
    "template_path": "template",  # 模板路径的配置
    "static_path": "statics",  # 静态文件的位置
    # 'static_url_prefix': '/sss/',#静态文件地址别名
    "ui_methods":mt,#自定义方法
    "ui_modules":md,#自定义模块

}
# 路由映射，路由系统
application = tornado.web.Application([(r"/index", Mainhandler)], **settings)  # 创建一个对象


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
