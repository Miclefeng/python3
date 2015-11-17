#!/usr/bin/env python
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
udpCliSock = socket(AF_INET,SOCK_DGRAM)
udpCliSock.connect(ADDR)
while True:
	data = input('>')
	if not data:
		break
	udpCliSock.send(('%s\r\n' % data).encode())
	data = udpCliSock.recv(BUFSIZ).decode()
	if not data:
		break
	print(data.strip())
udpCliSock.close()