from Crypto.Util.number import *
import binascii,socket,sys

def gcd(a, b):
  while(b): 
    a,b = b, a % b 
  return a 
def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  g, y, x = egcd(b%a,a)
  return (g, x - (b//a) * y, y)

def inv(a, m):
  g, x, y = egcd(a, m)
  if g != 1:
    raise Exception('No modular inverse')
  return x%m

# x**2 = a (mod m), m is prime
def quad_congruence_equation(a, m):
  assert((m+1)%4 == 0)
  return pow(a, (m+1)//4, m)
# m must satisfies pairwise relatively prime
def crt(a, m):
  n = len(m)
  ret = a[0]
  mod = m[0]
  for i in range(1,n):
    m1 = mod
    mod *= m[i]
    m2inv = inv(m[i],m1)
    m1inv = inv(m1,m[i])
    ret = (ret*m[i]*m2inv+a[i]*m1*m1inv)%mod
  return ret

############ my socket ###############
def interactive(socket):
  print("[+] interactive mode")
  while True:
    rr = socket.recv(2**16).decode()
    if not rr:
      print("[!] socket closed")
      return None
    print(rr)
    socket.send((input('> ')+'\n').encode())

def remote(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print("[+] Connecting to {}:{}".format(ip,port))
  sock.connect((ip,port))
  print("[+] Done!")
  return sock

def sendline(socket, msg):
  if type(msg) == str: msg = msg.encode()
  if msg[-1] != b'\n': msg += b'\n'
  socket.send(msg)

###################################
