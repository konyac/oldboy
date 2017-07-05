#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 OK\r\n\r\n")
    client.send("Hello s")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("localhost",8000))
    sock.listen(5)

    while True:
        conn,add = sock.accept()
        handle_request(conn)
        conn.close()

if __name__ == "__main__":
    main()
