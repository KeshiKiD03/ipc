# /usr/bin/python
#-*- coding: utf-8-*-
# server01.py
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time,codecs
from subprocess import Popen, PIPE

# S'importen les LLIBRERIES SYS, SOCKET, OS, SIGNAL, ARGPARSE, TIME

# Desde subprocess, importem Popen i PIPE

## --------- ARGPARSE

# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """Server Aaron Examen, server01""")

parser.add_argument("-d","--debug",action='store_true',default=False) # La opció es per a que hi surti el DEBUG
parser.add_argument("-p","--port",type=int, default=44444) # Argument opcional, per defecte es 44444

args=parser.parse_args() # Apreta el botó de ARGPARSE
# -------------------------------------

## --------- SOCKETS

llistaPeers=[]  # Definim la llista buida de les connexions
HOST = ''   # Definim com a HOST (localhost)
PORT = args.port    # Definim el PORT que l'agafarà per l'argument (parser)
DEBUG = args.debug  # Definim DEBUG, a l'igual que PORT, ho agafarà per (parser)
FI = bytes(chr(4), 'utf-8') # END OF TRANSMITION

## --------- SIGNALS MYHANDLER()

def mysigusr1(signum,frame): # 1. Definim la funció del signal usr1 (kill -10)
  print("Signal handler called with signal:", signum) # 2. Printa la señal rebuda
  print(llistaPeers) # 3. Llistem la llista de connexions
  sys.exit(0) # # 4. Surt del programa, si es vol mantenir i saber quants tenim, el comenten
  
def mysigusr2(signum,frame): # 1. Definim la funció del signal usr2 (kill -12)
  print("Signal handler called with signal:", signum) # 2. Printa la señal rebuda
  print(len(llistaPeers)) # 3. # Printem el len de la llista de connexions # Con la función len(lista)
  sys.exit(0) # # 4. Surt del programa, si es vol mantenir i saber quants tenim, el comenten

def mysigterm(signum,frame): # 1. # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum) # 2. Printa la señal rebuda
  print(llistaPeers, len(llistaPeers)) # 3. # Mostrem una llista amb les connexions i el len de totes les connexions que han hagut
  sys.exit(0) # # 4. Surt del programa, si es vol mantenir i saber quants tenim, el comenten

# ---------------------------------------

# -------------------- SIGNALS + FORK()

## A partir d'aquí es queda en DETACH!! EL PARE MOR PERO EL FILL ES QUEDA ESCOLTANT FINS A L'INFINIT I MÉS ENLLÀ!!!!!!!!!!!!

pid=os.fork() # 1. # Crea una copia del PID, es a dir, crea un FILL.

if pid !=0: # 2. # Fem l'if en funció del en funció del PID del Pare, espera al seu FILL.
  print("Engegat el server KESHI:", pid) # 3. El padre ha muerto pero el hijo sigue encendido.
  sys.exit(0) # 4. Sale del programa (Está en DETACH) // D'ara endavant mana el FILL, el crack.


# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!



signal.signal(signal.SIGUSR1,mysigusr1) # 1. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 10 (KILL -10)) recibida  (signal.SIGUSR1) + Llamará a la FUNCIÓN (mysigur1) = Listará la lista de Conexiones) 


signal.signal(signal.SIGUSR2,mysigusr2) # 2. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 12 (KILL -12)) recibida  (signal.SIGUSR2) + Llamará a la FUNCIÓN (mysigur2) = Listará la LONGITUD de CONEXIONES (len))

 
signal.signal(signal.SIGTERM,mysigterm) # 3. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGTERM = 15 (KILL -15)) recibida  (signal.SIGTERM) + Llamará a la FUNCIÓN (mysigterm) = Terminará el programa y LISTARÁ la lista y la LONGITUD de CONEXIONES (len)) 




# -------------------- SERVIDOR ES POSA A ESCOLTAR (SOCKET ORIGEN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1. Se activa el SOCKET / # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 2. Se reusa el SOCKET
s.bind((HOST,PORT)) # 3. Hace el enlace de HOST y PORT
s.listen(1) # 4. Se queda escuchando.


# ---------------------------------- EL PROGRAMA

############# 


# Lo de arriba es una plantilla

# Aquí es donde se hace TODO

while True: # Bucle infinit - (atendre connexions un darrera l'altre) - "ONE2ONE"
	conn, addr = s.accept() # Guardem les variables "conn" i "addr" # # Implementa el ACCEPT. 
        # Hasta que no acepte la conexión, no hace el accept. Se queda "enganchado".
	# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).
	if args.debug: # Args.debug = Debug --> Depura e Imprime en el servidor el resultado si no hay errores
		print("Connected by:", addr) # Indica quién está conectado.
	llistaPeers.append(addr) # Lo registra en la LISTA de conexiones
  # En la lista vacía, cada HOST que se conecte al SERVIDOR, lo REGISTRA. Hace un APPEND. Lo añade al final de la LISTA (OBJETO).
	while True: # Se realiza un BUCLE INFINITO para estar ESCUCHANDO el SERVIDOR.	
  		data = conn.recv(1024) # El servidor está recibiendo DATOS del CLIENTE. (Está recibiendo porque el CLIENTE le manda el COMANDO.)
#  		data = str(str, 'UTF-8') # NO WORK
#  		dataString = ''.join(map(chr, data)) # CONVERTIR BYTES A STRING
#  		if args.debug:
#  			print ("Comanda:", data)
  		if not data:
  			if args.debug:
  				print("No s'ha rebut una comanda, tanco connexio amb %s ,adeu" % (addr[0]))
  			conn.close() # Tanca la connexió
  			break # Cuando el otro me ha penjado el teléfono cierra. Si ya no hay más datos a recibir por parte del CLIENTE, salta del programa.
  		data = data[:-1]
  		print(data)
  		if data == b'processos':
  			data = "ps ax"
  		elif data == b'ports':
  			data = "netstat -puta"
  		elif data == b'whoareyou':
  			data = "uname -a"
  		else:
  			data = "uname -a"		
  		pipeData = Popen(data, shell=True, stdout=PIPE, stderr=PIPE) # Se crea un TUBO (pipeData) donde enviará "data" por la SALIDA ESTÁNDAR (1) = PIPE y la SALIDA de ERROR también por el PIPE
  		for line in pipeData.stdout: # Se recorre cada LÍNEA de la SALIDA ESTÁNDAR (1)
#  			lineString = ''.join(map(chr, line))
  			if args.debug: # Args.debug = Debug --> Depura e Imprime en el servidor el resultado si no hay errores
  				# lineString = ''.join(map(chr, line))
  				print("Enviant:", line) # Printa cada línea.
  			conn.sendall(line) # Envía la línea # Se asegura de vacíar el bufer, envía todo.
  		for line in pipeData.stderr:# Pipe de ERROR
  			#lineString = ''.join(map(chr, line))
  			if args.debug:
  				print("Enviant error:", line)
  			conn.sendall(line) # Envía la línea
  		conn.sendall(FI)
	conn.close()
s.close()
sys.exit(0)

"""

116
#  			processos en rebre aquesta instrucció el servidor executarà l’ordre “ps ax” i retornarà el resultat al client.


117
#  			ports en rebre aquesta ordre el servidor executarà l’ordre “netstat -puta” i retornarà el resultat al client. 

119
# 			whoareyou en rebre aquesta ordre el servidor executa l’ordre “uname -a” i retorna el resultat al client.

120
#  			Qualsevol altre ordre rebuda del client és processada igual que “whoareyou”.


	TROUBLESHOOT: 
	
		¿En que casos usar "ESTAR ESCUCHANDO" -->data = s.recv(1024) (Si es CLIENTE) o conn.recv(1024) (Si es SERVIDOR)?
		
			* En este caso SIEMPRE que haya alguien "TANTO CLIENTE como SERVIDOR estén ENVIANDO datos a través del SOCKET"
			
				* En este caso el CLIENTE manda el COMANDO por POPEN (stdout) y el SERVIDOR lo recive (data = conn.recv(1024))

	RESUMEN:
	
		1. El CLIENTE NC quiere conectarse al SERVIDOR.
		
		2. El SERVIDOR acepta el CLIENTE.
		
		3. Cada CLIENTE que se conecte se guardará su ADDR (IP y PUERTO ORIGEN) a una lista (llistaPeers) y se añadirá al final de cada línea del fichero.
		
		4. El CLIENTE le manda el COMANDO y todo su CONTENIDO LO VOMITA en la salida estándar del PIPE.
		
		5. El CLIENTE, para cada línea del COMANDO (No requiere While true), hace un s.send(line) --> Envía cada línea por el SOCKET de DESTINO.
		
		6. El SERVIDOR recibe los DATOS del CLIENTE --> data = conn.recv(1024) # ESCUCHA DEL SOCKET
		
		7. Se quedará escuchando hasta que el CLIENTE termine de enviarle DATOS. Ahí data valdrá NONE, entonces salta un BREAK.
		
		8. El CLIENTE termina la conexión con el SERVIDOR. --> s.close()
		
		9. El SERVIDOR termina la conexión con el CLIENTE. --> conn.close() # CIERRA EL SOCKET
		
		10. Sale del programa --> sys.exit(0)
		
		----
		
		# EXTRA SI LE PASAMOS SEÑALES 10 12 Y 15
		
		1. 10 SIGUSR1 - Muestra los SE HAN CONECTADO al SERVIDOR. (llistaPeers)
		
		2. 12 SIGUSR2 - Muestra CUANTOS SE HAN CONECTADO al SERVIDOR. len(llistaPeers)
		
		3. 15 Termina y sale del programa --> ACCIÓN: Printa los QUE SE HAN CONECTADO y CUANTOS (llistaPeers) se han CONECTADO (len(llistaPeers)).


		----- IMPORTANTE
		
		* EL CLIENTE NETCAT mostrará TODOS LOS COMANDOS QUE LE PASEMOS "px ax" - "netstat -puta" - "uname -a"  ....
		
			* Órdenes que tampoco existen, lo procesa y muestra ERROR.
			

####################################################3


### CORREGIDA EN CLASE

PROGRAMA TIENE LA SEÑAL 1

VA ACUMULANDO LAS SEÑALES

SERVIDOR ONE 2 ONE --> ACEPTA UNA CONEXIÓN AL MISMO TIEMPO.


Todo el programa va en el WHILE TRUE (Está todo ahí)

El resto es una PLANTILLA. [IMPORTANTE]







Se conectan al puerto 44444 y devuelve el RESULTADO por STDOUT (1) y si hubier ERROR pues por STDERR (2).

El servidor hace un WHILE TRUE (Cada iteración atiende un cliente, a la propera atiende a otro).




### VERIFICACIÓN



1. Necesitamos el NETCAT como CLIENTE

	nc localhost 44444


isx36579183@i14:~/Documents$ nc localhost 44444
ls
Apertura-Servidor01.png
Desktop
Documents
Downloads
isx36579183
KILL-10-SIGUSR1.png
KILL-12-SIGUSR2.png
KILL-15-SIGTERM.png
Music
NC-ClientePruebaPSAX.png
NC-Cliente-Prueba-uname-a.png
Pictures
Prova-Comandes-PSAX-UNAMEA-Netstat-whoareyou.png
Public
server01.py
Templates
Videos
ps ax
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:02 /sbin/init
      2 ?        S      0:00 [kthreadd]
      3 ?        I<     0:00 [rcu_gp]
      4 ?        I<     0:00 [rcu_par_gp]
      6 ?        I<     0:00 [kworker/0:0H-events_highpri]
      9 ?        I<     0:00 [mm_percpu_wq]
     10 ?        S      0:00 [rcu_tasks_rude_]
     11 ?        S      0:00 [rcu_tasks_trace]
     12 ?        S      0:00 [ksoftirqd/0]
     13 ?        I      0:02 [rcu_sched]
     14 ?        S      0:00 [migration/0]
     15 ?        S      0:00 [cpuhp/0]
     16 ?        S      0:00 [cpuhp/1]
.....


uname -a
Linux i14 5.10.0-8-amd64 #1 SMP Debian 5.10.46-4 (2021-08-03) x86_64 GNU/Linux

netstat -puta
/bin/sh: 1: netstat: not found

vivakoeman 
/bin/sh: 1: vivakoeman: not found


....



"""
