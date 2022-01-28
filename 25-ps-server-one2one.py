# /usr/bin/python
#-*- coding: utf-8-*-
# cal-server-one2one-pissara.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """CAL server""")

parser.add_argument("-a","--any",type=int, default=2022)

parser.add_argument("-p","--port",type=int, default=50001)

args=parser.parse_args()
# -------------------------------------
llistaPeers=[]  # Definim la llista buida de les connexions
HOST = ''   # Definim com a HOST (localhost)
PORT = args.port    # Definim el PORT que l'agafarà per l'argument (parser)
ANY = args.any  # Definim ANY que a l'igual que PORT, ho agafarà per (parser)

def mysigusr1(signum,frame):    # Definim la funció del signal usr1 (kill -10)
  print("Signal handler called with signal:", signum)
  print(llistaPeers)    # Llistem la llista de connexions
  sys.exit(0)
#  
def mysigusr2(signum,frame):    # Definim la funció del signal usr2 (kill -12)
  print("Signal handler called with signal:", signum)
  print(len(llistaPeers))   # Printem el len de la llista de connexions
  sys.exit(0)
#
def mysigterm(signum,frame):    # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum)
  print(llistaPeers, len(llistaPeers))  # Mostrem una llista amb les connexions i el len de totes les connexions que han hagut
  sys.exit(0)
# ---------------------------------------
pid=os.fork()

if pid != 0:    # Fem l'if en funció el PID al pare.
  print("Engegat el server CAL:", pid)
  sys.exit(0)   # PREGUNTAR CANET

signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

while True: # Bucle infinit
  conn, addr = s.accept()
  print("Connected by", addr)
  llistaPeers.append(addr)
  command = "cal %d" % (ANY)
  pipeData = Popen(command,shell=True,stdout=PIPE)
  for line in pipeData.stdout:
    conn.send(line)
  conn.close()
