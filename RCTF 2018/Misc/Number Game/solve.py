import hashlib, socket, re, string, itertools, random, time, libnum

# mastermind

def proofOfWork(text, sha):
	for XXXX in itertools.product(string.ascii_letters+string.digits, repeat=4):
		plain = ''.join(XXXX)+text
		if hashlib.sha256(plain).hexdigest() == sha:
			print plain
			return plain

def check_1a2b(correct, guess):
	##Prompts user input and appends the result to guess_list as str. "3428" as ["3","4","2","8"]
	guess_list = []
	correct = correct.split(' ')

	def guess_to_list(guess):
		for num in guess:
			guess_list.append(num)

	guess_to_list(guess.split(' '))

	##Calculate total of As and Bs
	##Count correct num in incorrect possitions    
	def Count_B():
		total_B = 0
		for i in range(4):
			if guess_list[i] != correct[i]:
				if guess_list[i] in correct:
					total_B += 1
		return total_B

	##Count correct num in correct positions
	total_A = 0
	for each in range(4):
		if guess_list[each] == correct[each]:
			total_A = total_A + 1

	if total_A == 4:
		print "You win! Congrats!"
	else:
		return 'Nope. '+str(total_A)+', '+str(Count_B())

maxR = 0
while(True):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = "149.28.139.172"
	s.settimeout(3)
	s.connect((host, 10002))
	data = s.recv(120)
	sha = data.split(' == ')[1].strip()
	text = re.findall(r'\+(\w{16})', data)[0]
	print data
	print s.recv(1024)
	# print text, sha

	plain = proofOfWork(text, sha)
	s.send(plain)
	print s.recv(2048) # banner
	print s.recv(2048) # challenge
	anss = ['1 2 3 4', '5 6 7 8', '9 0 1 2', '4 5 8 9', '2 4 6 8', '4 6 8 0']

	for r in range(100):
		serverAns = []
		for ans in anss[:-1]:
			s.send(ans)
			print ans
			res = s.recv(2048)
			print res
			if 'Nope' in res:
				serverAns.append(re.findall('Nope. \d, \d', res)[0])

		for ans in range(9999, 0, -1):
			ans = str(ans).zfill(4)
			match = True
			if ans[0] != ans[1] and ans[0] != ans[2] and ans[0] != ans[3] and ans[1] != ans[2] and ans[1] != ans[3] and ans[2] != ans[3]:
				ans = ' '.join(ans)
			else:
				continue
			for i, sent in enumerate(anss[:-1]):
				if serverAns[i] != check_1a2b(ans, sent):
					match = False
					break
			if match:
				print 'match', ans
				break
		s.send(ans)
		print ans
		res = s.recv(2048)
		print res, '---------------------', r
		if maxR < r:
			open('log','a').write(res+' '+str(r)+'\n')
			maxR = r
		if 'Flag' in res:
			exit()
		if 'You lose' in res:
			break
		else:
			res = s.recv(2048)
			print res