import sys, socket, base64
from PIL import Image

def decodeVerticode(filename):
	im = Image.open(filename)
	pix = im.load()
	width, height = im.size
	pxPerBox = 12
	ans = ''
	for h in range(0, height, pxPerBox):
		colorShift = 0
		code = ''
		for w in range(6*pxPerBox, width, pxPerBox):
			r, g, b = pix[w, h]
			if w == 6*pxPerBox:
				# is first box
				if r == 255 and g == 0 and b == 0:
					colorShift = 0
				elif r == 128 and g == 0 and b == 128:
					colorShift = 1
				elif r == 0 and g == 0 and b == 255:
					colorShift = 2
				elif r == 0 and g == 128 and b == 0:
					colorShift = 3
				elif r == 255 and g == 255 and b == 0:
					colorShift = 4
				elif r == 255 and g == 165 and b == 0:
					colorShift = 5
			else:
				if r == 255:
					code += '0'
				else:
					code += '1'
		ans += chr(int(code,2)-colorShift)
	return ans

host = "problems1.2016q1.sctf.io"
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

for i in range(201):
	recv = s.recv(2024)
	if i == 200:
		print recv
		break
	recv = recv.replace('<html><img src=\'data:image/png;base64,', '')
	recv = recv.replace('\'></img>', '')

	image = base64.b64decode(recv)
	filename = "im"+str(i)+".png"
	with open(filename, 'wb') as f:
		f.write(image)
	dec = decodeVerticode(filename)
	s.send(dec)
	print dec
s.close()