#!/usr/bin/env python

verify_arr = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
user_arr = []
for arr in verify_arr:
  tmp = ((arr & 255 ) ^ 111)
  user_arr.append(tmp >> 5 | (tmp << 3 & 255))

print ''.join(chr(i) for i in user_arr)