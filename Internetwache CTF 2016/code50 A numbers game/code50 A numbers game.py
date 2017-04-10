import sys
import socket

#	https://ctf.internetwache.org/tasks/code/50

host = "188.166.133.53"
port = 11027

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print s.recv(2024)
for i in range(101):
	recv = s.recv(2024)
	print recv
	equation = recv.split(": ")[1].strip()
	#print equation
	z = int(equation.split(" = ")[1].strip())
	y = int(equation.split(" = ")[0].split(" ")[2].strip())
	op = equation.split(" = ")[0].split(" ")[1].strip()
	# print y
	# print z
	# print op
	if op == '+':
		print z-y
		s.send(str(z-y))
		print s.recv(2024)
	elif op == '-':
		print z+y
		s.send(str(z+y))
		print s.recv(2024)
	elif op == '*':
		print z/y
		s.send(str(z/y))
		print s.recv(2024)
	elif op == '/':
		print z*y
		s.send(str(z*y))
		print s.recv(2024)
s.close()