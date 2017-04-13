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
        self.USER_HOME = "%s\\var\\users" % BASE_DIR
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
            "2002": "ACK(可以开始上传)",
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
            self.sock.connect((host, int(port)))
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
        print(str(server_response, encoding="gbk"))

    def instruction_cd(self, instructions):
        print("instr:", instructions)
        if len(instructions) == 1:
            print("gg")
        elif len(instructions) == 2:
            path = instructions[1]
            if path.startswith("/"):
                try_path = path.split("/")
            else:
                try_path = self.cwd
                print("try_path", try_path)
                split_path = path.split("/")
                try_path.extend(split_path)
                print(try_path)
            self.sock.send(("cd|%s" % json.dumps({"cwd": try_path})).encode())
            server_response = json.loads(self.sock.recv(1024).decode())
            if server_response["response"] == "601":
                print("self.cwd", server_response["cwd"])
                if server_response["cwd"][-1] == "..":
                    server_response["cwd"].pop(-1)
                    server_response["cwd"].pop(-1)

                self.cwd = server_response["cwd"]
            elif server_response["response"] == "602":
                print("directory doesn't exist")

    def bar(self, num=1, sum=100):
        rate = float(num)/float(sum)
        rate_num = int(rate*100)
        temp = "\r%d %%" % (rate_num)
        sys.stdout.write(temp)
        sys.stdout.flush()

    def instruction_put(self, instructions):
        file_is = ""
        if len(instructions) == 1:
            print("gg")
            pass
        elif os.path.isfile(os.path.join(os.path.dirname(os.path.dirname(__file__)), instructions[1])):
            file_is = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), instructions[1]))
        elif os.path.isfile(instructions[1]):
            file_is = instructions[1]
        if file_is != "":
            file_bytes_size = os.stat(file_is).st_size
            file_name = os.path.basename(file_is)
            print(file_bytes_size,file_name)
            put_str = "put|%s" % json.dumps({"file_name": file_name, "file_size": file_bytes_size})
            print(put_str)
            self.sock.send(put_str.encode())
            server_response = json.loads(self.sock.recv(1024).decode())
            if server_response["response"] == "303":
                print(self.response_code["303"])
            elif server_response["response"] == "301":
                has_send = 0
                print(self.response_code["301"])
                server_response = str(self.sock.recv(1024), encoding="utf-8")
                if server_response == "2003":
                    inp = input(self.response_code["2003"] + "续传?Y/N")
                    if inp.upper() == "Y":
                        self.sock.send(bytes("2004", encoding="utf-8"))
                        has_file_size = int(str(self.sock.recv(1024), encoding="utf-8"))
                        has_send = has_file_size
                        f = open(file_is, "rb")
                        f.seek(has_file_size)
                    else:
                        f = open(file_is, "rb")

                else:
                    print(self.response_code["2002"])
                    f = open(file_is, "rb")
                while has_send < file_bytes_size:
                    data = f.read(1024)
                    self.sock.sendall(data)
                    has_send += len(data)
                    self.bar(has_send, file_bytes_size)
                f.close()
                print("上传成功")



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
                    os.makedirs("%s\\%s" % (self.USER_HOME, self.login_user))
                except OSError:
                    print("bbb")
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
