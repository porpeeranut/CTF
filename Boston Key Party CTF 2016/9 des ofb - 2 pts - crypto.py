from Crypto.Cipher import DES

'''
	decrypt with weak key
	"Because of the symmetry of the XOR operation, 
	encryption and decryption are exactly the same"

	ref:
	https://en.wikipedia.org/wiki/Weak_key#Weak_keys_in_DES
	https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_Feedback_.28OFB.29
'''

key_hex = "E1E1E1E1F0F0F0F0"
KEY = key_hex.decode("hex")
IV = '13245678'
a = DES.new(KEY, DES.MODE_OFB, IV)

f = open('ciphertext', 'r')
ciphertext = f.read()
f.close()

plaintext = a.encrypt(ciphertext)
f = open('plaintext', 'w')
f.write(plaintext)
f.close()