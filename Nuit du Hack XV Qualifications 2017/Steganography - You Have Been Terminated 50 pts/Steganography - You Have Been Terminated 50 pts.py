# -*- coding: utf-8 -*-
from PIL import Image
from numpy import *

im = array(Image.open("o.jpg"))
N = im.shape[0]

# create x and y components of Arnold's cat mapping
x,y = meshgrid(range(N),range(N))
xmap = (2*x+y) % N
ymap = (x+y) % N

for i in xrange(N+1):
	result = Image.fromarray(im)
	result.save("cat_%03d.png" % i)
	im = im[xmap,ymap]