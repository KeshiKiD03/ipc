# /usr/bin/python3
#-*- coding: utf-8-*-
# ps-server.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket,os,signal,argparse, time
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""server""")
parser.add_argument("-p","--port",type=int, default=44444)
parser.add_argument("-d","--debug",action='store_true',default=False)
args=parser.parse_args()
llistaPeers=[]
HOST = ''
PORT = args.port

def mysigusr1(signum,frame):
  print("Signal handler called with signal:", signum)
  print(llistaPeers)
  sys.exit(0)
  
def mysigusr2(signum,frame):
  print("Signal handler called with signal:", signum)
  print(len(llistaPeers))
  sys.exit(0)

def mysigterm(signum,frame):
  print("Signal handler called with signal:", signum)
  print(llistaPeers, len(llistaPeers))
  sys.exit(0)
  
pid=os.fork()
if pid !=0:
  print("Engegat el server PS data:", pid)
  sys.exit(0)
  
signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

while True:

  conn, addr = s.accept()
  print("Connected by", addr)
  llistaPeers.append(addr)
 

  while True:

    data = conn.recv(1024)
    
    if args.debug:
        
        print ("data: %s" % (data))
    
    if not data:

        if args.debug:
		    
            print ("La connexió amb %s ha tancat" % (addr[0]))

        conn.close()
        
        break

    comanda= str.rstrip(data.decode('utf-8'))

    if args.debug:
		
        print ("Comanda rebuda: %s" %(comanda))

    if comanda == 'procesos':

        data = 'ps ax'

    elif comanda == 'ports':

        data = "ss -puta"

    else:

        data = "uname -a"

    pipeData = Popen(data,shell=True,stdout=PIPE)
    
    for line in pipeData.stdout:
        
        conn.send(line)

        if args.debug:
			
            print ("Enviant: %s" %(line))
    
    conn.send(b'\x04')

