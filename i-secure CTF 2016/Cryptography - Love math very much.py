import base64

'''
Find flag please.

i ^ k		= 0xe112dc7fdb
j + k		= 0x21afddba257
(i & j) ^ k = 0xf2f39479d3
NOT j		= 0xfed7e95a1709

Flag = somedecode("VGhlX0ZsQGdfMXNf") + unhex(i + j - k)
'''

j = ~0xfed7e95a1709 & 0xffffffffffff
k = 0x21afddba257 - j
i = k ^ 0xe112dc7fdb
print base64.b64decode("VGhlX0ZsQGdfMXNf")+str(i + j - k)