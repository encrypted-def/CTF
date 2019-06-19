from hashlib import sha256
import string,random
import socket
from math import pi
import sys,time

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

def recv(socket):
  r = socket.recv(2**16).decode()
  return r

def sendline(socket, msg):
  if type(msg) == str: msg = msg.encode()
  if msg[-1] != b'\n': msg += b'\n'
  socket.send(msg)

def send(socket, msg):
  if type(msg) == str: msg = msg.encode()
  socket.send(msg)


schedule = '''0,1,1,2,1,1
1,1,0,0,1,1
1,1,0,2,1,1
1,1,1,1,1,1
1,1,1,2,0,0
0,0,0,0,0,0
0,0,0,2,0,0
0,0,1,1,0,0
0,0,1,2,2,0
2,0,0,0,2,0
2,0,0,2,2,0
2,0,1,1,2,0
2,0,1,2,2,2
2,2,0,0,2,2
2,2,0,2,2,2
2,2,1,1,2,2
2,2,1,2,0,1
0,1,0,0,0,1
0,1,0,2,0,1
0,1,1,1,0,1
0,1,2,0,1,1
1,1,2,2,1,1
1,1,2,0,0,0
0,0,2,2,0,0
0,0,2,0,2,0
2,0,2,0,2,2
2,2,2,0,0,0
0,0,1,1,1,1
1,1,0,2,0,2
0,2,1,1,0,0
0,0,0,2,1,0
1,0,1,1,1,0
1,0,0,0,0,0
0,0,2,0,1,0
1,0,0,2,1,2
1,2,1,1,1,2
1,2,0,2,2,1
2,1,0,2,1,1
1,1,0,1,1,1
1,1,1,0,1,1
1,1,2,1,1,1
1,1,1,2,1,1
1,1,2,0,1,1
1,1,0,0,2,2
2,2,1,1,0,0
0,0,0,0,1,1
1,1,2,2,2,0
2,0,1,1,0,2
0,2,2,0,0,1
0,1,2,2,0,1
0,1,0,2,0,0
0,0,1,0,0,0
0,0,0,1,1,1
1,1,1,1,2,2
2,2,0,2,2,0
2,0,2,2,1,1
1,1,0,2,0,1
0,1,1,0,1,1
1,1,0,1,0,0
0,0,0,2,2,0
2,0,0,0,0,0
0,0,2,2,2,0
2,0,0,2,2,2
2,2,2,2,0,0
0,0,1,1,1,0
1,0,2,0,1,2
1,2,0,2,0,2
0,2,0,2,1,0
1,0,0,2,2,1
2,1,0,0,1,0
1,0,0,2,2,0
0,1,1,2,0,0
0,0,0,1,0,0
0,0,1,2,0,2
0,2,0,0,1,2
1,2,1,1,1,1
1,1,0,0,2,1
2,1,1,1,0,0
0,0,1,0,2,0
2,0,0,2,0,0
0,0,0,0,1,2
1,2,0,0,2,0
2,0,0,1,2,0
2,0,2,0,0,2
0,2,0,2,1,2
1,2,0,2,1,2
1,2,2,0,2,1
2,1,0,2,0,0
0,0,2,0,0,0
0,0,2,1,0,0
0,0,2,1,2,0
2,0,0,2,2,1
2,1,0,1,0,2
0,2,0,2,2,2
2,2,0,0,0,0
0,0,2,1,1,0
1,0,1,1,0,2
2,2,1,1,1,1
1,1,0,1,2,2
2,2,1,0,1,1
1,1,2,2,2,2
2,2,0,1,1,0
1,0,2,0,1,1
1,1,2,1,0,2
1,1,2,1,2,0
2,0,0,1,0,2
2,0,0,0,1,0
1,0,1,0,0,2
1,1,2,2,2,1
2,1,0,0,2,2
2,2,1,0,0,0
0,0,2,2,1,2
1,2,1,1,0,2
2,2,1,0,1,0
1,0,0,0,1,0
1,0,1,2,0,2
0,1,2,1,0,0
0,0,1,2,2,2
2,2,2,2,0,2
2,2,1,0,0,2
1,1,2,0,2,2
2,2,2,2,1,1
1,2,1,0,0,0
0,0,1,2,1,2
1,2,2,2,0,2
2,2,1,0,2,0
2,0,1,0,0,0
0,0,1,1,2,0
2,2,0,2,0,1
2,2,2,0,2,0
2,0,1,2,2,0
2,0,2,0,1,1
2,1,1,1,2,2
1,2,2,0,1,0
1,0,2,2,0,2
2,0,2,0,0,0
2,1,0,0,0,0
2,0,1,2,1,0
1,0,2,0,0,1
0,1,1,1,0,0
1,2,2,1,1,1
2,0,1,2,2,1
2,1,0,2,0,2
1,2,0,0,0,2
0,1,2,0,1,0
1,0,1,2,0,0
2,1,0,2,0,1
2,1,0,1,2,2
2,2,2,0,2,2
2,2,2,1,2,2
2,2,2,0,1,0
0,1,0,0,1,1
1,2,1,2,2,0
0,1,2,0,1,2
1,0,2,1,0,0
1,2,0,0,2,2
0,1,1,0,0,1
0,1,1,1,0,2
0,1,1,0,0,0
1,0,2,0,2,1
2,2,0,0,1,2
2,1,1,1,1,0
2,1,1,2,1,2
1,2,1,1,1,0
0,1,1,0,2,1
2,1,2,0,0,0
2,2,0,0,0,2'''.split()
###################################
PLAYER = 1
OPPOSITE = -1
class game():
  def __init__(self,r):
    self.board = [[0]*27 for i in range(27)]
    self.state2 = [[0]*9 for i in range(9)]
    self.state3 = [[0]*27 for i in range(27)]
    self.restrict = None
    self.r = r
  
  def do_my_move(self,query):
    sendline(self.r,query)

  def buf_clear_mymove(self):
    print("[+] buf_clear_mymove begin")
    for _ in range(30):
      print("****** line number :",_,"*******")
      a = recv(self.r)
      print(a)
      if 'X:' in a:
        return
    print("[-] Something wrong in buf_clear_mymove :(")

  def get_oppomove(self):
    print("[+] get_oppomove begin")
    for _ in range(30):
      print("****** line number :",_,"*******")
      a = recv(self.r)
      print(a)
      if 'AI' in a: break
    if not 'AI' in a:
      print("[-] Something wrong in get_oppomove :(")
    else:
      oppo_move = [int(a[13]),int(a[16]),int(a[21]),int(a[24]),int(a[29]),int(a[32])]
      print("[+] Opposite move :",oppo_move)
      return oppo_move
    

  


def convert(tt):
  s = ''
  for x in tt:
    s += str(x)+','
  return s[:-1]

r1 = remote('192.168.201.23', 10016)
### 1 or 2
print(recv(r1))
sendline(r1,'1')

G1 = game(r1)
for ggg in range(5): # Playing 5 times
  for cnt in range(len(schedule)):
    G1.buf_clear_mymove()
    print(schedule[cnt],"------>", cnt)
    G1.do_my_move(schedule[cnt])


print(recv(r1))
print(recv(r1))
print(recv(r1))
print(recv(r1))
