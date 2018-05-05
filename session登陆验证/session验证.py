#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import hashlib,time
container = {}

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
       if self.get_argument("u",None) in ["alex","eric"]:
            obj = hashlib.md5()
            obj.update(bytes(str(time.time()),encoding="utf-8"))
            random_str = obj.hexdigest() #生成一个随机字符串
            container[random_str] = {}
            container[random_str]["k1"] = "123"
            container[random_str]["k2"] = self.get_argument("u",None)+"parents"
            container[random_str]["is_login"] = True
            self.set_cookie("iiiiiiii",random_str)
            self.redirect("/manager")
       else:
           self.write("请登陆")

class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        random_str =  self.get_cookie("iiiiiiii",None)
        current_user_info = container.get(random_str,None)
        if not current_user_info:
            self.redirect("/index")
        else:
            if current_user_info.get("is_login",None):
                temp = "%s -%s" % (current_user_info.get("k1",""),current_user_info.get("k2",""))
                self.write(temp)
            else:
                self.redirect("/index")



setting = {
    "template_path": "views",  # 模板路径
    "static_path": "statics",  # 静态文件
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
}
application = tornado.web.Application(
    [("/login", LoginHandler),
     ("/manager", ManagerHandler)], **setting
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
