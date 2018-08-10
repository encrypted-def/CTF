import socket
from time import sleep
import sys
EPS = 10**(-7)

def split2(numstr): # length 4
  op = ['+','-','*','/']
  N = len(numstr)
  L = [] # value,query
  ret = []
  if N == 1:
    ret.append((float(numstr[0]), numstr[0]))
    return ret
  
  for p_st in range(N-1):
    for p_en in range(p_st+1,N):
      for op_brute in range(4**(N-1)):
        querylist = []
        tmp = op_brute
        for i in range(N-1):
          if p_st == i:
            querylist.append('(')
          if p_en == i:
            querylist.append(numstr[i]+') '+op[tmp&3]+' ')
          else:
            querylist.append(numstr[i]+' '+op[tmp&3] + ' ')

          tmp //= 4
        if p_en == N-1:
          querylist.append(numstr[N-1]+')')
        else:
          querylist.append(numstr[N-1])         
        query = ''.join(querylist)
        try:
          L.append((eval(query),query))
        except:
          pass
  L.sort()
  ret.append(L[0])
  for i in range(1,len(L)):
    if ret[-1][0] != L[i][0]:
      ret.append(L[i])
  return ret

def solver(recvdata):
  op = ['+','-','*','/']
  numstr = recvdata.split()
  N = len(numstr)-1
  num = [0.0]*(N+1)
  for i in range(N+1):
    num[i] = float(numstr[i])
 # cat = catalan(N) 
  for op_brute in range(4**(N-1)):
    querylist = []
    tmp = op_brute
    for i in range(N-1):
      querylist.append(numstr[i]+' '+op[tmp&3] + ' ')
      tmp //= 4
    querylist.append(numstr[N-1])
    query = ''.join(querylist)+'\n'
    #print(query, eval(query))
    try:
      if abs(eval(query)-num[N]) < EPS:
        return query
    except: pass

  for sep in range(1,8):
    L1 = split2(numstr[:sep])
    L2 = split2(numstr[sep:-1])
    print(len(L1),len(L2))
    for elem1 in L1:
      for elem2 in L2:
        #print(elem1)
        if abs(elem1[0] + elem2[0] - num[N]) < EPS:
          return '('+elem1[1] + ') + (' + elem2[1] + ')\n'
        if abs(elem1[0] * elem2[0] - num[N]) < EPS:
          return '('+elem1[1] + ') * (' + elem2[1] + ')\n'
        if abs(elem1[0] - elem2[0] - num[N]) < EPS:
          return '('+elem1[1] + ') - (' + elem2[1] + ')\n'
        try:
          if abs(elem1[0] / elem2[0] - num[N]) < EPS:
            return '('+elem1[1] + ') / (' + elem2[1] + ')\n'
        except: pass
  print("not found in l1 l2")
  '''
  for p_st in range(N-1):
    for p_en in range(p_st+1,N):
      for op_brute in range(4**(N-1)):
        querylist = []
        tmp = op_brute
        for i in range(N-1):
          if p_st == i:
            querylist.append('(')
          if p_en == i:
            querylist.append(numstr[i]+') '+op[tmp&3]+' ')
          else:
            querylist.append(numstr[i]+' '+op[tmp&3] + ' ')

          tmp //= 4
        if p_en == N-1:
          querylist.append(numstr[N-1]+')')
        else:
          querylist.append(numstr[N-1])         
        query = ''.join(querylist)+'\n'
        try:
          if abs(eval(query)-num[N]) < EPS:
            return query
        except: pass  
  return 'zxcvzxcv\n'
'''
#print(solver("1 1 1 1 1 1 1 1 0.142857142857"))
#exit(0)


while True:
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('ppc-01.v7frkwrfyhsjtbpfcppnu.ctfz.one', 2445)
    sock.connect(server_addr)
    #step 1
    print("#########step 1#########")
    recvdata = sock.recv(1000).decode()
    print(recvdata)
    numstr = recvdata.split()
    num = [0.0]*4
    num[0] = float(numstr[0])
    num[1] = float(numstr[1])
    num[2] = float(numstr[2])
    num[3] = float(numstr[3])
  
    query = "sdf\n"
    if abs(num[0]+num[1]+num[2] - num[3]) < EPS:
      query = "{} + {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]+num[1]-num[2] - num[3]) < EPS:
      query = "{} + {} - {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]+num[2] - num[3]) < EPS:
      query = "{} - {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]-num[2] - num[3]) < EPS:
      query = "{} - {} - {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]*num[2] - num[3]) < EPS:
      query = "{} * {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]/num[2] - num[3]) < EPS:
      query = "{} * {} / {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]/num[1]*num[2] - num[3]) < EPS:
      query = "{} / {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]+num[1]/num[2] - num[3]) < EPS:
      query = "{} + {} / {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]+num[1]*num[2] - num[3]) < EPS:
      query = "{} + {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]/num[2] - num[3]) < EPS:
      query = "{} - {} / {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]*num[2] - num[3]) < EPS:
      query = "{} - {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]/num[1]+num[2] - num[3]) < EPS:
      query = "{} / {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]/num[1]+num[2] - num[3]) < EPS:
      query = "{} / {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]+num[2] - num[3]) < EPS:
      query = "{} * {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]-num[2] - num[3]) < EPS:
      query = "{} * {} - {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]+num[1])*num[2]-num[3]) < EPS:
      query = "({} + {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]-num[1])*num[2]-num[3]) < EPS:
      query = "({} - {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]+num[1])/num[2]-num[3]) < EPS:
      query = "({} + {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]-num[1])/num[2]-num[3]) < EPS:
      query = "({} + {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]*(num[1]+num[2]))-num[3]) < EPS:
      query = " {} * ({} + {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]*(num[1]-num[2]))-num[3]) < EPS:
      query = " {} * ({} - {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]/(num[1]*num[2]))-num[3]) < EPS:
      query = " {} / ({} * {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]/(num[1]+num[2]))-num[3]) < EPS:
      query = " {} / ({} + {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]/(num[1]-num[2]))-num[3]) < EPS:
      query = " {} / ({} - {})\n".format(numstr[0],numstr[1],numstr[2])
  
    
    print(query)
    senddata = sock.send(query.encode())
    print("Send done")
    sleep(0.3)
    recvdata = sock.recv(1000).decode()
    print(recvdata)

    #step 2
    print("#########step 2#########")
    sleep(0.3)
    recvdata = sock.recv(1000).decode()
    print(recvdata)
    numstr = recvdata.split()
    num = [0.0]*3
    num[0] = float(numstr[0])
    num[1] = float(numstr[1])
    num[2] = float(numstr[2])
    query = "sdf\n"
    if abs(num[0]+num[1]-num[2]) < EPS:
      query = "{} + {}\n".format(numstr[0],numstr[1])
    if abs(num[0]-num[1]-num[2]) < EPS:
      query = "{} - {}\n".format(numstr[0],numstr[1])
    if abs(num[0]*num[1]-num[2]) < EPS:
      query = "{} * {}\n".format(numstr[0],numstr[1])
    if abs(num[0]/num[1]-num[2]) < EPS:
      query = "{} / {}\n".format(numstr[0],numstr[1])

    #print(query)
    senddata = sock.send(query.encode())
    print("Send done")
    sleep(0.3)
    recvdata = sock.recv(1000).decode()
    print(recvdata)

    #step 3
    print("#########step 3#########")
    sleep(0.3)
    recvdata = sock.recv(1000).decode()
    print(recvdata)
    numstr = recvdata.split()
    num = [0.0]*4
    num[0] = float(numstr[0])
    num[1] = float(numstr[1])
    num[2] = float(numstr[2])
    num[3] = float(numstr[3])
  
    query = "sdf\n"
    if abs(num[0]+num[1]+num[2] - num[3]) < EPS:
      query = "{} + {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]+num[1]-num[2] - num[3]) < EPS:
      query = "{} + {} - {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]+num[2] - num[3]) < EPS:
      query = "{} - {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]-num[2] - num[3]) < EPS:
      query = "{} - {} - {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]*num[2] - num[3]) < EPS:
      query = "{} * {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]/num[2] - num[3]) < EPS:
      query = "{} * {} / {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]/num[1]*num[2] - num[3]) < EPS:
      query = "{} / {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]+num[1]/num[2] - num[3]) < EPS:
      query = "{} + {} / {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]+num[1]*num[2] - num[3]) < EPS:
      query = "{} + {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]/num[2] - num[3]) < EPS:
      query = "{} - {} / {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]-num[1]*num[2] - num[3]) < EPS:
      query = "{} - {} * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]/num[1]+num[2] - num[3]) < EPS:
      query = "{} / {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]/num[1]+num[2] - num[3]) < EPS:
      query = "{} / {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]+num[2] - num[3]) < EPS:
      query = "{} * {} + {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs(num[0]*num[1]-num[2] - num[3]) < EPS:
      query = "{} * {} - {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]+num[1])*num[2]-num[3]) < EPS:
      query = "({} + {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]-num[1])*num[2]-num[3]) < EPS:
      query = "({} - {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]+num[1])/num[2]-num[3]) < EPS:
      query = "({} + {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]-num[1])/num[2]-num[3]) < EPS:
      query = "({} + {}) * {}\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]*(num[1]+num[2]))-num[3]) < EPS:
      query = " {} * ({} + {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]*(num[1]-num[2]))-num[3]) < EPS:
      query = " {} * ({} - {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]/(num[1]*num[2]))-num[3]) < EPS:
      query = " {} / ({} * {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]/(num[1]+num[2]))-num[3]) < EPS:
      query = " {} / ({} + {})\n".format(numstr[0],numstr[1],numstr[2])
    elif abs((num[0]/(num[1]-num[2]))-num[3]) < EPS:
      query = " {} / ({} - {})\n".format(numstr[0],numstr[1],numstr[2])
  
    
    print(query)
    sleep(0.3)
    senddata = sock.send(query.encode())
    print("Send done")
    sleep(0.3)
    recvdata = sock.recv(1000).decode()
    print(recvdata)
    step = 4
    while True:
      print('go', step)
      print("#########step {}#########".format(step))
      sleep(0.3)
      recvdata = sock.recv(1000).decode()
      print(recvdata.strip())
      query = solver(recvdata)
      print(query.strip())
      sleep(0.3)
      sock.send(query.encode())
      sleep(0.3)
      recvdata = sock.recv(1000).decode()
      print(recvdata)
      step += 1
  except:
    break
