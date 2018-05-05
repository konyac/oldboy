#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import re


class MainForm:
    def __init__(self):
        """
        定义参数的规则，正则验证规则
        """
        self.host = "(.*)"
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
        self.port = '(\d+)'
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'

    def check_valid(self, request):
        """
        验证表单数据是否符合规则
        :param request: 传入的Indexhandler对象，也就是self。用来获取参数的。self.get_argument("host")
        :return: 返回验证结果
        """
        flag = True
        value_dict = {}  # 用来存储key value
        form_dict = self.__dict__  # self.__dict__方法获取对象的属性字典。获取对象的参数
        # print(form_dict)
        for key, regular in form_dict.items():
            post_value = request.get_argument(key, None)  # 用户输入的值
            val = re.match(regular, post_value)  # 正则匹配，math，从开头开始匹配，成功返回一个对象，不成功是None
            if not val:
                flag = False
            value_dict[key] = post_value
            # print(key, val, post_value)
        return flag, value_dict  # 返回验证的标志，


class Indexhandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        obj = MainForm()
        is_valid, value_dict = obj.check_valid(self)
        print(is_valid, value_dict)
        if is_valid:
            print(value_dict)
            # self.write("ok")


settings = {
    "template_path": "views",  # 模板路径的配置
    "static_path": "statics",  # 静态文件的位置
    'static_url_prefix': '/statics/',  # 静态文件地址别名

}
# 路由映射，路由系统
application = tornado.web.Application([(r"/index", Indexhandler)], **settings)  # 创建一个对象

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
