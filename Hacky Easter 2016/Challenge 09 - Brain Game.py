# -*- coding: utf-8 -*-

import sys
import codecs
import sys 

# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# print(u'e with obfuscation: ♔ ö')

# sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
# print u"Stöcker"                # works

def play(black, white, command):
	for cmd in command:
		cmdW, cmdB = cmd.split(" ")
		(isCapture, pos) = move(white, cmdW)
		if isCapture:
			capture(black, pos)
		(isCapture, pos) = move(black, cmdB)
		if isCapture:
			capture(white, pos)

def move(pieces, cmd):
	if len(cmd) == 2:
		minMove = 8
		for key, value in pieces.iteritems():
			if 'P' in key and cmd[0] in value:
				mv = abs(int(value[1]) - int(cmd[1]))
				if mv < minMove:
					minMove = mv
					mvKey = key
		pieces[mvKey] = cmd
	else:
		cmd = cmd.replace("+", "")
		if '-' not in cmd:
			piece = cmd[0]
			pos = cmd[-2:]
			if piece == 'N':
				if not checkMoveKnight(pieces, 'N1', pos):
					checkMoveKnight(pieces, 'N2', pos)
			elif piece == 'B':
				if not checkMoveBishop(pieces, 'B1', pos):
					checkMoveBishop(pieces, 'B2', pos)
			elif piece == 'R':
				if not checkMoveRook(pieces, 'R1', pos):
					checkMoveRook(pieces, 'R2', pos)
			elif piece == 'K' or piece == 'Q':
				pieces[piece+'1'] = pos
			if 'x' in cmd:
				#	makes a capture on position
				if piece.islower():
					#	capture by pawn
					for key, value in pieces.iteritems():
						if 'P' in key and piece in value:
							pieces[key] = pos
				return (True, pos)
		elif 'O-O' == cmd:
			#	castled kingside (right)
			pieces['K1'] = chr(ord(pieces['K1'][0])+2) + pieces['K1'][1]
			pieces['R2'] = chr(ord(pieces['K1'][0])-1) + pieces['K1'][1]
		elif 'O-O-O' == cmd:
			#	castled queenside (left)
			pieces['K1'] = chr(ord(pieces['K1'][0])-2) + pieces['K1'][1]
			pieces['R1'] = chr(ord(pieces['K1'][0])+1) + pieces['K1'][1]
	return (False, '')

def capture(pieces, pos):
	for key, value in pieces.iteritems():
		if pos in value:
			pieces[key] = ''

def checkMoveBishop(pieces, piece, pos):
	if len(pieces[piece]) == 0:
		return False
	mvH = abs(ord(pieces[piece][0]) - ord(pos[0]))
	mvV = abs(int(pieces[piece][1]) - int(pos[1]))
	if (mvV == mvH):
		pieces[piece] = pos
		return True
	else:
		return False

def checkMoveKnight(pieces, piece, pos):
	if len(pieces[piece]) == 0:
		return False
	mvH = abs(ord(pieces[piece][0]) - ord(pos[0]))
	mvV = abs(int(pieces[piece][1]) - int(pos[1]))
	#print mvH, mvV
	if (mvV == 1 and mvH == 2) or (mvV == 2 and mvH == 1):
		pieces[piece] = pos
		return True
	else:
		return False

def checkMoveRook(pieces, piece, pos):
	if len(pieces[piece]) == 0:
		return False
	aNum = ord(pieces[piece][0])
	iNum = int(pieces[piece][1])
	mvH = abs(aNum - ord(pos[0]))
	mvV = abs(iNum - int(pos[1]))
	cnt = 1
	#	switch key, value
	tmp = {y:x for x,y in pieces.iteritems()}
	if mvV == 0:
		if ord(pos[0]) < aNum:
			cnt = -1
		for i in range(aNum+1*cnt, ord(pos[0]), cnt):
			if chr(i)+str(iNum) in tmp:
				return False
		pieces[piece] = pos
		return True
	elif mvH == 0:
		if int(pos[1]) < iNum:
			cnt = -1
		for i in range(iNum, int(pos[1]), cnt):
			if chr(aNum)+chr(i) in tmp:
				return False
		pieces[piece] = pos
		return True
	else:
		return False

def printTable(black, white):
	#	switch key, value
	black = {y:x for x,y in black.iteritems()}
	white = {y:x for x,y in white.iteritems()}
	for i in range(8, 0, -1):
		for c in range(ord('a'), ord('i')):
			pos = chr(c)+str(i)
			if pos in black:
				#print u'\u0420\u043e\u0441\u0441\u0438\u044f'
				#print u"♔"#.decode('cp65001').encode(platform_encoding)
				#print u"\u2654".encode(sys.stdout.encoding, errors='replace')
				print str('#')+black[pos],
			elif pos in white:
				print str('_')+white[pos],
			else:
				print "   ",
		print

def printAns(black, white):
	#	switch key, value
	black = {y:x for x,y in black.iteritems()}
	white = {y:x for x,y in white.iteritems()}
	ans = ''
	for i in range(8, 0, -1):
		value = ''
		for c in range(ord('a'), ord('i')):
			pos = chr(c)+str(i)
			if pos in black or pos in white:
				value += '1'
			else:
				value += '0'
		if i != 8:
			ans += '-'
		ans += str(int(value,2))
	print ans

white = {'P1': 'a2',
		'P2': 'b2',
		'P3': 'c2',
		'P4': 'd2',
		'P5': 'e2',
		'P6': 'f2',
		'P7': 'g2',
		'P8': 'h2',
		'R1': 'a1',
		'N1': 'b1',
		'B1': 'c1',
		'Q1': 'd1',
		'K1': 'e1',
		'B2': 'f1',
		'N2': 'g1',
		'R2': 'h1'}

black = {'P1': 'a7',
		'P2': 'b7',
		'P3': 'c7',
		'P4': 'd7',
		'P5': 'e7',
		'P6': 'f7',
		'P7': 'g7',
		'P8': 'h7',
		'R1': 'a8',
		'N1': 'b8',
		'B1': 'c8',
		'Q1': 'd8',
		'K1': 'e8',
		'B2': 'f8',
		'N2': 'g8',
		'R2': 'h8'}

command = ["e4 e5",
		"Nf3 Nc6",
		"Bb5 Nf6",
		"d3 Bc5",
		"O-O d6",
		"Nbd2 O-O",
		"Bxc6 bxc6",
		"h3 h6",
		"Re1 Re8",
		"Nf1 a5",
		"Ng3 Rb8",
		"b3 Bb4",
		"Bd2 Ra8",
		"c3 Bc5",
		"d4 Bb6",
		"dxe5 dxe5",
		"c4 Nh7",
		"Qe2 Nf8",
		"Be3 c5",
		"Rad1 Qf6",
		"Nh5 Qe7",
		"Nh2 Kh7",
		"Qf3 f6",
		"Ng4 Bxg4",
		"Qxg4 Red8",
		"Qf5+ Kh8",
		"f4 Rxd1",
		"Rxd1 exf4",
		"Bxf4 Qe6",
		"Rd3 Re8",
		"Nxg7 Kxg7",
		"Qh5 Nh7",
		"Bxh6+ Kh8",
		"Qg6 Qg8",
		"Bg7+ Qxg7",
		"Qxe8+ Qf8",
		"Qe6 Qh6",
		"e5 Qc1+",
		"Kh2 Qf4+",
		"Rg3 1-0"]
play(black, white, command)
printTable(black, white)
printAns(black, white)