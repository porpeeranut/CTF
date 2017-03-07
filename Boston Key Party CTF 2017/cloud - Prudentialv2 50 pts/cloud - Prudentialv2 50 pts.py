import requests

# https://shattered.io/
# https://alf.nu/SHA1
# https://twitter.com/marcan42/status/835175023425966080/photo/1
# https://shattered.io/static/shattered.pdf
# https://shattered.io/static/pdf_format.png
# https://github.com/cr-marcstevens/sha1collisiondetection

def readfile(filename):
	f = open(filename).read()
	out = ''
	for c in f:
		out += '%'+c.encode('hex')
	return out

r = requests.get('http://54.202.82.13/?name='+readfile('a.pdf')+'&password='+readfile('b.pdf'))
print r.text