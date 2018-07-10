#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/8 11:27
#=============================================================
# coding:utf8
import socket, threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()

def handler_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf8'))
        re_data = input()
        sock.send(re_data.encode('utf8'))

while True:
    sock, addr = server.accept()

    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handler_sock, args=(sock, addr))
    client_thread.start()
