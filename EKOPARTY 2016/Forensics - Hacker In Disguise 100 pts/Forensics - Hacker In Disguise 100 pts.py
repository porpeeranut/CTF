from HIDKeyboardMappings import *
import re

# http://www.freebsddiary.org/APC/usb_hid_usages.php

# not handle {Caps Lock} yet
flag = ''
with open("TIC.txt") as f:
	isLSHIFTdown = False
	isRSHIFTdown = False
	for line in f:
		line = line.strip().split(' ')
		for k in line:
			m = re.findall('d(\w\w)', k)
			if m:
				m = m[0]
				if m == "E1":
					isLSHIFTdown = True
					continue
				if m == "E5":
					isRSHIFTdown = True
					continue
				if type(hidMap[m]) == list:
					if isLSHIFTdown or isRSHIFTdown:
						flag += hidMap[m][1]
					else:
						flag += hidMap[m][0]
				else:
					flag += hidMap[m]
			m = re.findall('u(\w\w)', k)
			if m:
				m = m[0]
				if m == "E1":
					isLSHIFTdown = False
				if m == "E5":
					isRSHIFTdown = False
print flag