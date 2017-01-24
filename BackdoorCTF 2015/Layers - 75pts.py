'''
https://backdoor.sdslabs.co/challenges/LAYERS

decode "624870365a446f764c32527a59587076636d746d4c6e466c5a7938786355524f626d307a51673d3d"
to ascii --> "bHp6ZDovL2RzYXpvcmtmLnFlZy8xcURObm0zQg=="

and decode to base64 --> "lzzd://dsazorkf.qeg/1qDNnm3B"

and ROT with this pattern
a 18
b 16
c 14
d 12
e 10
f 8
g 6
h 4
i 2
j 0
k 24
l 22
m 20
n 18
o 16
p 14
q 12
r 10
s 8
t 6
u 4
v 2
w 0
x 24
y 22
z 20

then got a link "http://pastebin.com/1cPFfg3R"

'''

text = "lzzd://dsazorkf.qeg/1qDNnm3B"
textOut = ""
shift = [0] * 26
tmp = 18
i = 0
while i < len(shift):
	shift[i] = tmp
	if tmp > 0:
		tmp = tmp - 2
	else:
		tmp = 24
	i = i+1
	
for ch in text:
	rot = 0
	if (ch >= 'A' and ch <= 'Z'):
		rot = shift[ord(ch) - ord('A')]
		if ord(ch)+rot > ord('Z'):
			textOut += chr((ord('A')+(ord(ch)+rot - ord('Z')))-1)
		else:
			textOut += chr(ord(ch)+rot)
	elif (ch >= 'a' and ch <= 'z'):
		rot = shift[ord(ch) - ord('a')]
		if ord(ch)+rot > ord('z'):
			textOut += chr((ord('a')+(ord(ch)+rot - ord('z')))-1)
		else:
			textOut += chr(ord(ch)+rot)
	else:
		textOut += ch
print textOut