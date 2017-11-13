from HIDKeyboardMappings import *
import re

'''
https://docs.mbed.com/docs/ble-hid/en/latest/api/md_doc_HID.html
find packet with info "GET DESCRIPTOR Response DEVICE"

filter packet "URB_INTERRUPT in" in wireshark
usb.device_address==3 && usb.capdata
'''

f = open('task.pcap', 'rb').read()
flag = ['']

# filter packet "URB_INTERRUPT in" len 35
URB = re.findall(r'\x1b\x00.{8}\x00{4}.{9}\x08\x00\x00\x00(.{8})', f)
lineIdx = 0
for u in URB:
	if ord(u[2]) == 0x00:
		continue
	key = u[2].encode('hex').upper()
	if key == '28' or key == '58':
		flag.append('')
		lineIdx += 1
		continue
	modifier = ord(u[0])
	isSHIFTdown = False
	if modifier & 0b100000 or modifier & 0b10:
		isSHIFTdown = True
	if key == '51': # DownArrow
		lineIdx += 1
		continue
	if key == '52': # UpArrow
		lineIdx -= 1
		continue
	if type(hidMap[key]) == list:
		if isSHIFTdown:
			flag[lineIdx] += hidMap[key][1]
		else:
			flag[lineIdx] += hidMap[key][0]
	else:
		flag[lineIdx] += hidMap[key]
for f in flag:
	print f