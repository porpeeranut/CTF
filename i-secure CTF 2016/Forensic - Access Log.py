import urllib, binascii

i = 1
maxVal = 0
flag = ''
with open('access.log') as a:
	for line in a:
		if 'flag' not in line:
			break
		dec = urllib.unquote(line).decode('utf8')
		dec = dec.split('LIMIT 0,1),')[1]
		dec = dec.split(' "-" "sqlmap')[0]
		dec = dec.split(')# HTTP/1.1" 200 ')
		result = dec[1]
		dec = dec[0].split(',1))>')
		chIdx = dec[0]
		chVal = dec[1]

		if i != int(chIdx):
			maxVal += 1
			try:
				flag += chr(maxVal)
			except:
				continue
			maxVal = 0
			i = i+1

		if i == int(chIdx):
			if result == '36':
				if maxVal < int(chVal):
					maxVal = int(chVal)
print flag.decode('hex')