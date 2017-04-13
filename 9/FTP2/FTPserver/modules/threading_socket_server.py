#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
import json, os
import platform
from conf import settings
from modules import user
import hashlib
import subprocess


class MyTCPHandler(socketserver.BaseRequestHandler):
    response_code_list = {
        "200": "Pass authentication!",
        "201": "Wrong username or password",
        "300": "Ready to send file to client",
        "301": "Client ready to recevie file",
        "302": "File doesn't exist",
        "2002": "ACK(可以开始上传)",
        "2003": "file exist",
    }

    # def setup(self):
    #   settings.BASE_DIR = BASE_DIR
    #   settings.USER_HOME = "%s/var/users" % BASE_DIR
    def handle(self):
        while True:
            data = self.request.recv(1024).decode()
            print("received data:", data)
            if not data:
                print("user disconnected")
                break
            self.instruction_distributor(data)

    def instruction_distributor(self, instruction):
        print("in1", instruction)
        instructions = instruction.split("|")
        print("in2", instructions)
        function_str = instructions[0]
        if hasattr(self, function_str):
            func = getattr(self, function_str)
            func(instructions[1])
        else:
            print("Invalid instruction")

    def calculate_storage(self):
        self.login_user.used_storage = 0

    def ls(self, user_data):
        directory_path = "%s\\%s%s" % (
        settings.USER_HOME, self.login_user.username, "\\".join(self.login_user.cwd) + "\\")
        print("cwd>>>", directory_path)
        print(">>>", self.login_user.cwd)
        if platform.system() == "Windows":
            cmd = "dir %s" % directory_path
        else:
            cmd = "ls %s" % directory_path
        print(cmd)
        cmd_call = subprocess.getoutput(cmd)
        print(cmd_call)
        cmd_result = bytes(cmd_call, encoding="gbk")

        self.request.send(cmd_result)

    def dir(self, user_data):
        directory_path = "%s\\%s%s" % (
        settings.USER_HOME, self.login_user.username, "\\".join(self.login_user.cwd) + "\\")
        cmd = "dir"
        cmd_call = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        cmd_result = cmd_call.stdout.read()
        self.request.send(cmd_result)

    def cd(self, user_data):
        json_data = json.loads(user_data)

        new_dir = json_data["cwd"]
        abs_dir = "%s\\%s%s" % (settings.USER_HOME, self.login_user.username, "\\".join(new_dir) + "\\")
        if os.path.isdir(abs_dir):
            self.request.send(json.dumps({"response": "601", "cwd": new_dir}).encode())
            self.login_user.cwd = new_dir
        else:
            self.request.send(json.dumps({"response": "602"}).encode())

    def file_put(self, user_data):
        json_data = json.loads(user_data)
        if not self.login_user.used_storage:
            self.calculate_storage()
        if self.login_user.used_storage + json_data["file_size"] > self.login_user.storage_limit:
            self.request.send(json.dumps({"response": "303"}).encode())

        else:
            self.request.send(json.dumps({"response": "303"}).encode())

        file_abs_path = self.get_file_abs_path(json_data["file name"])
        total_file_size = int(json_data["file_size"])

        has_received = 0

        if os.path.exists(file_abs_path):
            self.request.sendall(bytes("2003", encoding="utf-8"))
            is_continue = str(self.request.recv(1024), encoding="utf-8")
            if is_continue == "2004":
                has_file_size = os.stat(file_abs_path).st_size
                self.request.sendall(bytes(str(has_file_size), encoding="utf-8"))
                has_received -= has_file_size
                f = open(file_abs_path, "ab")
            else:
                f = open(file_abs_path, "wb")
        else:
            self.request.sendall(bytes("2002", encoding="utf-8"))
            f = open(file_abs_path, "wb")
        while has_received < total_file_size:
            data = self.request.recv(1024)
            f.write(data)
            has_received += len(data)
        print("ending")
        f.close()

    def get_file_abs_path(self, filename):
        return "%s/%s%s%s" % (
            settings.USER_HOME, self.login_user.username, "/".join(self.login_user.cwd) + "/", filename)

    def file_get(self, user_data):
        print("client try to get a file")
        json_data = json.loads(user_data)
        file_abs_path = self.get_file_abs_path(json_data["file_name"])
        print("file_abs_path:", file_abs_path)
        if os.path.isfile(file_abs_path):
            file_size = os.path.getsize(file_abs_path)
            response_msg = {"response": "300",
                            "file_size": file_size,
                            "md5": hashlib.md5(open(file_abs_path, "rb").read()).hexdigest()
                            }
            self.request.send(json.dumps(response_msg).encode())

            client_response_json = json.loads(self.request.recv(1024).decode())
            if client_response_json["response"] == "301":
                f = open(file_abs_path, "rb")
                client_size = client_response_json["received_size"]
                f.seek(client_size)
                sent_size = client_size
                while file_size != sent_size:
                    data = f.read(4096)
                    self.request.send(data)
                    sent_size += len(data)
                else:
                    print("file transfer completed")
                    f.close()
        else:
            response_msg = {"response": "302"}
            self.request.send(json.dumps(response_msg).encode())

    def user_auth(self, data):
        auth_info = json.loads(data)
        if auth_info["username"] in settings.USER_ACCOUNT:
            if settings.USER_ACCOUNT[auth_info["username"]]["password"] == auth_info["password"]:
                self.login_user = user.User(auth_info["username"], settings.USER_ACCOUNT[auth_info["username"]])
                response_code = "200"
                print(response_code)
                try:
                    # print(settings.USER_HOME,self.login_user)
                    os.makedirs("%s\\%s" % (settings.USER_HOME, self.login_user.username))
                except OSError:
                    print("hhh")
                    pass
            else:
                response_code = "201"
            self.request.send("response|{0}".format(response_code).encode())

