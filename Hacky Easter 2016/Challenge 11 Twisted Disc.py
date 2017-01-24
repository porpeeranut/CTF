def findSingleLetter(word):
	for c in word:
		if word.count(c) == 1:
			return c

wheel1 = 'beanstzkcdauueiyzybmvxgpjlcxnjqwoowqfdhilfrmgpsrtvk'
wheel2 = 'buwxhappysdfbkcooltqwreezymklcfdtvqhvsmrzxu '
wheel3 = 'cpidephjklonkamuffyiolyumsschajdett'
wheel4 = 'idlyrvchefpdopoefussycrlhuv'
wheel5 = 'xjqsimpeljqninxmpel'
wheel6 = 'kakosfflaohls'
wheel7 = 'peoplle'

ans = ''
ans += findSingleLetter(wheel1)
ans += findSingleLetter(wheel2)
ans += findSingleLetter(wheel3)
ans += findSingleLetter(wheel4)
ans += findSingleLetter(wheel5)
ans += findSingleLetter(wheel6)
ans += findSingleLetter(wheel7)
print ans