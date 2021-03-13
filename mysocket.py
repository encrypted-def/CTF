############ my socket ###############

class remote:
  def __init__(self, addr, port, debug = False):
    self.addr = addr
    self.port = port
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[+] Connecting to {}:{}".format(self.addr,self.port))
    self.socket.connect((addr,port))
    print("[+] Done!")
    self.debug = debug

  def interactive(self):
    print("[+] interactive mode")
    while True:
      rr = self.socket.recv(2**16).decode()
      if not rr:
        print("[!] socket closed")
        return None
      print(rr)
      self.socket.send((input('> ')+'\n').encode())

  def sendline(self, msg):    
    if type(msg) == str: msg = msg.encode()
    if msg[-1] != b'\n': msg += b'\n'
    self.socket.send(msg)

  def recv(self):
    recved = self.socket.recv(2**16).decode()
    if self.debug: print(recved)
    return recved

  def recvuntil(self, delim):
    buf = ''
    while delim not in buf:
      buf += self.socket.recv(1).decode()
    if self.debug: print(buf)
    return buf
  
  def recvline(self):
    return self.recvuntil('\n')

########################################
