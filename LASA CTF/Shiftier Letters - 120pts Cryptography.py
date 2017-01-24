import sys, socket
# import enchant
# from nltk.corpus import words
# from nltk.corpus import wordnet

host = "web.lasactf.com"
port = 4056

with open("wordsEn.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    return word.lower() in english_words

#dic = enchant.Dict("en_US")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
for i in range(101):
    code = s.recv(2024)
    maxScore = 0
    if i == 50:
        print code
    for caesarKey in range(1, 27):
        score = 0
        caesarDecrypted = ''
        for c in code:
            if not c.isalpha():     # use isalnum() if want to rot number
                caesarDecrypted += c
            else:
                offset = ord('a') if c.islower() else ord('A')
                c = ord(c) - offset
                c = (c + caesarKey) % 26
                caesarDecrypted += chr(c + offset)
        wordlist = caesarDecrypted.split(" ")
        for word in wordlist:
            #if word in words.words():
            #if wordnet.synsets(word):
            #if dic.check(word):
            if is_english_word(word):
                score = score + 1
        if score > maxScore:
            maxScore = score
            bestAns = caesarDecrypted
            print i,"rotate",caesarKey, ":score", score
    #print bestAns
    s.send(bestAns)
s.close()