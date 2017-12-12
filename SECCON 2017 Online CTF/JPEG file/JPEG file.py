import numpy, os, time, imagehash, time
from PIL import Image

data = open('JPEG file.jpg', 'rb').read()
block = len(data)/200
for b in range(200):
	end = len(data) if len(data) < b*block+block else b*block+block
	error = []
	for i in range(b*block, end):
		x = 0b10000000
		found = False
		for bx in range(8):
			filename = str(i)+'-'+str(bx)+'.jpg'
			data = data[:i] + chr((ord(data[i])^x)) + data[(i+1):]
			open(filename, 'wb').write(data)
			data = data[:i] + chr((ord(data[i])^x)) + data[(i+1):]
			x /= 2
			try:
				hashh = imagehash.average_hash(Image.open(filename))
				print filename, hashh
				found = True
				break
			except Exception as e:
				#print e
				error.append(str(i)+'-'+str(bx)+'.jpg')
				pass
		if found:
			break
	for er in error:
		while True:
			try:
				os.remove(er)
				break
			except:
				time.sleep(0.2)
	if found:
		break