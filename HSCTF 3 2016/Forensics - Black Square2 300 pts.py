import base64, binascii
from PIL import Image

im = Image.open('BlackSquare2.png')
pix = im.load()
width, height = im.size
data = ''
for h in range(height):
	for w in range(width):
		r, g, b = pix[w, h]
		if b == 0:
			data += '0'
		else:
			data += '1'

data = binascii.unhexlify('%x' % int(data, 2))
data = base64.b64decode(data)

with open("newPng.png", 'wb') as f:
	f.write(data)

im = Image.open('newPng.png')
pix = im.load()
width, height = im.size
bin = ''
for h in range(height):
	for w in range(width):
		r, g, b = pix[w, h]
		if g == 255:
			bin += '0'
		else:
			bin += '1'

b64 = binascii.unhexlify('%x' % int(bin, 2))
plain = base64.b64decode(b64)
print plain