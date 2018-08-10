import base64
import sys
import socket
from time import sleep
#print(base64.b64decode(b"TvYqAi4mgu4DAaTC6Ycyru3wTvdGIAEXM/TzrHxv6AC8zI35PZA7nqfNN2x7wLydnN2X6knKfkPiHwWib8G04DXikKrmLZc9tOjTOuWYW14hqiCJIcrQPmNBQzANUneuk1rkjBnrsMu6+VajnMym9c5XjFdg8GlSpV/9OgLjsGiz2KZV96R4GJfZ2obHtSwuA9WicqWHl0ZJdwjh0g6i5Mqy11TURfXTtHRAMxFXM8UkCU+cPTRvMa4eZHpkBbXw6T4aoFQzEK4EHBECYVPZKa/u+BcehSD/kiYdRia8cyA+iktK2mNqzzCEUJxKd0VsS11W7mYI4Ce38/yIJdjGwxGCN7zZ7oq2V/FGss9LmZYA+1mN4k4juPZkVTT3NvaThYEgNBQtMMhxUdyHX6eIVPWK2ZnW3JLn+It6S0YTqc/XQ7wiiIPROifz+Qt8ptSsiMdKbdxaEiZ6HSdUaWsqN5q9VmI+/Nl0r5R/FYVidWZunvV270kYfQAskTOn7crlscZUGwhL9h67kgXzEat7z5N369GOcl1/noCyxleZmDHAl5fJp4oYZ/qgE2MhiihCeIg4cZIA6F68OvoEpna1AfpijSewrlC4EjVKj15sVKQmdMvAxudWmQtKHqUZbazz4/JqIk2LkDpQcyKbKQCMuJKCAF9w/dCb8pU1jnNEgtd+D3gUUMj1Qdn26kwpmWQB+ZpCrtkSBkIDv72lHqayIzEFHIGC6AUayssrle/W1vaT+WUZMoLBGPbb/Ilki4vtCRRXQXNY4av0F8PTRDnRxphbY6bYX4DDjlM/xmIX7jOJgqQclpugfHdSzB0MmuIuSgJd7FdFQA2hPCYguRDu2d42Q/tsJaNjbZrGRiadfuor5z1HDcg0qg4TdEGz4KTB1wSiIwQsfTNFQ4F46IW6Plmjeh7A0d2yCoNyDK/SUXEKuCc7V0bwRNHKSmUemvCpzww8zYcOlLPSNJVVmUSlNoc4k/e8hegoGmPPduVBjtKM+k3Jn1rRSULxdr3OZ8rv6ylWwYVcbIg++o0gtOfVZsOIm3XIj8g7guamDf9h1mBYQHFtsn6RJf8TZCUXwBGBpzhSDBDF6iM53nXs03ZbIwGRe9af35ZOWV32L+QtCQnlV7+8Z7DlB7t329NTc2AoXR7ODZ9oXdbka8fhMD+QAFNBev1qLZATEfvk85mqHDO1JxFubNOOSrp/7m2zy+pLyCGgtzFy5RGGkLXWrtvgiul7SGHZ4NRllbMzjkhwcod1rTNBFzJryMKaELf7Ga1VUeI0haREL4vPUPpdz7zU7GhkIwpnBWw0bLBn+ZnnRqhBzgbdP+i2R4VRnl6iBMiRHZo7n5sDU+EotyD8D7+ZWLxHSdDv76PVDatkQJKQbzMZ3b/Uh/CItHhBi4Ahug9+6KVVUKT0mRXgMQ3QLJaH4UkoJhtjB2ESViyJMWdEFXUsr3RRTB084lc3bFGcbjGli0/U9GsJBlX27OQe4oE136ib77Xaa+TjqivVgiYPuTVMpH4Z1EY2+vNLhpCZzBbw").hex())
#exit(0)

test1=b'\x00\x00\x00\x00'*3+b'\x13\x50\x50\x02'
#print(base64.b64encode(test1))
#print(base64.b64decode(b'AAAAAAAAAAAAAAAAE1BQAv/////////////////////pDgAA').hex())
#00 00 00 00 : 16 0e 00 00
#00 50 00 00 : 26 0e 00 00
#13 50 50 02 : e9 0e 00 00 
#exit(0)
def recvmsg():
  end = '\n'
  recv = sock.recv(100000).decode('utf-8')
  while recv.find(end) == -1:
    recv += sock.recv(100000).decode('utf-8')
  return recv[:recv.find(end)]

def sendmsg(msg):
  if type(msg) == str:
    sock.send(msg.encode())
  else:
    sock.send(msg)

def interactive():
  while True:
    S = input('> ')
    sendmsg(S)
    print(recvmsg())


HASH_LENGTH=32
CHECKSUM_LENGTH=4
MESSAGE_LENGTH=32
CHANGED_MESSAGE_LENGTH=MESSAGE_LENGTH+CHECKSUM_LENGTH
BITS_PER_BYTE=8
show_flag_command="show flag"+(MESSAGE_LENGTH-9)*"\xff"
admin_command=b"su admin"+(MESSAGE_LENGTH-8)*b"\x00"
admin_command_b64 = base64.b64encode(admin_command)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('crypto-02.v7frkwrfyhsjtbpfcppnu.ctfz.one',1337)
sock.connect(server_addr)
recvdata = recvmsg()
print(recvdata) # intro
forge_admin_command = b"su admin"+(MESSAGE_LENGTH-9)*b"\x00"+b"\x01"
forge_admin_command_b64 = base64.b64encode(forge_admin_command).decode("utf-8")
sendmsg("sign:"+forge_admin_command_b64)
data_sig = recvmsg()
data = base64.b64decode(data_sig.split(',')[0])

##### recover checksum #####
checksum = data[32:]
print("checksum ", checksum.hex())
for ch in range(255,-1,-1):
  print("#### step {} #######".format(ch))
  checksum = bytes([ch])+checksum[1:]
  query = b"execute_command:"+base64.b64encode(admin_command+checksum)+b",aaaa"
  sendmsg(query)
  sleep(0.3)
  recvdata = recvmsg()
  if recvdata.find("checksum") < 0:
    print(recvdata)
    print("FIND!!", checksum.hex())
    break
  if ch == 0:
    print("Failed to recover checksum..")
    exit(0)

##### recover admin data #######

forge_admin_command1 = b"su admin"+(MESSAGE_LENGTH-9)*b"\x00"+b"\x01"
forge_admin_command2 = b"su admin"+(MESSAGE_LENGTH-10)*b"\x00"+b"\x01\x00"
forge_admin_command1_b64 = base64.b64encode(forge_admin_command1).decode("utf-8")
forge_admin_command2_b64 = base64.b64encode(forge_admin_command2).decode("utf-8")

sendmsg("sign:"+forge_admin_command1_b64)
sleep(0.3)
data_sig1 = recvmsg()
sig1 = base64.b64decode(data_sig1.split(',')[1]) # first 31*32byte of admin command
#print(data_sig1)
print(sig1.hex())
print("\n\n")

sendmsg("sign:"+forge_admin_command2_b64)
sleep(0.3)
data_sig2 = recvmsg()
#print(data_sig2)
sig2 = base64.b64decode(data_sig2.split(',')[1]) # last 32byte of admin command
print(sig2.hex())
print("\n\n")

# must recover sign of checksum
brute = 0 
while True:  # probability is 1/256
  brute += 1
  forge_admin_command3 = b"su admin"+(MESSAGE_LENGTH-12)*b"\x00"+b"\x01\x01"+bytes([(brute & 0xff00) >> 8,brute & 0xff])
  sendmsg(b"sign:"+base64.b64encode(forge_admin_command3))
  sleep(0.3)
  data_sig3 = recvmsg()
  #print(data_sig3)
  data = base64.b64decode(data_sig3.split(',')[0])
  sig3 = base64.b64decode(data_sig3.split(',')[1])
  print(brute, data[32:].hex(),checksum.hex())
  if data[32:] == checksum:
    print("recover success!!")
    print(sig3.hex())
    print("\n\n")
    break


admin_sig = sig1[:-160]+sig2[-160:-128]+sig3[-128:]
print(admin_sig.hex())
print("\n\n")

print("-------------admin_sig-------------",admin_sig)
admin_data = admin_command+checksum
print("------- admin data ----- ", admin_data.hex())
query = b"execute_command:"+base64.b64encode(admin_data)+b","+base64.b64encode(admin_sig)
print("-------------query----------------",query)
sendmsg(query)
sleep(0.3)

recvdata = recvmsg()
print(recvdata)


############ show flag ###############
print("\n#### show flag ####\n")
forge_flag_command=b"show flag"+(MESSAGE_LENGTH-10)*b"\xff"
forge_flag_b64 = base64.b64encode(forge_flag_command).decode("utf-8")

sendmsg("sign:"+forge_flag_b64) # send forge flag command
sleep(0.3)

flag_data_sig = recvmsg() # after previlage escalation, just send this

sendmsg("execute_command:"+flag_data_sig)
sleep(0.3)

recvdata = recvmsg()
print(recvdata)

interactive()
# 
