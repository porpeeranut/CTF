# -*- coding: utf-8 -*-
from PIL import Image
import math, imagehash, os

'''
use http://gifmaker.me/exploder/ to extract gif

https://www.guballa.de/substitution-solver
http://quipqiup.com/
http://md5decrypt.net/en/Letters-frequency-analysis/
'''

def findBoundary(im):
	pix = im.load()
	width, height = im.size
	top = 0
	bottom = height
	left = 0
	right = width

	# find top
	found = False
	for h in range(height):
		for w in range(width):
			if pix[w, h] != 0:
				top = h
				found = True
				break
		if found:
			break
	# find bottom
	found = False
	for h in range(height-1, 0, -1):
		for w in range(width-1, 0, -1):
			if pix[w, h] != 0:
				bottom = h
				found = True
				break
		if found:
			break
	# find left
	found = False
	for w in range(width):
		for h in range(height):
			if pix[w, h] != 0:
				left = w
				found = True
				break
		if found:
			break
	# find right
	found = False
	for w in range(width-1, 0, -1):
		for h in range(height-1, 0, -1):
			if pix[w, h] != 0:
				right = w
				found = True
				break
		if found:
			break
	return top, bottom, left, right

def findImageHash(filename):
	im = Image.open(filename)
	top, bottom, left, right = findBoundary(im)
	ihash = imagehash.average_hash(Image.open(filename).crop((left, top, right, bottom)))
	return ihash

def convertGIFtoBlackWhiteJPG():
	print 'converting GIF to black white JPG...'
	if not os.path.exists('output/jpg'): os.makedirs('output/jpg')
	for i in range(1, 1246):
		im = Image.open('output/tmp-'+str(i)+'.gif').convert('L')
		bw = im.point(lambda x: 255 if x!=0 else 0, '1')
		bw.save('output/jpg/'+str(i)+'.jpg')

def createHashTemplate():
	print 'creating image hash template...'
	template = []
	for root, directories, filenames in os.walk('output\\template'):
		for i, filename in enumerate(filenames):
			if not os.path.exists('output/check/out'+str(i)): os.makedirs('output/check/out'+str(i))
			#print i, os.path.join(root,filename)
			template.append(findImageHash(os.path.join(root,filename)))
	return template

def mapJPGtoChar():
	out = ''
	for f in range(1, 1246):
		minDif = 99
		minInx = 99
		filename = str(f)+'.jpg'
		rt = findImageHash('output/jpg/'+filename)
		for i, r in enumerate(hTemplate):
			# bias error
			if '636.jpg' == filename:
				minInx = 16
				break
			elif '56.jpg' == filename or '71.jpg' == filename or '256.jpg' == filename or '461.jpg' == filename:
				minInx = 25
				break		

			dif = math.fabs(rt-r)
			if minDif > dif:
				minDif = dif
				minInx = i
			#print math.fabs(rt-r), r, rt
		#print minDif, minInx

		# write image for check error
		Image.open('output/jpg/'+filename).save('output/check/out'+str(minInx)+'/'+filename)

		out += chr(ord('a')+minInx)
	#out = 'alzqrsavarbrdrhiijkmanojqhphbamalzoriazpavhdzvmbddnzyzlzhkhbnmztdohbulzoriatzvlavijwznhtzbadxamayzlphbramahyxnatrbandxarvzsbwhvrhbdmztalzqrkmrbgpvzpvradhvjmdhbnhvnmdxatrvmdalzqrshmyvahdanrbqhphbojmxrgadhuhukvrdhsxzshmphvdztdxadahlszvurbgzbbddnzyzlzmrlznalzoriarbdavbadpihdtzvlukvrdhdzzurbmprvhdrzbtvzlsahdxavtzvayhmdmdxhdkmanmjlozimdzmxzssahdxavyxrbamayxhvhydavmhbnmdvaadmrgbmhbntvzllhbghdxhdkmanmdzyumjlozimdzaepvammalzdrzbmmkyxhmirgxdokiommrgbrtjrbgrbmprvhdrzbdxatrvmdmadztalzqrshmyvahdanhmphvdztrlznamlammhgrbgtahdkvamdzxaipthyrirdhdaaiaydvzbryyzllkbryhdrzbhbndzmavwahmhnrmdrbgkrmxrbgtahdkvatvzlzdxavmavwryamukvrdhyvahdandxatrvmdalzqrohmanzbdxaaepvammrzbmdxhdxazomavwanpazpialhurbghbnzdxavdxrbgmrbdxayrdjxkbnvanmztalzqryxhvhydavmsavaabyznanrbdxakbryznamdhbnhvndxahnnrdrzbmzvrgrbhiijvackamdanojgzzgiauhdlzlzrlhvunhwrmhbnlhvukmmyxavavsvzdadxatrvmdnvhtdtzvyzbmrnavhdrzbojdxakbryznadayxbryhiyzllrddaahbnhppiarbysxzmajhmkzurnhhbnpadavanoavgqzrbandxatrvmdzttryrhikdypvzpzmhisabddxvzkgxhizbgmavramztyzllabdrbgojlaloavmztdxakbryznayzbmzvdrklhbnbhdrzbhimdhbnhvnrfhdrzboznramztwhvrzkmyzkbdvramphvdryrphdrbgsxabdvhbmlrddanalzqrmjlozimhvampayrtranhmhdszojdamackabyayzbgvhdkihdrzbmrtjzkyhbvahndxrmlammhgadxatihgrmxgeaabdwejmdvasyfqkljtskegfvbnpyumrkthyjcl'
	return out

convertGIFtoBlackWhiteJPG()
hTemplate = createHashTemplate()

out = mapJPGtoChar()

# use substitution solver / frequency analysis
fromChr = 'hoynatgxrquilbzpcvmdkwsejf'
toChr = 'abcdefghijklmnopqrstuvwxyz'
flag = ''
for c in out:
	flag += toChr[fromChr.index(c)]
#flag = flag.replace("flagis", "\nflag is ")
print flag