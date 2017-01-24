from PIL import Image
import sys, numpy

im = Image.open('warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg')

width, height = im.size
pix = numpy.array(im)
tmp = numpy.zeros((height, width*2, 3))
for h in range(height):
	for w in range(width*2):
		tmp[h][w] = pix[h][w%width]
im = tmp

pix = numpy.array(im)
pixO = numpy.copy(pix)

blockHeight = 8
shift = 8
width = len(pix[0])
height = len(pix)
pixO2 = numpy.zeros((height*2, width/2, 3))

for b in range(height/blockHeight):
	for h in range(b*blockHeight, b*blockHeight+blockHeight):
		for w in range(width-(b*shift)):
			pixO[h][w] = pix[h][w+(b*shift)]

for b in range((height*2)/blockHeight):
	ho = (b/2)*blockHeight
	for h in range(b*blockHeight, b*blockHeight+blockHeight):
		for w in range(width/2):
			if b % 2 == 0:
				pixO2[h][w] = pixO[ho][w]
			else:
				pixO2[h][w] = pixO[ho][w+505]
		ho += 1

result = Image.fromarray((pixO).astype(numpy.uint8))
result.save('imgShift.png')

result = Image.fromarray((pixO2).astype(numpy.uint8))
result.save('imgOut.png')