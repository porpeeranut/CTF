import os, string, subprocess

enc = open('out').read().replace('\r\n','').lower()

def chunks(l, n):
	"""Yield successive n-sized chunks from l."""
	for i in range(0, len(l), n):
		yield l[i:i + n]

def send(p, payload):
	command = payload + '\r\n'
	p.stdin.write(command)
	for i in range(30):
		response = p.stdout.readline()
		# print response.strip(), payload[i]
		chrDict[response.strip().replace('your input:try again', '')] = payload[i]
	p.stdout.readline()

chrDict = {}
AllChars = string.printable
chrChunks = list(chunks(AllChars, 30))
for chnk in chrChunks:
	p = subprocess.Popen(['./babyre'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p.stdin.write('a\n30\n')
	if len(chnk) != 30:
		chnk += 'a'*(30-len(chnk))
	send(p, chnk)
	p.kill()
for k,v in chrDict.iteritems():
	enc = enc.replace(k, v)
print enc
