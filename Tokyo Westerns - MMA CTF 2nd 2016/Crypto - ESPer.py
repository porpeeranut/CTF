import hashlib, sys, socket, hashlib, random, string, itertools, re, libnum, sympy

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def decrypt(p, q, e, n, ct):
    phi = (p - 1 ) * (q - 1)
    d = libnum.invmod(e, phi)
    pt = pow(ct, long(d), n)
    return libnum.n2s(pt)

host = "cry1.chal.ctf.westerns.tokyo"
port = 37992

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
recv = s.recv(1024)
print recv
recv = recv.split(' and ')[1]
recv = recv.split(' <= number <= ')
number = int(recv[0])
max = int(recv[1])
	
while(number < max):
	if hashlib.sha1(str(number)).hexdigest().startswith('00000'):
		s.send(str(number)+'\n')
		break
	number += 1
while(True):
	recv = s.recv(1024)
	print recv
	if 'Your choice>' in recv:
		break

# -------------- encrypt
# s.send('1\n')
# print s.recv(1024)
# s.send('1:e\n')
# print s.recv(1024)
# s.send('123456789\n')
# enc = s.recv(1024).split('Encrypted: ')[1]
# print 'Encrypted: ', enc
# print s.recv(1024)

enc = '1'
# -------------- decrypt
s.send('2\n')
print s.recv(1024)
s.send('7:m2\n')
print s.recv(1024)
s.send(enc+'\n')
m_result1 = s.recv(1024).split('Decrypted: ')[1]
print 'Decrypted: ', m_result1
print s.recv(1024)

enc = '1'
# -------------- decrypt
s.send('2\n')
print s.recv(1024)
s.send('7:m2\n')
print s.recv(1024)
s.send(enc+'\n')
m_result2 = s.recv(1024).split('Decrypted: ')[1]
print 'Decrypted: ', m_result2
print s.recv(1024)

q = gcd(long(m_result1)-1, long(m_result2)-1)

enc = '1'
# -------------- decrypt
s.send('2\n')
print s.recv(1024)
s.send('7:m1\n')
print s.recv(1024)
s.send(enc+'\n')
m_result1 = s.recv(1024).split('Decrypted: ')[1]
print 'Decrypted: ', m_result1
print s.recv(1024)

enc = '1'
# -------------- decrypt
s.send('2\n')
print s.recv(1024)
s.send('7:m1\n')
print s.recv(1024)
s.send(enc+'\n')
m_result2 = s.recv(1024).split('Decrypted: ')[1]
print 'Decrypted: ', m_result2
print s.recv(1024)

p = gcd(long(m_result1)-1, long(m_result2)-1)
print 'p: %d\nq: %d\n' % (p, q)

if not sympy.isprime(p):
    print 'p not prime'
    sys.exit(0)
if not sympy.isprime(q):
    print 'q not prime'
    sys.exit(0)

# -------------- exit
s.send('4\n')
flag_enc = long(s.recv(1024).split('is here.')[1].strip())
print decrypt(long(p), long(q), 65537L, long(p*q), flag_enc)

# -------------- about
#s.send('3\n')

s.close()