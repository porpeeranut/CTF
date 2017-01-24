import sys, socket, morse_talk

host = "146.148.102.236"
port = 24069

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print s.recv(1024)
charset = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

s.send("x\n")
for i in range(250):
	recv = s.recv(2024)
	print recv
	print i
	if i < 50:
		code = recv.split('What is')[1].split(' decrypted?')[0].strip()
		code = code.split('  ')
		decode = ''
		for c in code:
			decode += morse_talk.decode(c)+' '
		decode = decode[:-1]
		print "\n", decode
		s.send(decode+"\n")
	elif i < 100:
		code = recv.split('What is ')[1].split(' decrypted?')[0]
		decode = ''
		for c in code:
			decode += charset[(charset.index(c)+82)%len(charset)]
		print decode
		s.send(decode+"\n")
	elif i < 150:
		plain = 'abcdefghijklmnopqrstuvwxyz. '
		enc1 = 'axje.uidchtnmbrl\'poygk,qf;v '
		enc2 = 'abcsftdhuneimky;qprglvwxjz. '
		enc = recv.split('encrypted is')[1].split('What is')[0].strip()
		code = recv.split('What is ')[1].split(' decrypted?')[0]
		decode = ''
		if 'f' in enc:
			for c in code:
				decode += plain[enc1.index(c)]
		else:
			for c in code:
				decode += plain[enc2.index(c)]
		print decode
		s.send(decode+"\n")
	elif i < 200:
		enc = recv.split('encrypted is')[1].split('What is')[0].strip()
		rot = charset.index('y')-charset.index(enc)
		code = recv.split('What is ')[1].split(' decrypted?')[0]
		print "rot", rot
		decode = ''
		for c in code:
			decode += charset[(charset.index(c)+rot)%len(charset)]
		print decode
		s.send(decode+"\n")
	elif i < 250:
		encset = '~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\'&%$#"!'
		code = recv.split('What is ')[1].split(' decrypted?')[0]
		decode = ''
		for c in code:
			decode += charset[encset.index(c)]
		print decode
		s.send(decode+"\n")
	recv = s.recv(2024)
	print recv
	s.send("y\n")
s.close()