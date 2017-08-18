import tornado.ioloop
import tornado.web
import re


# 检测输入框的ip
class IPFiled:
    REGULAR = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"  # 静态 字段

    def __init__(self, error_dict=None, required=True):
        # 封装了错误信息  81行实例化时候封装的
        self.error_dict = {}
        if error_dict:  # 81 行实例化 传入的错误信息,如果不传 则为None,则不会执行
            self.error_dict.update(error_dict)  # 将实例化时候 传入的错误信息封装

        self.required = required  # # 81 行实例化 传入的是否为空字段,默认是浏览器输入不许为空

        self.error = None  # 错误信息
        self.value = None
        self.is_valid = False

    def validate(self, name, input_value):
        """
        :param name: 字段名
        :param input_value: 用户表单中输入的内容
        :return:
        """
        if not self.required:  # 当比如81行我们传入可以为空的时候即False时候走这一段代码
            # 用户输入可以为空
            self.is_valid = True  # 设置封装值为真
            self.value = input_value  # 将空值封装
        else:  # 当81行要求输入不为空时候
            # 用户有输入,这一要验证正则了。
            if not input_value.strip():  # 输入为空,返回错误信息。 错误信息字典
                if self.error_dict.get('required', None):  # 81行定义的错误信息。如果未定义则自己定义
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name  # 默认错误信息
            else:  # 输入不为空,
                ret = re.match(IPFiled.REGULAR, input_value)  # 获取 静态字段的正则字符串,跟用户的input输入内容匹配
                if ret:  # 匹配通过,
                    self.is_valid = True
                    self.value = input_value
                else:  # 匹配不通过,返回错误字典
                    if self.error_dict.get('valid', None):  # 81 行定义的错误信息,如果未定义则自己定义
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid" % name


# 检测 输入框的字符串
class StringFiled:
    REGULAR = "^(.*)$"  # 静态 字段

    def __init__(self, error_dict=None, required=True):
        # 封装了错误信息  82行实例化时候封装的
        self.error_dict = {}
        if error_dict:  # 82 行实例化 传入的错误信息,如果不传 则为None,则不会执行
            self.error_dict.update(error_dict)  # 将实例化时候 传入的错误信息封装

        self.required = required  # # 81 行实例化 传入的是否为空字段,默认是浏览器输入不许为空

        self.error = None  # 错误信息
        self.value = None
        self.is_valid = False

    def validate(self, name, input_value):
        """
        :param name: 字段名
        :param input_value: 用户表单中输入的内容
        :return:
        """
        if not self.required:  # 当比如82行我们传入可以为空的时候即False时候走这一段代码
            # 用户输入可以为空
            self.is_valid = True  # 设置封装值为真
            self.value = input_value  # 将空值封装
        else:  # 当81行要求输入不为空时候
            # 用户有输入,这一要验证正则了。
            if not input_value.strip():  # 输入为空,返回错误信息。 错误信息字典
                if self.error_dict.get('required', None):  # 82行定义的错误信息。如果未定义则自己定义
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name  # 默认错误信息
            else:  # 输入不为空,
                ret = re.match(StringFiled.REGULAR, input_value)  # 获取 静态字段的正则字符串,跟用户的input输入内容匹配
                if ret:  # 匹配通过,
                    self.is_valid = True
                    self.value = input_value
                else:  # 匹配不通过,返回错误字典
                    if self.error_dict.get('valid', None):  # 82 行定义的错误信息,如果未定义则自己定义
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid" % name


# 检测输入框的复选框
class ChechBoxFiled:
    def __init__(self, error_dict=None, required=True):
        # 封装了错误信息
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)

        self.required = required

        self.error = None  # 错误信息
        self.value = None
        self.is_valid = False

    def validate(self, name, input_value):
        """
        :param name: 字段名 favor
        :param input_value: 用户表单中输入的内容，列表None, [1,2]
        :return:
        """

        if not self.required:
            # 用户输入可以为空
            self.is_valid = True
            self.value = input_value
        else:
            if not input_value:
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name
            else:
                self.is_valid = True
                self.value = input_value


class FileFiled:
    REGULAR = "^(\w+\.pdf)|(\w+\.mp3)|(\w+\.py)|(\w+\.txt)$"

    def __init__(self, error_dict=None, required=True):
        # 封装了错误信息
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)  # 错误信息更新
        self.required = required
        self.error = None  # 错误信息
        self.value = []  # 默认是空列表
        self.is_valid = True
        self.name = None
        self.success_file_name_list = []

    def validate(self, name, all_file_name_list):
        """
        :param name: 字段名
        :param all_file_name_list: 所有文件文件名
        :return:
        """
        self.name = name
        if not self.required:
            # 用户输入可以为空
            self.is_valid = True
            self.value = all_file_name_list
        else:
            if not all_file_name_list:  # 没有传文件，一个都没传
                self.is_valid = False
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name
            else:
                # 循环所有的文件名，避免有的传，有的没传
                for file_name in all_file_name_list:
                    ret = re.match(FileFiled.REGULAR, file_name)
                    if not ret:
                        self.is_valid = False
                        if self.error_dict.get('valid', None):
                            self.error = self.error_dict['valid']
                        else:
                            self.error = "%s is invalid" % name
                        break  # 只要有一个没传值，就退出。
                    else:
                        self.value.append(file_name)  # 成功一个加一个。

    def save(self, request, path='static'):#一般path=static
        # 获取所有的文件列表，
        file_metas = request.files.get(self.name)  # self.name = fafafa
        temp_list = []
        #x循环每一个文件列表
        for meta in file_metas:
            file_name = meta['filename']  # 每个文件的文件名
            # 文件名存在 并且文件名在文件名列表中
            import os
            # self.value:[1.py, 2.py]  【statics/1.py  statics/2.py】
            new_file_name = os.path.join(path, file_name)

            if file_name and file_name in self.value:
                temp_list.append(new_file_name)
                with open(new_file_name, "wb") as up:
                    up.write(meta['body'])
        # print(temp_list)
        self.value= temp_list #此时更改self.value  其实在打印之后，验证完毕之后都已经输出了。因此不起作用。


class BaseForm:  # 公共的类的方法,不用重复写
    def check_valid(self, handle):  # 94 行调用了这个方法,继承找到的
        flag = True  # 默认为true
        error_message_dict = {}
        success_value_dict = {}
        for key, regular in self.__dict__.items():  # 对象的所有项 self。(ip  IPFiled对象)
            # key: ip .....
            # handle: HomeIndex对象，self.get_... self.
            # regular: IPFiled(required=True)
            if type(regular) == ChechBoxFiled:
                input_value = handle.get_arguments(key)  # 获取的是复选框字典 ,没有默默认参数
            elif type(regular) == FileFiled:
                # 获取文件名
                file_list = handle.request.files.get(key)  # 获取所有文件，放到一个列表里。一个个文件对象到列表里，对象是个字典
                # [{"body":"xx","filename":"xx"},{"body":"xx","filename":"xx"}]
                input_value = []
                for item in file_list:
                    input_value.append(item['filename'])
                    # 对所有文件名验证，把input_value 列表传过去，文件名都放到这里
            else:
                input_value = handle.get_argument(key, None)  # 获取浏览器传输过来的输入框的name值
            # input_value = 用户输入的值
            # 将具体的验证，放在IPFiled对象中
            regular.validate(key,input_value)  # 由于regular是字段验证对象,于是跳到其valiate方法这里是IPField 由于是 IPFiled对象的validate方法,传入前端input框的name值
            if regular.is_valid:
                success_value_dict[key] = regular.value
            else:
                error_message_dict[key] = regular.error
                flag = False

        return flag, success_value_dict, error_message_dict


# class IndexForm(BaseForm):
#     def __init__(self):
#         self.host = "(.*)"
#         self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
#         self.port = '(\d+)'
#         self.phone = '^1[3|4|5|8][0-9]\d{8}$'


class FileForm(BaseForm):
    def __init__(self):  # 构造函数
        # IPFiled是另一个类,实例化 ,传入的是我们自定义信息,如果我们不传入,会返回给我们内部自定义信息。
        # 这时候 封装的self.ip 是一个对象。执行IPField的init方法,封装一些属性
        # 下面的ip host favor 必须与前端的input 的name相同
        self.ip = IPFiled(required=True, error_dict={'required': "别闹，别整空的..", "valid": "骚年，格式错误了"})
        self.host = StringFiled(required=False)
        self.favor = ChechBoxFiled(required=True, error_dict={'required': "复选框不能为空"})
        self.fafafa = FileFiled(required=True)


class fileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('file.html', error_dict=None)

    def post(self, *args, **kwargs):
        obj = FileForm()  # 实例化HomeForm类 每种验证都是一个类,而这些验证的类需要验证合法性的方法我们用类的继承放在另一个类中
        # 获取用户输入的内容
        # 和正则表达式匹配
        is_valid, success_dict, error_dict = obj.check_valid(self)  # 将 HomeHandler类对象传入 获取对象继承的类的方法的返回值 执行 BaseForm类的check_valid方法
        if is_valid:  #
            print('success', success_dict)
            obj.fafafa.save(self.request)  # 执行保存文件操作，self.request 保存了文件的信息
        else:
            print('error', error_dict)
            self.render('file.html', error_dict=error_dict)


settings = {
    'template_path': 'views',
    'static_path': 'static',
    'static_url_prefix': '/statics/',
}

application = tornado.web.Application([
    (r"/file", fileHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
