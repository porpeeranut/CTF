import base64, cStringIO
from PIL import Image, ImageFont, ImageDraw

#	https://ctf.internetwache.org/tasks/misc/60

file = open('README.txt', 'r')
fileQR = open('qr.txt', 'w')

b64 = ""
i = 1
#	write QRcode text to .png
for line in file:
	if len(line) == 77:
		b64 += line
	else:
		b64 += line
		fileQR.write(base64.b64decode(b64))

		img = Image.new('RGB', (320, 320))
		d = ImageDraw.Draw(img)
		str = base64.b64decode(b64).decode('utf-8')

		font=ImageFont.truetype("C:\Windows\Fonts\cour.ttf",11)	# courier new
		d.text((0, 0), str, fill=(255, 255, 255), font=font)
		#d.multiline_text((0, 0), str, fill=(255, 255, 255), font=font, spacing=0)


		img.save("qr{}.png".format(i))
		i = i + 1
		b64 = ""
		#break
	#print len(line),

#	decode QRcode from .png
#
#
#
#