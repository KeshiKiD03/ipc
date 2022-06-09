# /usr/bin/python3
#-*- coding: utf-8-*-
# ps-server.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket,os,signal,argparse, time
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""PS server""")
parser.add_argument("-p","--port",type=int, default=50001)
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
  fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%s"))
  fileLog=open(fileName,"w")
  while True:
    data = conn.recv(1024)
    if not data: break
    fileLog.write(str(data))
  conn.close()
  fileLog.close()



