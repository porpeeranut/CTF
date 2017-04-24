import zlib

'''
ref: http://blog.dragonsector.pl/2013/08/ufo-ctf-2013-broken-brokoli-forensics.html
'''

raw = open("zipper_50d3dc76dcdfa047178f5a1c19a52118.zip", "rb").read()

CSIZE   = int(raw[0x12:0x16][::-1].encode('hex'), 16)
DSIZE  = int(raw[0x16:0x1a][::-1].encode('hex'), 16)

for OFFSET in range(0x1e, len(raw)-CSIZE):
	d = raw[OFFSET:OFFSET+CSIZE]
	for m in [ "\x78\x01", "\x78\x9C", "\x78\xDA" ]:
		try:
			o = zlib.decompressobj().decompress(m + d, DSIZE)
			open("out.%.2x%.2x" % (ord(m[0]), ord(m[1])), "wb").write(o)
		except:
			pass