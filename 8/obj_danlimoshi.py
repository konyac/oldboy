#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class ConnectionPoll:
    __instance = None

    def __init__(self):
        self.ip = "1.1.1.1"
        self.port = 3306
        self.pwd = 123
        self.username = "root"

        self.conn_list = [1,2,3,4,5,6,7]

    @staticmethod
    def get_instance():
        if ConnectionPoll.__instance:
            return ConnectionPoll.__instance
        else:
            #创建一个对象，并且赋值给__instance
            ConnectionPoll.__instance = ConnectionPoll()
            return ConnectionPoll.__instance
#静态方法类去访问
obj1 = ConnectionPoll.get_instance()
print(obj1)
obj2 = ConnectionPoll.get_instance()
print(obj2)
obj2= ConnectionPoll.get_instance()
print(obj2)