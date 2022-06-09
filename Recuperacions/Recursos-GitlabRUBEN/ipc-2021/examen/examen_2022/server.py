# /usr/bin/python
#-*- coding: utf-8-*-
# prog [-d|--debug] [-p|--port]
#------------------------------
# Jamison Quelal León ASIX M06 Curs 2021-2022
# Exàmen Pràctic
#------------------------------
import sys,socket,os,signal,argparse
from subprocess import Popen, PIPE
#-------------------------------
parser = argparse.ArgumentParser(description="""Server01 Exàmen""")
parser.add_argument("-d","--debug",type=str)
parser.add_argument("-p","--port",type=int,default=44444)
args=parser.parse_args()
#--------------------------------
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
#--------------------------------------------
pid = os.fork()
if pid !=0:
    print("Server Engegat:", pid)
    sys.exit(0)

signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
MYEOT = bytes(chr(4), 'utf-8')

while True:
    conn, addr = s.accept()
    llistaPeers.append(addr)
    if args.debug:
        print("Connectat per:", addr)
    while True:
        command = conn.recv(1024)
        if not command:
            conn.close()
            break
        else:
            if command == 'processos':
                command = "ps ax"
            elif command == 'ports':
                command = "netstat -puta"
            elif command == 'whoareyou':
                command = "uname -a"
            else:
                command = "uname -a"
           
            pipeData = Popen(command,shell=True,stdout=PIPE,stderr=PIPE)
            for line in pipeData.stderr:
                conn.send(line)
            for line in pipeData.stdout:
                conn.send(line)
            conn.send(MYEOT)
