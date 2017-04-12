#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import socket
import json
import hashlib
import copy


class Client:
    def __init__(self, sys_argv):
        self.USER_HOME = "%s/var/users" % BASE_DIR
        self.args = sys_argv
        self.argv_parse()
        self.response_code = {
            "200": "pass user authentication!",
            "201": "wrong username or password",
            "300": "ready to get file from server",
            "301": "ready to send to server",
            "302": "file doesn't exist on ftp server",
            "303": "storage full",
            "601": "changed directory ",
            "602": "failed to find directory",
            "2003": "file exist",
            "2004": "continue put",
        }
        self.handle()

    def help_msg(self):
        msg = """
            -s ftp_server_addr
            -p ftp_server_port
        """
        print(msg)

    def argv_parse(self):
        if len(self.args) < 5:
            self.help_msg()
            sys.exit()
        else:
            mandatory_fields = ["-p", "-s"]
            for i in mandatory_fields:
                if i not in self.args:
                    self.help_msg()
                    sys.exit("")
            try:
                self.ftp_host = self.args[self.args.index("-s") + 1]
                self.ftp_port = self.args[self.args.index("-p") + 1]
            except (IndexError, ValueError):
                self.help_msg()
                sys.exit("")

    def connect(self, host, port):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
        except socket.error as e:
            sys.exit("Failed to connect server: %s" % e)

    def get_response_code(self, response):
        response_code = response.split("|")
        code = response_code[1]
        return code

    def parse_instruction(self, user_input):
        user_input_to_list = user_input.split()
        func_str = user_input_to_list[0]
        if hasattr(self, "instruction_" + func_str):
            return True, user_input_to_list
        else:
            return False, user_input_to_list

    def current_dir(self, cwd):
        return "/".join(cwd) + "/"

    def interactive(self):
        self.logout_flag = False
        while self.logout_flag is not True:
            user_input = input("[%s]:%s" % (self.login_user, self.current_dir(self.cwd))).strip()
            if len(user_input) == 0: continue
            status, user_input_instructions = self.parse_instruction(user_input)
            if status is True:
                func = getattr(self, "instruction_" + user_input_instructions[0])
                func(user_input_instructions)
            else:
                print("Invalid instruction")

    def instruction_ls(self, instructions):
        self.sock.send(("ls|%s" % json.dumps({})).encode())
        server_response = self.sock.recv(1024)
        print(str(server_response,encoding="gbk"))

    def auth(self):
        retry_count = 0
        while retry_count < 3:
            username = input("Please enter your username:")
            if len(username) == 0: continue
            password = input("Please enter your password:")
            if len(password) == 0: continue
            md5 = hashlib.md5()
            md5.update(password.encode())
            auth_str = "user_auth|%s" % (json.dumps({"username": username, "password": md5.hexdigest()}))
            self.sock.send(auth_str.encode())
            server_response = self.sock.recv(1024).decode()
            response_code = self.get_response_code(server_response)
            if response_code == "200":
                self.login_user = username
                self.cwd = [""]
                try:
                    os.makedirs("%s%s" % (self.USER_HOME, self.login_user))
                except OSError:
                    print("hhh")
                    pass
                return True
            else:
                retry_count += 1
        else:
            sys.exit("too many attemps")

    def handle(self):
        self.connect(self.ftp_host, self.ftp_port)
        if self.auth():
            self.interactive()
