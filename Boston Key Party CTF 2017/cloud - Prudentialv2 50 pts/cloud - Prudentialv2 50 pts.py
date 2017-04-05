import requests

'''
https://shattered.io/
https://alf.nu/SHA1
https://twitter.com/marcan42/status/835175023425966080/photo/1
https://shattered.io/static/shattered.pdf
https://shattered.io/static/pdf_format.png
https://github.com/cr-marcstevens/sha1collisiondetection

https://news.ycombinator.com/item?id=13728294
'The first 320 bytes of the two PDFs released by Google result in the same SHA-1 state'
'''

def urlencode(data):
	out = ''
	for c in data:
		out += '%'+c.encode('hex')
	return out

# solution 1
r = requests.get('http://54.202.82.13/?name='+urlencode(open('a.pdf').read())+'&password='+urlencode(open('b.pdf').read()))
print r.text

# solution 2
r = requests.get('http://54.202.82.13/?name='+urlencode(open('shattered-1.pdf').read()[:320])+'&password='+urlencode(open('shattered-2.pdf').read()[:320]))
print r.text