# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse # Importamos librerias
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description="""PS Client""")
parser.add_argument("-p","--port",type=int, default=50001) # Optional parameter como puerto default 50001
parser.add_argument("server",type=str) # Se conecta cualquiera # Positional parameter
args=parser.parse_args()

# ---------------------------------------
HOST = args.server
PORT = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abre el SOCKET TCP
s.connect((HOST, PORT)) # Se conecta

command = "ps ax" # Le pasamos el comando PS AX # Especifiquem la commanda que s'executarà (%d (integer), %s (string)--> any passat per argument)
pipeData = Popen(command, shell=True, stdout=PIPE) # Popen (shell=True --> es perquè funcioni) # Hace el POPEN y el TUBO VOMITA al PIPE.


for line in pipeData.stdout: # Recorre el tubo # Enviem per el socket les linees # Lo que hace es LEER Y ENVIAR
	s.send(line) # Recoge el tubo  # ENVIA
	
s.close()  # Tanquem el socket (connexió)
sys.exit(0)



"""

### CORREGIDA

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
