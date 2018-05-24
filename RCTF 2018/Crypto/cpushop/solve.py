# https://www.whitehatsec.com/blog/hash-length-extension-attacks/

import hashpumpy, hashlib, socket

#print help(hashpumpy.hashpump)

for i in range(8, 33):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = "cpushop.2018.teamrois.cn"
	s.settimeout(3)
	s.connect((host, 43000))
	data = s.recv(120)
	# print data

	s.send('1\n')
	data = s.recv(1024)
	# print data

	s.send('2\n')
	data = s.recv(1024)+s.recv(1024)
	# print data

	s.send('1\n')
	data = s.recv(1024)
	# print data
	secret = 'x'*i
	knownMsg = data.split('Your order:\n')[1].split('&sign=')[0]
	knownHash = data.split('&sign=')[1].strip()
	extensionMsg = '&product=Flag&price=1'
	print knownMsg
	print knownHash
	try:
		newHash, newMsg = hashpumpy.hashpump(knownHash, knownMsg, extensionMsg, len(secret))
	except:
		print 'ERROR', i
		continue
	print newMsg.encode('string_escape')

	s.send('3\n')
	data = s.recv(1024)
	# print data

	s.send(newMsg+'&sign='+newHash+'\n')
	data = s.recv(1024)+s.recv(1024)
	print i
	if 'Invalid Order' not in data:
		print data
		exit()