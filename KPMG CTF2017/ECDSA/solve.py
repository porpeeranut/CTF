import collections
from hashlib import sha1, sha256
from ecdsa import SigningKey
from ecdsa.curves import NIST192p, NIST256p
from ecdsa.numbertheory import inverse_mod
from ecdsa.ellipticcurve import Point
from ecdsa.util import sigdecode_string

# reuse nonce (k) attack
def recover_key(m1, r1, s1, m2, r2, s2):
	assert(r1==r2)
	z1 = long(sha256(m1).hexdigest(), 16)
	z2 = long(sha256(m2).hexdigest(), 16)
	n = NIST256p.order
	k = (((z1 - z2) % n) * inverse_mod(s1 - s2, n)) % n
	print 'k', k
	dA = ((((s1 * k) % n) - z1) * inverse_mod(r1, n)) % n
	print 'dA', dA	
	return k, dA

# find reused nonce (k)
r = []
sigs = {}
with open('signature.txt') as f:
	for line in f:
		line = line.strip().split(':')
		r.append(line[1])
		sigs[line[0]] = [line[1], line[2]]
reuseR = [item for item, count in collections.Counter(r).items() if count > 1]
assert reuseR
weakSigs = []
for name, sig in sigs.iteritems():
	if reuseR[0] == sig[0]:
		weakSigs.append({'m':name, 'r':long(sig[0]), 's':long(sig[1])})
k, dA = recover_key(weakSigs[0]['m'], weakSigs[0]['r'], weakSigs[0]['s'], weakSigs[1]['m'], weakSigs[1]['r'], weakSigs[1]['s'])

# sign
sk = SigningKey.from_secret_exponent(dA, curve=NIST256p, hashfunc=sha256)
m = 'Kim Jong Unji'
sig = sk.sign(m, k=k, hashfunc=sha256)
vk = sk.get_verifying_key()
pub_curve_point = Point(None, 107324307922508327618818604973232425414834705935339085689120011583634761572893, 67000007909522739173079618251159928745553160396093434285090519625295801372020)
assert sk.privkey.public_key.point._Point__x == pub_curve_point._Point__x and sk.privkey.public_key.point._Point__y == pub_curve_point._Point__y
assert vk.verify(sig, m)
r, s = sigdecode_string(sig, sk.privkey.public_key.order)
print 'KPMG{'+str(r)+':'+str(s)+'}'