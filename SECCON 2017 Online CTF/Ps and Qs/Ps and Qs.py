# common factor attack in RSA
from Crypto.PublicKey import RSA
import fractions, libnum

def decrypt(p, q, e, n, ct):
	phi = (p - 1 ) * (q - 1)
	d = libnum.invmod(e, phi)
	privkey = RSA.construct((n,e,d,p,q))
	return privkey.decrypt(ct)
	#return repr(privkey.decrypt(ct))

key1 = RSA.importKey(open('pub1.pub').read())
key2 = RSA.importKey(open('pub2.pub').read())
gcd = fractions.gcd(key1.n, key2.n)
if gcd != 1:
	q = key1.n/gcd
	p = gcd
	print decrypt(p, q, key1.e, key1.n, open('cipher', 'rb').read())