# https://en.wikipedia.org/wiki/Quantum_key_distribution
import itertools, re
from Crypto.Cipher import AES

def aesDecrypt(key, iv, cipher):
	aes = AES.new(key, AES.MODE_CBC, iv)
	return aes.decrypt(cipher)

q_transmission_1 = open('q_transmission_1').read().split('\n')[2]
q_transmission_3 = open('q_transmission_3').read().split('\n')[2]

for x in set(itertools.permutations("1100")):
	shared_key = ''
	try:
		for i, t3 in enumerate(q_transmission_3):
			if t3 == 'v':
				shared_key += str(x['/-\\|'.index(q_transmission_1[i])])
		shared_key = hex(int(shared_key, 2))[2:-1].decode('hex')
		iv = re.findall("iv:(.*?),", shared_key)[0]
		key = re.findall("key:(.*?),", shared_key)[0]
		flag = '269118188444e7af980a245aedce5fb2811b560ccfc5db8e41f102a23f8d595ffde84cb1b3f7af8efd7a919bd2a7e6d3'.decode('hex')
		print aesDecrypt(key.decode("hex"), iv.decode("hex"), flag)
	except:
		pass