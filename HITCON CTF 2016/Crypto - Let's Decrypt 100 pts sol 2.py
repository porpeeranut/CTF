import socket, math, binascii, sys

HOST = "52.69.125.71"  
PORT = 4443

#	padding oracle with pkcs7
def splitHexStrToBlock(hex, sizeInByte):
	return [hex[i:i+sizeInByte*2] for i in range(0, len(hex), sizeInByte*2)]

def replaceByteInHexStr(hexStr, bytePos, val):
	return hexStr[:bytePos*2] + '%02x' % (val) + hexStr[(bytePos*2+2):]

def fillZero(hexStr, strLen):
	return ('0' * (strLen - len(hexStr))) + hexStr

def isPadCorrect(cipherStr):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))

	sys.stdout.write("\r" + cipherStr)
	sys.stdout.flush()
	s.recv(1024)
	s.recv(1024)
	s.sendall("2\n")
	s.sendall(cipherStr + "\n")
	plain = s.recv(1024)
	plain += s.recv(1024)
	if 'bad decrypt' in plain:
		return False
	else:
		print
		print plain.strip()
		return True

def oracleAttack(cipherStr, blkPosition, blkSizeInByte):
	cipher = splitHexStrToBlock(cipherStr, blkSizeInByte)

	cipher[-1] = cipher[blkPosition]
	inmdBlock = '99'*b_size
	pBlockToXorWthiIntmd = '54686520717569636b2062726f776e20'

	# insert mal cipher block
	mal_c = '22'*b_size
	tmp = cipher[-1]
	cipher[-1] = mal_c
	cipher.append(tmp)

	# loop cipher from last byte
	for b in range(blkSizeInByte-1, -1, -1):
		strt = 0
		if b == blkSizeInByte - 1:
			strt = 0x65
		elif b == blkSizeInByte - 2:
			strt = 0x34
		elif b == blkSizeInByte - 3:
			strt = 0x54
		elif b == blkSizeInByte - 4:
			strt = 0x11
		elif b == blkSizeInByte - 5:
			strt = 0x1b
		elif b == blkSizeInByte - 6:
			strt = 0x14
		elif b == blkSizeInByte - 7:
			strt = 0x7
		elif b == blkSizeInByte - 8:
			strt = 0x35
		elif b == blkSizeInByte - 9:
			strt = 0x23
		elif b == blkSizeInByte - 10:
			strt = 0x43
		elif b == blkSizeInByte - 11:
			strt = 0x13
		elif b == blkSizeInByte - 12:
			strt = 0x4d
		elif b == blkSizeInByte - 13:
			strt = 0x49
		elif b == blkSizeInByte - 14:
			strt = 0x5
		elif b == blkSizeInByte - 15:
			strt = 0x53
		elif b == blkSizeInByte - 16:
			strt = 0x16

		for val in range(strt, 256):
			cipher[-2] = replaceByteInHexStr(cipher[-2], b, val)
			if isPadCorrect(''.join(cipher)):
				padVal = blkSizeInByte-b
				padStr = '%02x' % (padVal) * padVal
				inmdBlock = inmdBlock[:(blkSizeInByte-padVal)*2] + fillZero(hex(int(padStr,16) ^ int(cipher[-2][-padVal*2:],16)).replace('0x','').replace('L',''), padVal*2)
				print 'pad', padVal
				print 'value %x' % val
				iv = fillZero(hex(int(pBlockToXorWthiIntmd[-padVal*2:],16) ^ int(inmdBlock[-padVal*2:],16)).replace('0x','').replace('L',''), padVal*2).decode('hex')
				print iv

				# change mal cipher block for next round
				padVal += 1
				padStr = '%02x' % (padVal) * padVal
				cipher[-2] = cipher[-2][:(blkSizeInByte-padVal)*2] + fillZero(hex(int(padStr,16) ^ int(inmdBlock[-padVal*2:],16)).replace('0x','').replace('L',''), padVal*2)
				break

c = "4a5b8d0034e5469c071b60000ca134d9e04f07e4dcd6cf096b47ba48b357814e4a89ef1cfad33e1dd28b892ba7233285"
b_size = 16

oracleAttack(c, 0, 16)