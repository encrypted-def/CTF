import socket
def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  g, y, x = egcd(b%a,a)
  return (g, x - (b//a) * y, y)
def GCD(a, b):
  if a == 0: return b
  return GCD(b%a, a)
def modinv(a, m):
  g, x, y = egcd(a, m)
  if g != 1:
    raise Exception('No modular inverse')
  return x%m
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
server_addr = ('lcg.eatpwnnosleep.com', 12345)
sock.connect(server_addr)
print("CONN DONE")
B = [0]*40
C = [0]*40
D = [0]*40
E = [0]*40
ff = 8
for i in range(1,ff+1):
  B[i] = int(sendrecv(sock,'1\n'))
for i in range(2,ff+1):
  C[i] = B[i]-B[i-1]
for i in range(3,ff):
  D[i] = C[i]*C[i]-C[i-1]*C[i+1]
G = 0
for i in range(4,ff-1):
  val = D[i]*D[i]-D[i-1]*D[i+1]
  G = GCD(G,abs(val))
  print(G)
x = (C[4]*C[3]-C[5]*C[2])*modinv(D[3],G)
y = -D[4]*modinv(D[3],G)
x = x % G
y = y % G
for i in range(ff,32):
  print("now ", i)
  C[i+1] = (x*C[i]+y*C[i-1]) % G
  B[i+1] = (C[i+1]+B[i]) % G
  print("send : ", B[i+1])
  if(i <= 16): print("recv : ", sendrecv(sock, str(B[i+1])+'\n'))
  else: sock.send((str(B[i+1])+'\n').encode())

print(sock.recv(1000).decode())
interactive(sock)
