import binascii

flag = ''
with open('hodor.txt') as f:
	for line in f:
		if 'ho' in line:
			line = line.strip().replace('ho', '0').replace('dor', '1').split(' / ')
			for l in line:
				flag += binascii.unhexlify('%x' % int(l, 2))
print flag
