# /usr/bin/python
#-*- coding: utf-8-*-
# cal-server-one2one-pissara.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket,os,signal,argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""CAL server""")
parser.add_argument("-a","--any",type=int, default=2019)
parser.add_argument("-p","--port",type=int, default=50001)
args=parser.parse_args()
llistaPeers=[]
HOST = ''
PORT = args.port
ANY = args.any

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
  print("Engegat el server CAL:", pid)
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
  command = "cal %d" % (ANY)
  pipeData = Popen(command,shell=True,stdout=PIPE)
  for line in pipeData.stdout:
    conn.send(line)
  conn.close()
  
  
"""
SOLUCIÓN:


**24-calendar-client-one2one.py [-s server] [-p port]**

**24-calendar-server-one2one.py [-p port] [-a any]**

  Calendar server amb un popen, el client es connecta i rep el calendari. El server 
  tanca la connexió amb el client un cop contestat però continua escoltant noves connexions.

  El server ha de governar-se amb senyals que fan:
   - sigusr1: llista de peers i plega.
   - sigusr2: count de listpeer i plega.
   - sigterm: llista de peers, count i plega.

  El server és un daemon que es queda en execució després de fer un fork del seu
  pare (que mor) i es governa amb senyals.

  Que sigui el servidor qui rep l'any com a argument és una tonteria, seria més lògic
  fer-ho en el client, però el diàleg client servidor queda per a una pràctica
  posterior. Aquí es vol practicar usar un arg en el popen.

"""



