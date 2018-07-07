import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()

while True:
    # 获取客户端数据 1k 数据
    data = sock.recv(1024)
    print(data.decode('utf8'))
    rep_data = input()
    # 发送数据需要是 bytes 类型
    sock.send(rep_data.encode('utf8'))
# server.close()
# sock.close()