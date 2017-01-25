# -*- coding: utf-8 -*-
from PIL import Image
import imagehash, cv2, sys, os, operator, base64, subprocess, zlib

'''
ffmpeg -i seccontower.mp4 -ss 00:01:16.000 -vframes 1 out.jpg
ffmpeg -i seccontower.mp4 -ss 00:01:15.790 -r 1 out/img%04d.jpg
'''

def createBinaryImage(path, add, combine):
	im = cv2.imread(path, 0)
	im = im[75+int(add*1.2):420+int(add*1.2), 500-int(add*1.3):950-int(add*1.3)]
	thres = 185-add*1.6
	im = cv2.GaussianBlur(im,(11,11),0)
	im[im<thres] = 0
	im[im>=thres] = 255
	im = cv2.addWeighted(im,0.8,combine,0.2,0)
	im[im<255] = 0
	return im

def preprocess():
	print 'preprocessing..'
	if not os.path.exists('preprocess'): os.makedirs('preprocess')
	combine = cv2.imread('preprocess/combine.jpg', 0)
	add = 0
	for i in range(3, 2983):
		im = createBinaryImage('out720/img'+ str(i).zfill(4) +'.jpg', add, combine)
		cv2.imwrite('preprocess/img'+ str(i).zfill(4) +'.jpg',im)
		if i % 200 == 0:
			add += 1

def writeImageToEachGroup(char, imgNumber):
	if not os.path.exists('check/check'+char): os.makedirs('check/check'+char)
	with open('check/check'+char+'/img'+ str(imgNumber).zfill(4) +'.jpg', 'wb') as fout:
		fout.write(open('preprocess/img'+ str(imgNumber).zfill(4) +'.jpg', 'rb').read())

def decodeSemaphore():
	B32ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
	trainHash = {}
	imgname = {}
	imgname['2'] = ['img0267', 'img1436', 'img2331']
	imgname['3'] = ['img0292', 'img1307', 'img2363']
	imgname['4'] = ['img0394', 'img1288', 'img2304']
	imgname['5'] = ['img0331', 'img1363', 'img2376']
	imgname['6'] = ['img0467', 'img1286', 'img2400']
	imgname['7'] = ['img0289', 'img1340', 'img2318']
	imgname['A'] = ['img0310', 'img1387', 'img2343']
	imgname['B'] = ['img0312', 'img1422', 'img2429']
	imgname['C'] = ['img0309', 'img1451', 'img2321']
	imgname['D'] = ['img0298', 'img1297', 'img2308']
	imgname['E'] = ['img0051', 'img1290', 'img2336']
	imgname['F'] = ['img0367', 'img1383', 'img2452']
	imgname['G'] = ['img0282', 'img1467', 'img2315']
	imgname['H'] = ['img0297', 'img1306', 'img2330']
	imgname['I'] = ['img0302', 'img1303', 'img2296']
	imgname['J'] = ['img0341', 'img1407', 'img2116']
	imgname['K'] = ['img0452', 'img1294', 'img2323']
	imgname['L'] = ['img0299', 'img1313', 'img2317']
	imgname['M'] = ['img0478', 'img1300', 'img2355']
	imgname['N'] = ['img0326', 'img1445', 'img2350']
	imgname['O'] = ['img0343', 'img1326', 'img2294']
	imgname['P'] = ['img0327', 'img1377', 'img2378']
	imgname['Q'] = ['img0434', 'img1360', 'img2311']
	imgname['R'] = ['img0441', 'img1471', 'img2398']
	imgname['S'] = ['img0373', 'img1384', 'img2387']
	imgname['T'] = ['img0418', 'img1299', 'img2368']
	imgname['U'] = ['img0334', 'img1381', 'img2380']
	imgname['V'] = ['img0187', 'img1364', 'img2322']
	imgname['W'] = ['img0323', 'img1332', 'img2374']
	imgname['X'] = ['img0283', 'img1321', 'img2307']
	imgname['Y'] = ['img0332', 'img1305', 'img2324']
	imgname['Z'] = ['img0372', 'img1339', 'img2391']
	trainSize = 3

	for b32 in B32ALPHA:
		tmp = {}
		tmp['dhash'] = []
		tmp['dhasV'] = []
		tmp['phash'] = []
		tmp['ahash'] = []
		for i in range(trainSize):
			tmp['phash'].append(imagehash.phash(Image.open('preprocess/'+imgname[b32][i]+'.jpg')))
			tmp['dhash'].append(imagehash.dhash(Image.open('preprocess/'+imgname[b32][i]+'.jpg')))
			tmp['dhasV'].append(imagehash.dhash_vertical(Image.open('preprocess/'+imgname[b32][i]+'.jpg')))
			tmp['ahash'].append(imagehash.average_hash(Image.open('preprocess/'+imgname[b32][i]+'.jpg')))
		trainHash[b32] = tmp
	resB32 = ''
	if not os.path.exists('check'): os.makedirs('check')
	for i in range(3, 2983):
		if i == 2096:
			resB32 += 'B'
			continue

		dhash = imagehash.dhash(Image.open('preprocess/img'+ str(i).zfill(4) +'.jpg') )#.crop((480, 60, 920, 520)))
		dhashV = imagehash.dhash_vertical(Image.open('preprocess/img'+ str(i).zfill(4) +'.jpg') )#.crop((480, 60, 920, 520)))
		phash = imagehash.phash(Image.open('preprocess/img'+ str(i).zfill(4) +'.jpg') )#.crop((480, 60, 920, 520)))
		ahash = imagehash.average_hash(Image.open('preprocess/img'+ str(i).zfill(4) +'.jpg') )#.crop((480, 60, 920, 520)))
		sumHash = {}
		for b32 in B32ALPHA:
			sumHash[b32] = 0
			for j in range(trainSize):
				sumHash[b32] += (dhashV - trainHash[b32]['dhasV'][j]) + (phash - trainHash[b32]['phash'][j]) + (dhash - trainHash[b32]['dhash'][j]) + (ahash - trainHash[b32]['ahash'][j])

		# sort by value
		sumHash = sorted(sumHash.items(), key=operator.itemgetter(1), reverse=False)
		sys.stdout.write(sumHash[0][0])
		resB32 += sumHash[0][0]

		# write image for check error and find training set
		writeImageToEachGroup(sumHash[0][0], i)

	padding = (8-len(resB32) % 8) % 8
	resB32 += '=' * padding
	dec = base64.b32decode(resB32)
	with open("flag.png", 'wb') as f:
		f.write(dec)
	print '\n', subprocess.check_output(["zbarimg","-q", 'flag.png']).decode('utf-8')

def get_crc(tag, data):
	ch1 = zlib.crc32(tag) # this isnt necessary but shows 
	ch2 = zlib.crc32(str(data), ch1) # a cool property of CRC
	return hex(ch2 & 2**32-1)[2:-1].zfill(8).lower()

def get_zlib_check_value(data_decompressed):
	BLOCKSIZE=256*1024*1024

	asum = 1
	for i in range(len(data_decompressed)/BLOCKSIZE+1):
		d = data_decompressed[i*BLOCKSIZE:i*BLOCKSIZE+BLOCKSIZE]
		if not d:
			break
		asum = zlib.adler32(d, asum)
		if asum < 0:
			asum += 2**32
	return hex(asum)[2:-1].zfill(8).lower()

preprocess()
decodeSemaphore()

f = open('flag.png', 'rb').read()
print 'CRC:', get_crc('IDAT', f[0x5e:0x736])
print 'zlib check value:', get_zlib_check_value(zlib.decompress(f[0x5e:0x736]))