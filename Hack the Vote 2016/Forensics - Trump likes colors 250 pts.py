from PySide.QtSvg import *
from PySide.QtGui import *
import sys, subprocess, urllib
from PIL import Image
import numpy as np

# extract APNG to PNG
# ffmpeg -i trump_likes_colors.png trump%d.png

# interpreter for piet programming language
# http://www.bertnase.de/npiet/
# http://www.dangermouse.net/esoteric/piet.html

progPath = 'C://Users//test//Downloads//npiet-1.3a-win32//'
imPath = 'C://Users//test//Desktop//CTF//Hack the Vote 2016//for//Trump likes colors//'
w, h = 128, 128
data = np.zeros((h, w, 3), dtype=np.uint8)
for i in range(16384-1):
	txt = subprocess.check_output([progPath+"npiet.exe", imPath+"trump"+str(i+1)+".png"]).strip()
	strOut = txt.decode('utf-8')
	if i < 81 and i % 2 == 1:
		r = int(prev[1:3], 16)
		g = int(prev[3:5], 16)
		b = int(prev[5:], 16)
		data[i/128, i%128] = [0 if r==0 else r-63, 0 if g==0 else g-63, 0 if b==0 else b-63]
	else:
		data[i/128, i%128] = [int(strOut[1:3], 16), int(strOut[3:5], 16), int(strOut[5:], 16)]
	prev = strOut
img = Image.fromarray(data, 'RGB')
img.save('out.png')

# txt = subprocess.check_output([progPath+"npiet.exe", imPath+"out.png"]).strip()
# print txt.decode('utf-8')