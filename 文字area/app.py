#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import tornado.ioloop
import pymysql
list=['']

def insert(args):
    flag =True
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test1',charset='utf8')
    cursor = conn.cursor()
    temp = "insert into lab (text) values ('%s')" % args
    print(temp)
    effect_row = cursor.execute(temp)
    conn.commit()
    cursor.close()
    conn.close()
    if not effect_row:
        flag=False
    return flag

# print(select())
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html",item=list[-1])

    def post(self, *args, **kwargs):
        text = self.get_argument('text',None)
        text = text.replace( '\n',"<br/>")
        list.append(text)
        result = insert(text)
        print(text,result,list)
        self.render("login.html", item=list[-1])

settings = {
    "template_path": "views",
    "static_path": "statics",

}

app = tornado.web.Application([("/index", IndexHandler),
                               ], **settings)

# print(insert("112sdfah啊哈"))
if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

