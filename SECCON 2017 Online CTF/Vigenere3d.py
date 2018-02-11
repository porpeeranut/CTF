import sys
def _l(idx, s):
	return s[idx:] + s[:idx]

def main(data, k1, k2, encrypt=False):
	s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
	t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
	i1 = 0
	i2 = 0
	if encrypt:
		c = ""
		for a in data:
			c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
			i1 = (i1 + 1) % len(k1)
			i2 = (i2 + 1) % len(k2)
		return c
	else:
		decrypted = ""
		for a in data:
			for c in s:
				if t[s.find(c)][s.find(k1[i1])][s.find(k2[i2])] == a:
					decrypted += c
					break
			i1 = (i1 + 1) % len(k1)
			i2 = (i2 + 1) % len(k2)
		return decrypted

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
cipher = 'POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9'
plain = 'SECCON{__________________________}'
key = '______________'
for i in range(len(cipher[:7])):
	for k in LETTERS:
		tmpkey = key[:i] + k + key[(i+1):]
		if main(plain, tmpkey, tmpkey[::-1], encrypt=True)[:i+1] == cipher[:i+1]:
			key = tmpkey
			print key, main(plain, key, key[::-1], encrypt=True)[:i+1]
			break
print main(cipher, key, key[::-1], encrypt=False)