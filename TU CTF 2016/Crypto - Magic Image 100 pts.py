#!/usr/bin/env python

def xor(s1, s2):
    res = [chr(0)]*12
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

def add_pad(msg):
    l = 12 - len(msg)%12
    msg += chr(l)*l
    return msg

with open('encrypted.png', 'rb') as f:
    data = f.read()

key = ''
png_signature = '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d'
dec_data = ''
key = xor(data[0:12], png_signature)
for i in range(0, len(data), 12):
    enc = xor(data[i:i+12], key)
    dec_data += enc
with open('decrypted.png', 'wb') as f:
    f.write(dec_data)