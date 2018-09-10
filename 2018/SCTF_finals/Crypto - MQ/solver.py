import socket
import random
def sendrecv(sock, msg):
  if type(msg) == str: msg = msg.encode()
  sock.send(msg)
  recvdata = sock.recv(1000).decode()
  return recvdata.strip()
def interactive(sock):
  while True:
    S = input('> ')
    print(sendrecv(sock,S))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('mq.eatpwnnosleep.com', 12345)
sock.connect(server_addr)
p = 131
quad = [[0]*32 for i  in range(32)]
A = [[0]*32 for i  in range(32)]
uni = [0]*32
c = 0
pasre = sock.recv(100000).decode().split('+')
for elem in pasre:
  es = elem.strip().split('x')
  if len(es) == 1:
    c = int(es[0])
  elif len(es) == 2:
    uni[int(es[1])-1]=int(es[0])
  else:
    a = int(es[1])-1
    b = int(es[2])-1
    quad[a][b] = int(es[0])
    quad[b][a] = int(es[0])


for i in range(32):
  for j in range(32):
    A[i][j]=quad[i][j]
    if i==j: A[i][j] = 2*A[i][j]



print(A)
#### parse factor
original = int(sendrecv(sock,'\x00'*32)[2:],16)
B = [0]*32
for i in range(32):
  query = '\x00'*i+'\x01'+'\x00'*(31-i)
  newval = int(sendrecv(sock,query)[2:],16)
  B[i] = (newval - original - uni[i] - quad[i][i])%p
print()
print()
print(B)
