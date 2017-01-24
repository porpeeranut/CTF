import itertools

'''
view source and decode base64 string in footer
will found code of javascript that obfuscated

then use "javascript deobfuscator" plugin in firefox to deobfuscate
and bruteforce permutation string to find key
'''

def checkEntries(passwd):
	for i in range(1, 11):
		digit = int(passwd[i - 1]);
		part = int(passwd[:i]);
		if part % i != 0:
			return False
	return True

def solve():
	allPass = list(itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']))
	for passwd in allPass:
		if checkEntries(''.join(passwd)):
			print ''.join(passwd)
			break
	
solve()