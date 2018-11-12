flag = 'I8[7I8M*L#9_V%9FK%=5V#H%A9,_G^AiE:_BM$,cH$,9DKAMYD00'
for i in range(256):
	tmp = ''.join([chr(ord(c) + i) for c in flag])
	try:
		plain = tmp.decode('base64')
		if 'THCTF' in plain:
			print plain
			break
	except:
		pass

# THCTF{cAesaR_bAsE64_eNCoDiNg_iS_EAsY}