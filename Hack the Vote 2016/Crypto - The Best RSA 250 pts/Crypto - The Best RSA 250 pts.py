import libnum, os

def get_private_exponent(phi, e):
	return libnum.modular.invmod(e, phi)
		
def primes_under(n):
	# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	sieve = [True] * (n+1)
	primes = []
	for p in range(2, n+1):
		if (sieve[p]):
			#print p
			primes.append(p)
			for i in range(p, n+1, p):
				sieve[i] = False
	return primes

def find_factors(n, h):
	primes = primes_under(h)
	factors = {}
	for p in primes:
		while n % p == 0:
			n = n / p
			if p in factors:
				factors[p] +=1
			else:
				factors[p] = 1
	return factors
	
data = open("best_rsa.txt").read()
data = data.split('\n')
e = long(data[0].replace('e = ', ''))
n = long(data[1].replace('n = ', ''))
cipher_text = long(data[2].replace('c = ', ''))
print '[+] Factoring n...'
single_factors = find_factors(n, 10000)
phi = n
print '[+] Computing phi...'
for p in single_factors:
	phi = phi / p * (p - 1)
print '[+] Computing private exponent'
d = get_private_exponent(phi, e)

print '[+] Computing for CRT'
remainders = []
moduli = []
for p in single_factors:
	modulus = pow(p, single_factors[p])
	moduli.append(modulus)

	phi_m = (p ** (single_factors[p] - 1)) * (p - 1)
	c = cipher_text % modulus
	remainder = pow(c, d % phi_m, modulus)
	remainders.append(remainder)
print '[+] Solving CRT'
plaintext = libnum.modular.solve_crt(remainders, moduli)
with open('flag.gif', 'wb') as fp:
	fp.write(hex(plaintext)[2:-1].decode('hex'))