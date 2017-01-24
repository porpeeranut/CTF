import sys
import socket

host = "52.197.160.186"
port = 31337

def recv(s):
	print s.recv(2024)
	print s.recv(2024)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

recv(s)
row = [1,16,18]
for r in row:
	for c in range(19):
		s.send(str(r)+' '+str(c)+'\n')
		recv(s)
recv(s)
s.close()