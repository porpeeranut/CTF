#!/usr/bin/python

import sys

"""
Daedalus Corporation encryption script.
"""

def xor(input_data, key):
    result = ""

    for ch in input_data:
        result += chr(ord(ch) ^ key)

    print '%s\n' %(result)
    return result

def encrypt(input_data, password):
    result_data = ""
    for key in range(0,256):
        print 'key %s' %(key)
        result_data += "\n\nkey %s\n" % key
        result_data += xor(input_data, key)

    out_file = open(sys.argv[3], 'w')
    out_file.write(result_data)
    out_file.close()
    return "1"

def decrypt(input_data, password):
    return encrypt(input_data, password)

def usage():
    print("Usage: %s [encrypt/decrypt] [in_file] [out_file] [password]" % sys.argv[0])
    exit()

def main():
    if len(sys.argv) < 5:
        usage()

    input_data = open(sys.argv[2], 'r').read()
    result_data = ""

    if sys.argv[1] == "encrypt":
        result_data = encrypt(input_data, sys.argv[4])
    elif sys.argv[1] == "decrypt":
        result_data = decrypt(input_data, sys.argv[4])
    else:
        usage()

main()