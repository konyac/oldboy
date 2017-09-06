#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import pymysql


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html")
    def post(self, *args, **kwargs):
        username= self.get_argument("user",None)
        pwd = self.get_argument("pwd",None)
        # print(username, pwd)
        # 创建连接
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test1')
        # 创建游标
        cursor = conn.cursor()
        # print(1231)
        # sql注入 前端
        # user 的input: alex' or 1=1 -- '
        # pwd 的input : 随便输入
        temp = "select name from userinfo where name='%s' and password = '%s' " % (username, pwd)
        print(temp)

        effect_row = cursor.execute(temp)
        print(effect_row)

        result = cursor.fetchone()
        print(result)

        conn.commit()

        cursor.close()

        conn.close()
        if result:
            self.write('登录成功')
        else:
            self.write('登录失败')



setting = {
    "template_path":"views",
    "static_path":"static",
}

application = tornado.web.Application([
    ("/login",LoginHandler)
],**setting)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()