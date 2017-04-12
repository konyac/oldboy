#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver, os, subprocess


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        ac_path = os.path.join(os.path.dirname(__file__), "account", "ac")
        db_path = os.path.join(os.path.dirname(__file__), "account", "db")
        conn = self.request
        while True:
            ret = str(conn.recv(1024), encoding="utf-8")
            if ret == "reg":
                conn.sendall(bytes("acc", encoding="utf-8"))
                account = str(conn.recv(1024), encoding="utf-8")
                u, p = account.split("$")
                if os.path.exists(ac_path):
                    with open(ac_path, "r") as f:
                        for line in f:
                            if line.split("$")[0] == u:
                                ret = "0"
                                break
                            else:
                                ret = "1"
                    if ret == "1":
                        with open(ac_path, "a") as f:
                            f.write(account)
                else:
                    with open(ac_path, "a") as f:
                        ret = "1"
                        f.write(account)
                conn.sendall(bytes(ret, encoding="utf-8"))
            elif ret == "login":
                conn.sendall(bytes("login", encoding="utf-8"))
                l_account = str(conn.recv(1024), encoding="utf-8")
                with open(ac_path, "r") as f:
                    for line in f:
                        if line == l_account:
                            ret = "1"
                            break
                        else:
                            ret = "0"
                conn.sendall(bytes(ret, encoding="utf-8"))
            elif ret == "comm":
                while True:
                    conn.sendall(bytes("#", encoding="utf-8"))
                    ret = str(conn.recv(1024), encoding="utf-8")
                    if ret == "q":
                        conn.sendall(bytes("exit", encoding="utf-8"))
                        break
                    out = subprocess.getoutput(ret)
                    out_len = len(out)
                    conn.sendall(bytes(str(out_len),encoding="utf-8"))#输出的长度

                    conn.sendall(bytes(out,encoding="utf-8"))
                    conn.recv(1024)





            else:
                break


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 9999), Myserver)
    server.serve_forever()
