import sys

#	usage
#	strings ./flag.pcapng | grep Host | python python "misc80 404 Flag not found.py"

#	Description
#	decrypt url in DNS packet to ascii.
#	flag is the first char of each packet.

flag = ''
hex = ''
text = ''
for line in sys.stdin:
	line = line.replace("Host: ", "")
	line = line.replace(".2015.ctf.internetwache.org", "")
	line = line.strip()
	hex += line
text = hex.decode('hex')
text = text.split("\n")
for line  in text:
	flag += line[0:1]
print "flag:",flag