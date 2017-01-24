from PIL import Image
'''
Punch Card
'''
def translate(filename):
	# IBM-029
	mapp = {'a':'&', 'b':'-', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'a1':'A', 'a2':'B', 'a3':'C', 'a4':'D', 'a5':'E', 'a6':'F', 'a7':'G', 'a8':'H', 'a9':'I', 'b1':'J', 'b2':'K', 'b3':'L', 'b4':'M', 'b5':'N', 'b6':'O', 'b7':'P', 'b8':'Q', 'b9':'R', '01':'/', '02':'S', '03':'T', '04':'U', '05':'V', '06':'W', '07':'X', '08':'Y', '09':'Z', '28':':', '38':'#', '48':'@', '58':'\'', '68':'=', '78':'"', 'a28':'\\', 'a38':'.', 'a48':'<', 'a58':'(', 'a68':'+', 'a78':'|', 'b28':'!', 'b38':'$', 'b48':'*', 'b58':')', 'b68':';', 'b78':'^', '038':',', '048':'%', '058':'_', '068':'>', '078':'?'}

	# IBM-EBCDIC
	mapp = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'a01':'a', 'a02':'b', 'a03':'c', 'a04':'d', 'a05':'e', 'a06':'f', 'a07':'g', 'a08':'h', 'a09':'i', 'ab1':'j', 'ab2':'k', 'ab3':'l', 'ab4':'m', 'ab5':'n', 'ab6':'o', 'ab7':'p', 'ab8':'q', 'ab9':'r', 'b02':'s', 'b03':'t', 'b04':'u', 'b05':'v', 'b06':'w', 'b07':'x', 'b08':'y', 'b09':'z', 'a1':'A', 'a2':'B', 'a3':'C', 'a4':'D', 'a5':'E', 'a6':'F', 'a7':'G', 'a8':'H', 'a9':'I', 'b1':'J', 'b2':'K', 'b3':'L', 'b4':'M', 'b5':'N', 'b6':'O', 'b7':'P', 'b8':'Q', 'b9':'R', '02':'S', '03':'T', '04':'U', '05':'V', '06':'W', '07':'X', '08':'Y', '09':'Z', 'b28':'!', '78':'"', '38':'#', 'b38':'$', '048':'%', 'a':'&', 'b78':'\\', '58':'\'', 'a58':'(', 'b58':')', 'b48':'*', 'a68':'+', '038':',', 'b':'-', 'a38':'.', '01':'/', '28':':', 'b68':';', '078':'?'}

	text = ''
	im = Image.open(filename)
	pix = im.load()
	width, height = im.size
	for w in range(17, 460, 7):
		indx = ''
		i = -2
		for h in range(22, height-2, 20):	
			r, g, b, a = pix[w, h]
			if r == 255:
				if i == -2:
					indx += 'a'
				elif i == -1:
					indx += 'b'
				else:
					indx += str(i)
			i += 1
		if indx == '':
			text += ' '
		else:
			text += mapp[indx]
	return text

print 'E :I :', translate('f7191b128c49ecfef0b27cd049550ae75249f86b.png')
print 'K :I :', translate('2d77fbd5eda9ed661a7834d8273815722fb97ccc.png')
print 'O :U :', translate('89596be1f6463cb83abaecac7a375546069ecf0f.png')
print '( :U :', translate('a034586b253b057c96da0b6707364853886b22b6.png')
print 'M :W :', translate('cdeea42d7f7216f93a9f1eb93b2723c70e693bea.png')
print '4 :A :', translate('a9aba85ebcb160a7b18ea22abfb9589bd3ce1914.png')
print '1 :I :', translate('4a95fea0f5e9af0af550b94fb960222e934ad09b.png')
print 'N :C :', translate('07d561df3da01f31590066f014652e995f7b76f1.png')
print 'F :T :', translate('85a749d44bcba42869f21fb58f9725a443066a4f.png')
print 'R :F :', translate('a8a103961eccf8a991edfed1aaa39a8f9a3fe622.png')
print '4 :A :', translate('93ec404ba9266f5d059a727a6460b2693fc4c440.png')
print 'M :D :', translate('d3860afefe98f2408e24218a882aaf227d9287b9.png')
print '3 :E :', translate('19756efa72339faa9c9b5fe1743c3abedbc5079d.png')
print ') :) :', translate('24c1e220c056210e6507c4c57079ffb99ffeb96c.png')