#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
from conf import settings
from models import threading_socket_server


class ArgvHandle:
    def __init__(self,args):
        self.args = args
        self.argv_parse()

    def argv_parse(self):
        if len(self.args)<1:
            self.help_msg()
        else:
            first_argv = self.args[1]
            if hasattr(self,first_argv):
                fun = getattr(self,first_argv)
                fun()
            else:
                self.help_msg()
    def help_msg(self):
        pass

    def start(self):
        try:
            print("starting...")
            server = socketserver.ThreadingTCPServer((settings.BIND_HOST,settings.BIND_PORT),threading_socket_server.MyTCPHandler)
            print("server started")
            server.serve_forever()
        except KeyboardInterrupt:
            pass
