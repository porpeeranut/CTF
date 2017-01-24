import socket, math, binascii, sys, base64, re, textwrap, urllib, urllib2, requests, copy, string

#   padding oracle with pkcs7
def splitHexStrToBlock(hex, sizeInByte):
    return [hex[i:i+sizeInByte*2] for i in range(0, len(hex), sizeInByte*2)]

def replaceByteInHexStr(hexStr, bytePos, val):
    return hexStr[:bytePos*2] + '%02x' % (val) + hexStr[(bytePos*2+2):]

def fillZero(hexStr, strLen):
    return ('0' * (strLen - len(hexStr))) + hexStr

def isPadCorrect(cipherStr):
    token = base64.b64encode(cipherStr.decode('hex'))
    values = {'matrix-id' : token}
    r = requests.post('http://crypto.chal.csaw.io:8001/', data=values, allow_redirects=False)
    if 'exception' not in r.text:
        return True
    else:
        return False

def oracleAttack(cipherStr, blkPosition, blkSizeInByte):
    cipher = splitHexStrToBlock(cipherStr, blkSizeInByte)

    cipher[-1] = cipher[blkPosition]
    inmdBlock = 'ff'*b_size
    cBlockToXorWthiIntmd = cipher[-(len(cipher)-(blkPosition-1))]

    # insert mal cipher block
    mal_c = 'ee'*b_size
    tmp = cipher[-1]
    cipher[-1] = mal_c
    cipher.append(tmp)

    # loop cipher from last byte
    for b in range(blkSizeInByte-1, -1, -1):
        for val in range(256):
            cipher[-2] = replaceByteInHexStr(cipher[-2], b, val)
            sys.stdout.write("\r" + '%3d' % val)
            sys.stdout.flush()
            if isPadCorrect(''.join(cipher)):
                padVal = blkSizeInByte-b
                padStr = '%02x' % (padVal) * padVal
                inmdBlock = inmdBlock[:(blkSizeInByte-padVal)*2] + fillZero(hex(int(padStr,16) ^ int(cipher[-2][-padVal*2:],16)).replace('0x','').replace('L',''), padVal*2)
                print 'pad', padVal
                print 'value %x' % val
                plain = fillZero(hex(int(cBlockToXorWthiIntmd[-padVal*2:],16) ^ int(inmdBlock[-padVal*2:],16)).replace('0x','').replace('L',''), padVal*2).decode('hex')
                print plain+'\n'

                # change mal cipher block for next round
                padVal += 1
                padStr = '%02x' % (padVal) * padVal
                cipher[-2] = cipher[-2][:(blkSizeInByte-padVal)*2] + fillZero(hex(int(padStr,16) ^ int(inmdBlock[-padVal*2:],16)).replace('0x','').replace('L',''), padVal*2)
                break

token = 'EWS8Jk/BYA2EHrWP65W+7+kWHleH47lMpMgR70/zthxE9jXyJawDAH0iVMvow7G9YdxcId5Y3qaVhS8aHnVHtvy+lKLPioIWxNHSv7PQmLY='
c = base64.b64decode(token).encode('hex')
b_size = 16

oracleAttack(c, 1, 16)