import base64, math

enc = "TmRmcFpVbEtmZFU="
b64dec = base64.b64decode(enc)
ans = ''
for c in b64dec:
	ans += chr(int(math.ceil(math.sqrt(ord(c)*120))))
print ans