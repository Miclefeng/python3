import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

while True:
    send_data = input()
    client.send(send_data.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))
# client.closeI`