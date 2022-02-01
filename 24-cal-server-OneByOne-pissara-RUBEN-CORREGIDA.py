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
  
# 

signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

# Cargar las 3 señales, definir el SOCKET

while True: # Bucle infinit # Para que esté escuchando, para que esté atendiendo una conexión detrás de otro
  conn, addr = s.accept()
  print("Connected by", addr)
  llistaPeers.append(addr) # Lo registra en la lsita de conexiones
  command = "cal %d" % (ANY)
  pipeData = Popen(command,shell=True,stdout=PIPE)
  for line in pipeData.stdout:
    conn.send(line)
  conn.close()
  
# Shell True, si no se pone no funciona.

# %d es para pasar una VARIABLE.
  

"""

## NOMBRE DEL PROGRAMA + SINTAXIS

24 SERVIDOR
  
  Mostrar les deu primeres línies de file o stdin

# ----------------------------------------------

## Explicación

Mostrar les 10 primeres línies d'un fitxer. 
El nom del fitxer a mostrar es rep com a argument, sinó es rep, 

es mostren les deu primeres línies de  l'entrada estàndard. 

Sinpsys: $ head [file] 


# ----------------------------------------------

## Metodología

1. 

2.

3.

4.

5.

6.

7.

8.

9.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

20.







"""
