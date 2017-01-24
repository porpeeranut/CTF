import base64

def xor(s1, s2):
    res = [chr(0)]*12
    for i in range(len(s1)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

with open('sleeping.png.enc') as f:
    data = f.read()
    data = base64.b64decode(data)

    key = ''
    png_signature = '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d'
    dec_data = ''
    key = xor(data[0:12], png_signature)
    for i in range(0, len(data), 12):
        enc = xor(data[i:i+12], key)
        dec_data += enc

    with open('sleeping.png', 'wb') as fo:
        fo.write(dec_data)