import socket  
HOST = "52.69.125.71"  
PORT = 4443

c = "4a5b8d0034e5469c071b60000ca134d9e04f07e4dcd6cf096b47ba48b357814e4a89ef1cfad33e1dd28b892ba7233285"  
c1 = c[0:32]  
c2 = c[32:64]  
c3 = c[64:96]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect((HOST, PORT))

s.recv(1024)  
s.recv(1024)  
s.sendall("2\n")

s.sendall(c2 + c2 + c3 + "\n")  
plain = s.recv(1024)

c1 = c2
p1 = plain[0:32]
p2 = plain[32:64]

flag = hex(int(c1,16) ^ int(p1,16) ^ int(p2,16)).replace('0x','').replace('L','').decode('hex')
print flag