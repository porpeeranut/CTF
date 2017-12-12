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

from hashlib import sha1, sha256

shat1 = open('shattered-1.pdf').read()[:320]+'x'*(2017*1024)
shat2 = open('shattered-2.pdf').read()[:320]+'x'*(2017*1024)
print sha1(shat1).hexdigest()
print sha1(shat2).hexdigest()
print sha256(shat1).hexdigest()
print sha256(shat2).hexdigest()
open('out1', 'wb').write(shat1)
open('out2', 'wb').write(shat2)