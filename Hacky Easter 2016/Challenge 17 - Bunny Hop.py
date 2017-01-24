import sys, codecs
from PIL import Image
# -*- coding: utf-8 -*-

reload(sys)
sys.setdefaultencoding('utf-8')

eggMap = []
mapWidth = 27
direction = 'right'
idxRow = 1
idxCol = 1

def initMap():
	row = ['.'] * mapWidth
	for i in range(mapWidth):
		eggMap.append(list(row))

def dropEgg(row, col):
	global direction, idxRow, idxCol
	print "drop ", row, col
	eggMap[row][col] = '#'

def dropLineOfEggs(length):
	global direction, idxRow, idxCol
	for i in range(length):
		dropEgg(idxRow, idxCol)
		hop(1)
	turn('left', '180')
	hop(1)
	turn('left', '180')

def hop(num):
	global direction, idxRow, idxCol
	if direction == 'up':
		idxRow = idxRow - num
	elif direction == 'down':
		idxRow = idxRow + num
	elif direction == 'left':
		idxCol = idxCol - num
	elif direction == 'right':
		idxCol = idxCol + num
	if idxCol < 0 or idxRow < 0 or idxRow >= mapWidth or idxCol >= mapWidth:
		print "exceed hop ", idxRow, idxCol

def turn(direct, angle):
	global direction
	if angle == '90':
		if 'left' in direct:
			if direction == 'up':
				direction = 'left'
			elif direction == 'down':
				direction = 'right'
			elif direction == 'left':
				direction = 'down'
			elif direction == 'right':
				direction = 'up'
		elif 'right' in direct:
			if direction == 'up':
				direction = 'right'
			elif direction == 'down':
				direction = 'left'
			elif direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	elif angle == '180':
		if direction == 'up':
			direction = 'down'
		elif direction == 'down':
			direction = 'up'
		elif direction == 'left':
			direction = 'right'
		elif direction == 'right':
			direction = 'left'

def printMap():
	for row in eggMap:
		for col in row:
			if "." in col:
				sys.stdout.write(" ")
			else:
				sys.stdout.write(col)
		print

def moveAndDropEgg():
	with open('test.txt') as f:
		for line in f:
			line = line.strip()
			print "-----------", line
			if 'lineofeggs' in line:
				dropLineOfEggs(int(line.split(" ")[1]))
			elif 'egg' in line:
				dropEgg(idxRow, idxCol)
			elif 'hop' in line:
				hop(int(line.split(" ")[1])/10)
			elif 'right' in line or 'left' in line:
				turn(line.split(" ")[0], line.split(" ")[1])

def writePng():
	pixels_out = []
	for row in eggMap:
		for tup in row:
			if tup == '#':
				pixels_out.append((0,0,0))
			elif tup == '.':
				pixels_out.append((255,255,255))
	image_out = Image.new("RGB", (mapWidth, mapWidth), "white")
	image_out.putdata(pixels_out)
	image_out.save('test_out.png')

initMap()
moveAndDropEgg()
printMap()
writePng()