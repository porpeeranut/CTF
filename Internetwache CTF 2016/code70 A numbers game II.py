import sys, socket, re

#	https://ctf.internetwache.org/tasks/code/70

def encode(eq):
    out = []
    for c in eq:
        q = bin((ord(c)^(2<<4))).lstrip("0b")
        q = "0" * ((2<<2)-len(q)) + q
        out.append(q)
    b = ''.join(out)
    pr = []
    for x in range(0,len(b),2):
        c = chr(int(b[x:x+2],2)+51)
        pr.append(c)
    s = '.'.join(pr)
    return s

def decode(enc):
    s = enc.split(".")
    b = []
    for x in s:
        dec = ord(x)-51
        bin = format(dec, '02b')	# dec to bin in format bb
        b.append(bin)
        #print bin,
    b = ''.join(b)
    b = re.findall('........', b)	# split every 8 character
    eq = []
    for bin in b:
        eq.append(chr(int(bin, 2)^(2<<4)))
    return ''.join(eq)

host = "188.166.133.53"
port = 11071

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print s.recv(2024)
for i in range(101):
	recv = s.recv(2024)
	print recv
	eqEnc = recv.split(": ")[1].strip()
	equation = decode(eqEnc)
	print equation
	z = int(equation.split(" = ")[1].strip())
	y = int(equation.split(" = ")[0].split(" ")[2].strip())
	op = equation.split(" = ")[0].split(" ")[1].strip()
	# print y
	# print z
	# print op
	if op == '+':
		print z-y
		s.send(encode(str(z-y)))
		print s.recv(2024)
	elif op == '-':
		print z+y
		s.send(encode(str(z+y)))
		print s.recv(2024)
	elif op == '*':
		print z/y
		s.send(encode(str(z/y)))
		print s.recv(2024)
	elif op == '/':
		print z*y
		s.send(encode(str(z*y)))
		print s.recv(2024)
s.close()