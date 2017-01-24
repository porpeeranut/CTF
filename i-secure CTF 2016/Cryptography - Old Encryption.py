import base64

enc = 'PAbfR0TmKAxzGRHzS0Vfw0U3'

caesarKey = 6
caesarDecrypted = ''
for c in enc:
	if c.isalpha():
		offset = ord('a') if c.islower() else ord('A')
		c = ord(c) - offset
		c = (c + caesarKey) % 26
		caesarDecrypted += chr(c + offset)
	else:
		caesarDecrypted += c
print base64.b64decode(caesarDecrypted)