import re
# https://www.sqlite.org/opcode.html

codes = []
with open('sql.txt') as f:
	for line in f:
		if re.findall(r'^\d', line):
			codes.append(line.strip())
eip = 0
regs = [0]*100
flag = ['']*100
while True:
	addr, opcode, p1, p2, p3, p4, p5 = codes[eip].split('|')[:-1]
	print addr, opcode, p1, p2, p3, p4, p5
	if opcode == 'Goto':
		eip = int(p2)
		continue
	elif opcode == 'String8':
		regs[int(p2)] = p4
	elif opcode == 'If':
		if regs[int(p1)]:
			eip = int(p2)
			continue
	elif opcode == 'Function':
		regs[int(p3)] = int(regs[int(p2) + 1])
	elif opcode == 'Ne':
		flag[regs[int(p3)]] = regs[int(p1)]
		# if regs[int(p1)] != regs[int(p3)]:
		if regs[int(p1)] == regs[int(p3)]:
			eip = int(p2)
			continue
	elif opcode == 'Column':
		regs[int(p3)] = regs[int(p1)]
	elif opcode == 'Integer':
		regs[int(p2)] = int(p1)
	elif opcode == 'Halt':
		print ''.join(flag)
		exit()
	eip += 1