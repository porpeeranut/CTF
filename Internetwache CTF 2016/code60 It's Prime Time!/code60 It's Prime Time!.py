import sys
import socket

#	https://ctf.internetwache.org/tasks/code/60

host = "188.166.133.53"
port = 11059

def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print s.recv(1024)
for i in range(101):
	recv = s.recv(1024)
	print recv
	prime = int(recv.split("after ")[1].split(":")[0])
	next_primt = find_next_prime(prime+1)
	print next_primt
	s.send(str(next_primt))
	recv = s.recv(1024)
	print recv
s.close()