# --- RAID 5 backward parity (size per block = 512 byte) ---
#		________________
#		|  0 |  1 |  p |
#		|  2 |  p |  3 |
#		|  p |  4 |  5 |
#		 dsk0 dsk1 dsk2
# mount out.img /tmp/out

disk0 = 'disk0'
disk1 = 'disk1'
disk2 = 'disk2'
out = 'out.img'
d0 = bytearray(open(disk0, 'rb').read())
d2 = bytearray(open(disk2, 'rb').read())
d1 = bytearray(len(d0))
o = bytearray(len(d0)*2)
disk_count = 3
p_idx = 2
block_size = 512

# recovery disk1
for b in range(len(d0)):
	d1[b] = d0[b] ^ d2[b]

# rebuild data image from 3 disk
for block_i in range(len(d0)/block_size):
	dsk_idx_start = block_i*block_size
	out_idx_start = block_i*(disk_count-1)*block_size
	if p_idx == 2:
		o[out_idx_start:out_idx_start+block_size] = d0[dsk_idx_start:dsk_idx_start+block_size]
		o[out_idx_start+block_size:out_idx_start+block_size*2] = d1[dsk_idx_start:dsk_idx_start+block_size]
	elif p_idx == 1:
		o[out_idx_start:out_idx_start+block_size] = d0[dsk_idx_start:dsk_idx_start+block_size]
		o[out_idx_start+block_size:out_idx_start+block_size*2] = d2[dsk_idx_start:dsk_idx_start+block_size]
	else:
		o[out_idx_start:out_idx_start+block_size] = d1[dsk_idx_start:dsk_idx_start+block_size]
		o[out_idx_start+block_size:out_idx_start+block_size*2] = d2[dsk_idx_start:dsk_idx_start+block_size]
		
	p_idx -= 1
	if p_idx == -1:
		p_idx = 2
	
open(disk1, 'wb').write(d1)
open(out, 'wb').write(o)