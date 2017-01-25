import pyperclip, hashlib
import itertools

# Vigenere

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}'

def getKeyFromPlainText(cipher, plain):
	return decrypt(plain, cipher)

def main():
	plain = 'SECCON{'
	cipher = 'LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ'
	key = getKeyFromPlainText(cipher[:7], plain) + 'EXXXX'

	for xs in itertools.product(LETTERS, repeat=4):
		key = key[:8] + ''.join(xs)
		h = hashlib.md5()
		h.update(decrypt(key, cipher))
		if 'f528a6ab914c1ecf856a1d93103948fe' in h.hexdigest():
			print 'key', key, decrypt(key, cipher)
			exit()
	
def decrypt(key, ciphertext):
	pairs = zip(ciphertext, itertools.cycle(key))
	result = ''
	for pair in pairs:
		total = reduce(lambda x, y: LETTERS.index(x) - LETTERS.index(y), pair)
		result += LETTERS[total % len(LETTERS)]
	return result

if __name__ == '__main__':
	main()