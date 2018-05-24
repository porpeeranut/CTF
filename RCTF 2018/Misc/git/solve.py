import os
import sys, zlib

'''
git log -g
git reflog show HEAD
git checkout f4d0f6d
'''
def decomp(pathin, pathout):
	with open(pathout, 'wb') as fout:
		with open(pathin, 'rb') as fin:
			print '---------------------'
			print zlib.decompress(fin.read())
			# fout.write(zlib.decompress(fin.read()))

if not os.path.exists('decompressed'): os.makedirs('decompressed')
for root, directories, filenames in os.walk('.git/objects'):
	for filename in filenames:
		pathin = os.path.join(root,filename)
		# print pathin
		filename = os.path.join(root,filename).split('.git/objects\\')[1].replace('\\', '')
		pathout = 'decompressed/'+filename+'.dec'
		try:
			decomp(pathin, pathout)
		except:
			print 'error', filename
			pass

