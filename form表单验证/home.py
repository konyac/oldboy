#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import re


# 检测输入框的ip
class IPFiled:
    REGULAR = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"  # 静态 字段

    def __init__(self, error_dict=None, required=True):  # 初始化的时候要传入参数，
        self.error_dict = {}  # 用来封装了错误信息  默认为空，可以自己定义
        if error_dict:  # 实例化时 传入的错误信息,如果不传 则为None,则不会执行,有错误信息 就要更新原来的信息
            self.error_dict.update(error_dict)  # 将实例化时候传入的错误信息，封装
        self.required = required  # 实例化时 传入的是否为空字段,默认是浏览器输入不许为空
        self.error = None  # 错误信息
        self.value = None  # 值
        self.is_valid = False  # 是否严重通过

    def validate(self, name, input_value):
        '''
        :param name: 字段名
        :param input_value:用户表单中输入的值     
        :return: 
        '''
        if not self.required:  # 当比如我们实例化时传入可以为空的时候即required = False时候走这一段代码
            # 用户输入可以为空
            self.is_valid = True  # # 设置封装值为真 符合规则的
            self.value = input_value  # 将空置封装。还是原来的值
        else:  # 当实例化时要求输入不为空时候，required = True
            # 用户有输入,这一要验证正则了。
            if not input_value.strip():  # 输入的值为空
                if self.error_dict.get('required', None):  # 实例化时定义的错误信息。如果未定义则自己定义
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name  # 默认错误信息
            else:  # 输入不为空
                ret = re.match(IPFiled.REGULAR, input_value)  # 获取 静态字段的正则字符串,跟用户的input输入内容匹配
                if ret:  # 匹配通过
                    self.is_valid = True
                    self.value = input_value
                else:#匹配不通过,返回错误字典
                    if self.error_dict.get('valid', None):#82 行定义的错误信息,如果未定义则自己定义
                        self.error = self.error_dict['valid']

                    else:
                        self.error = "%s is invalid" % name


class BaseForm:  # 公共的类的方法,不用重复写
    def check_valid(self, handler):
        """
        验证表单数据是否符合规则
        :param handler: 传入的Indexhandler对象，也就是self。用来获取参数的。self.get_argument("host")
        :return: 返回验证结果
        """
        flag = True
        error_message_dict = {}  # 用来存储出错的值信息
        success_value_dict = {}  # 用来存储正确的值信息
        form_dict = self.__dict__  # self.__dict__方法获取对象的属性字典。获取对象的参数
        # print(form_dict)
        for key, regular in form_dict.items():# 对象的所有项 self。ip  IPFiled对象
            '''
            key:就是字段名称，self.ip
            handler:HomeHandler对象，用来获取值得，self.get_argument
            regular = IPFiled(required=True) 一个实例化的对象。
            
            '''
            input_value = handler.get_argument(key)  # 用户输入的值
            # 将具体的验证放到IPFiled中去，在IPFiled validate方法中
            regular.validate(key, input_value)  # 执行验证方法
            if regular.is_valid:
                success_value_dict[key] = input_value
                pass
            else:
                flag = False
                error_message_dict[key] = regular.error
        return flag, success_value_dict, error_message_dict  # 返回验证的标志，


class HomeForm(BaseForm):
    def __init__(self):
        """
        定义参数的规则，正则验证规则
        """

        self.ip = IPFiled(error_dict={'required': "别闹，别整空的..", "valid": "骚年，格式错误了"},required=True,)


class Homehandler(tornado.web.RequestHandler):  # 继承类RequestHandler
    def get(self, *args, **kwargs):
        self.render("home.html",error_dict = None)

    def post(self, *args, **kwargs):
        obj = HomeForm()
        is_valid, success_dict, error_dict = obj.check_valid(self)
        if is_valid:
            print('success',success_dict)
            self.render('home.html',error_dict = None)
        else:
            print('error',error_dict)
            self.render('home.html',error_dict =error_dict)




settings = {
    "template_path": "views",  # 模板路径的配置
    "static_path": "static",  # 静态文件的位置
    'static_url_prefix': '/statics/',  # 静态文件地址别名

}
# 路由映射，路由系统
application = tornado.web.Application([(r"/home", Homehandler)], **settings)  # 创建一个对象

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
