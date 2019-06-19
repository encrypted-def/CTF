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
    a,b,c,d,e,f=query
    sendline(self.r,str([a,b,c,d,e,f])[1:-1])

  def buf_clear_mymove(self):
    print("[+] buf_clear_mymove begin")
    for _ in range(30):
      print("****** line number :",_,"*******")
      a = recv(self.r)
      print(a)
      if 'X' in a:
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
    

  def choose_my_move(self):
    print("****Script of choose @@@ X***")
    for _ in range(10):
      a = recv(self.r)
      print(a)
      if 'X' in a:
        break
    print("***parse done***")
    if not self.restrict:
      self.do_my_move([1,1,1,1,1,1])

    else:
      aa,bb,cc,dd = self.restrict
      x = 9*aa+3*cc
      y = 9*bb+3*dd

      for a in [aa,(aa+1)%3,(aa+2)%3]:
        for b in [bb,(bb+1)%3,(bb+2)%3]:
          if self.state2[a][b] != 0: continue
          for c in [cc,(cc+1)%3,(cc+2)%3]:
            for d in [dd,(dd+1)%3,(dd+2)%3]:
              if self.state3[3*a+c][3*b+d] != 0: continue              
              
              for e in range(3):
                for f in range(3):
                  nx = 9*a+3*c+e
                  ny = 9*b+3*d+f

                  if self.board[nx][ny] == 0:
                    self.do_my_move([a,b,c,d,e,f])
                    return
      assert(0)



def convert(tt):
  s = ''
  for x in tt:
    s += str(x)+','
  return s[:-1]

r1 = remote('192.168.201.23', 10016)
r2 = remote('192.168.201.23', 10016)
### 1 or 2
print(recv(r1))
sendline(r1,'1')
print(recv(r2))
sendline(r2,'1')
g1_move = [0,1,0,1,1,2]
print("here")
G1 = game(r1)
print("here")
G2 = game(r2)
print("here")
f1 = open("g1.txt",'w')
f2 = open("g2.txt",'w')
f1.close()
f2.close()

TIMELIMIT  = 0.05
cnt = 0
while True:
  f1 = open("g1.txt",'a')
  f2 = open("g2.txt",'a')

  print("gogo!!!",cnt)
  cnt+=1
  G1.buf_clear_mymove()
  G1.do_my_move(g1_move)
  f1.write(convert(g1_move)+'\n')
  print(convert(g1_move))
  mv = G1.get_oppomove()
  G2.buf_clear_mymove()
  G2.do_my_move(mv)
  f2.write(convert(mv)+'\n')
  g1_move = G2.get_oppomove()
  f1.close()
  f2.close()



