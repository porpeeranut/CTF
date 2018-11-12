from PIL import Image

im = Image.open('the_milky_way.png')
pix = im.load()
imlist = []
width1, height1 = im.size
flag = ''
for h in range(height1):
	for w in range(width1):
		if pix[w, h][0] == 255 and pix[w, h][1] == 255 and pix[w, h][2] == 255:
			flag += chr(w)+chr(h)
print flag