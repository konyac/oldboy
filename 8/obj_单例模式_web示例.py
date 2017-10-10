#!/usr/bin/env python
#coding:utf-8
from wsgiref.simple_server import make_server

# ########### 单例类定义 ###########
class DbHelper(object):

    __instance = None

    def __init__(self):
        self.hostname = '1.1.1.1'
        self.port = 3306
        self.password = 'pwd'
        self.username = 'root'

    @staticmethod
    def singleton():
        if DbHelper.__instance:
            return DbHelper.__instance
        else:
            DbHelper.__instance = DbHelper()
            return DbHelper.__instance

    def fetch(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

    def create(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

    def remove(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

    def modify(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass


class Handler(object):

    def index(self):
        obj =  DbHelper.singleton()
        print(id(obj))
        obj.create()
        return 'index'

    def news(self):
        return 'news'


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    temp = url.split('/')[1]
    obj = Handler()
    is_exist = hasattr(obj, temp)
    if is_exist:
        func = getattr(obj, temp)
        ret = func()
        return ret
    else:
        return '404 not found'

if __name__ == '__main__':
    httpd = make_server('', 8001, RunServer)
    print( "Serving HTTP on port 8001...")
    httpd.serve_forever()

