# /usr/bin/python
#-*- coding: utf-8-*-
# cal-server-one2one-pissara.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
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


# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!

signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

# Lo de arriba es una plantilla

# Aquí es donde se hace TODO

while True: # Bucle infinit # Bucle infinit (atendre connexions un darrera l'altre)
  conn, addr = s.accept() # Guardem les variables conn i addr
  print("Connected by", addr) #  Printem
  llistaPeers.append(addr) # Lo añade a una LISTA
  fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%S"))
  fileLog=open(fileName,"w")
  while True:
  	data = conn.recv(1024)
  	if not data: break # Cuando el otro me ha penjado el teléfono cierra
  	fileLog.write(str(data))
  conn.close() # Cierra la conexión # Liberar el SOCKET.
  fileLog.close() # Cierra
  
  # Acepta un CLIENTE
  
  
"""

### CORREGIDA

PROGRAMA TIENE LA SEÑAL 1

VA ACUMULANDO LAS SEÑALES

SERVIDOR ONE 2 ONE --> ACEPTA UNA CONEXIÓN AL MISMO TIEMPO.


Todo el programa va en el WHILE TRUE (Está todo ahí)

El resto es una PLANTILLA. [IMPORTANTE]







Se conectan al puerto 50001 y se guarda en un FICHERO.

El servidor hace un WHILE TRUE (Cada iteración atiende un cliente, a la propera atiende a otro)




## CORREGIR PROGRAMA SERVIDOR

## EXPLICACIÓN

WHILE TRUE:
-----
	aceptar la conexión

	nom = generar_nom

	open del fitxer
	
	bucle
	
		read del socket
		
		write fitxer

	cerrar el fitxer

	socket.close() --> Cerrar el socket

----






1. Necesitamos el NETCAT

	nc -l 50001

2. Se conecta, vomita y cierra. --> python3 25-ps-client... localhost

3. En el SERVIDOR se verifica


isx36579183@i11:~/Documents/ipc$ nc -l 50001
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:02 /sbin/init
      2 ?        S      0:00 [kthreadd]
      3 ?        I<     0:00 [rcu_gp]
      4 ?        I<     0:00 [rcu_par_gp]
      6 ?        I<     0:00 [kworker/0:0H-events_highpri]
      8 ?        I      0:00 [kworker/u16:0-flush-259:0]
      9 ?        I<     0:00 [mm_percpu_wq]
     10 ?        S      0:00 [rcu_tasks_rude_]
     11 ?        S      0:00 [rcu_tasks_trace]
     12 ?        S      0:00 [ksoftirqd/0]
     13 ?        I      0:00 [rcu_sched]
     14 ?        S      0:00 [migration/0]
     15 ?        S      0:00 [cpuhp/0]
     16 ?        S      0:00 [cpuhp/1]
     17 ?        S      0:00 [migration/1]
     18 ?        S      0:00 [ksoftirqd/1]
     20 ?        I<     0:00 [kworker/1:0H-events_highpri]
     21 ?        S      0:00 [cpuhp/2]
     22 ?        S      0:00 [migration/2]
     23 ?        S      0:00 [ksoftirqd/2]
     25 ?        I<     0:00 [kworker/2:0H-kblockd]
     26 ?        S      0:00 [cpuhp/3]
     27 ?        S      0:00 [migration/3]

.......






"""
