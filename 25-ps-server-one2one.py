# /usr/bin/python
#-*- coding: utf-8-*-
# ps-server-one2one-pissara.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE

# SE IMPORTAN LIBRERÍAS

## --------- ARGPARSE

# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """PS server""")

parser.add_argument("-a","--any",type=int, default=2022)

parser.add_argument("-p","--port",type=int, default=50001)

args=parser.parse_args()
# -------------------------------------

## --------- SOCKETS

llistaPeers=[]  # Definim la llista buida de les connexions
HOST = ''   # Definim com a HOST (localhost)
PORT = args.port    # Definim el PORT que l'agafarà per l'argument (parser)
ANY = args.any  # Definim ANY que a l'igual que PORT, ho agafarà per (parser)

## --------- SIGNALS MYHANDLER

def mysigusr1(signum,frame): # 1. Definim la funció del signal usr1 (kill -10)
  print("Signal handler called with signal:", signum) # 2. Printa la señal recibida
  print(llistaPeers) # 3. Llistem la llista de connexions
  sys.exit(0) # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos

def mysigusr2(signum,frame): # 1. # Definim la funció del signal usr2 (kill -12)
  print("Signal handler called with signal:", signum) # 2. 
  print(len(llistaPeers)) # 3. # Printem el len de la llista de connexions # Con la función len(lista)
  sys.exit(0) # 4. SALE # Si se quiere mantener y saber cuantos tenemos, lo comentamos

def mysigterm(signum,frame): # 1. # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum) # 2. 
  print(llistaPeers, len(llistaPeers)) # 3. # Mostrem una llista amb les connexions i el len de totes les connexions que han hagut
  sys.exit(0) # 4. SALE

# ---------------------------------------

# -------------------- SIGNALS + FORK()


pid=os.fork() # 1. # Crea una copia del PID, es decir crea un HIJO.

if pid !=0: # 2. # Fem l'if en funció el PID al pare.
  print("Engegat el server CAL:", pid) # 3. El padre ha muerto pero el hijo sigue encendido.
  sys.exit(0) # 4. Sale del programa (Está en DETACH)


# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!



signal.signal(signal.SIGUSR1,mysigusr1) # 1. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 10 (KILL -10)) recibida  (signal.SIGUSR1) + Llamará a la FUNCIÓN (mysigur1) = Listará la lista de Conexiones) 


signal.signal(signal.SIGUSR2,mysigusr2) # 2. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 12 (KILL -12)) recibida  (signal.SIGUSR2) + Llamará a la FUNCIÓN (mysigur2) = Listará la LONGITUD de CONEXIONES (len))

 
signal.signal(signal.SIGTERM,mysigterm) # 3. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGTERM = 15 (KILL -15)) recibida  (signal.SIGTERM) + Llamará a la FUNCIÓN (mysigterm) = Terminará el programa y LISTARÁ la lista y la LONGITUD de CONEXIONES (len)) 




# -------------------- SERVIDOR SE PONE A ESCUCHAR (SOCKET)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1. Se activa el SOCKET
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 2. Se reusa el SOCKET
s.bind((HOST,PORT)) # 3. Hace el enlace de HOST y PORT
s.listen(1) # 4. Se queda escuchando.


# ---------------------------------- EL PROGRAMA

############# 


# Lo de arriba es una plantilla

# Aquí es donde se hace TODO

while True: # Bucle infinit # Bucle infinit (atendre connexions un darrera l'altre)
  conn, addr = s.accept() # Guardem les variables conn i addr # # Implementa el ACCEPT. 
        # Hasta que no acepte la conexión, no hace el accept.
	# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).
  print("Connected by", addr) # Indica quién está conectado.
  llistaPeers.append(addr) # Lo registra en la LISTA de conexiones
  # En la lista vacía, cada HOST que se conecte al SERVIDOR, lo REGISTRA. Hace un APPEND. Lo añade al final de la LISTA (OBJETO).
  
  # --- APERTURA DE FICHERO
  
  fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%S")) # Se especifica en la variable, la ruta del FICHERO. 
  # fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%S"))
  	
  	# 1. %s - %s - %s.log --> Indica que son 3 variables STRING.
  	
  	# 2. En la primera posición de la ADDR[0] = Irá la IP.
  	
  	# 3. En la segunda posición de la ADDR[1] = Irá el PUERTO.
  	
  	# 4. Luego se especifica otro string, este caso, de la librería time. --> Usamos strftime(""%Y%m%d-%H%M%S"") --> Tendrá un Formato de Año, Mes, Dia, Hora, Min y Seg.
  
  fileLog=open(fileName,"w") # Se abre un FICHERO especificado en fileName con sus características.
  
  # -----------------------------
  
  while True: # Se realiza un BUCLE INFINITO para estar ESCUCHANDO el SERVIDOR.
  	
  	
  	data = conn.recv(1024) # El servidor está recibiendo DATOS del CLIENTE. (Está recibiendo porque el CLIENTE le manda el COMANDO.)
  	
  	
  	if not data: break # Cuando el otro me ha penjado el teléfono cierra. Si ya no hay más datos a recibir por parte del CLIENTE, salta del programa.
  	
  	
  	fileLog.write(str(data)) # Se realiza un write del fileLog(str(data)) --> Se lo pasamos en formato string plano.
  	
  conn.close() # Cierra la conexión con el CLIENTE # Liberar el SOCKET.
  fileLog.close() # Cierra EL FICHERO.
  
  # Acepta un CLIENTE

# No le ponemos el SYS.EXIT(0) porque sino se va y el CLIENTE no mostrará


"""
	TROUBLESHOOT: 
	
		¿En que casos usar "ESTAR ESCUCHANDO" -->data = s.recv(1024) (Si es CLIENTE) o conn.recv(1024) (Si es SERVIDOR)?
		
			* En este caso SIEMPRE que haya alguien "TANTO CLIENTE como SERVIDOR estén ENVIANDO datos a través del SOCKET"
			
				* En este caso el CLIENTE manda el COMANDO por POPEN (stdout) y el SERVIDOR lo recive (data = conn.recv(1024))

	RESUMEN:
	
		1. El CLIENTE quiere conectarse al SERVIDOR.
		
		2. El SERVIDOR acepta el CLIENTE.
		
		3. Cada CLIENTE que se conecte se guardará su ADDR (IP y PUERTO ORIGEN) a una lista (llistaPeers) y se añadirá al final de cada línea del fichero.
		
		4. El CLIENTE le manda el COMANDO "PS AX" y todo su CONTENIDO LO VOMITA en la salida estándar del PIPE.
		
		5. El CLIENTE, para cada línea del COMANDO (No requiere While true), hace un s.send(line) --> Envía cada línea por el SOCKET de DESTINO.
		
		6. El SERVIDOR recibe los DATOS del CLIENTE --> data = conn.recv(1024) # ESCUCHA DEL SOCKET
		
		7. Se quedará escuchando hasta que el CLIENTE termine de enviarle DATOS. Ahí data valdrá NONE, entonces salta un BREAK.
		
		8. Para cada dispositivo que se conecte al SERVIDOR, se escribirá en el fichero fileLog quién se ha CONECTADO ((IP y PUERTO) y la HORA TIMESTAMP).
		
		9. El CLIENTE termina la conexión con el SERVIDOR. --> s.close()
		
		9. El SERVIDOR termina la conexión con el CLIENTE. --> conn.close() # CIERRA EL SOCKET
		
		10. El SERVIDOR cierra su fichero fileLog. --> fileLog.close()
		
		11. Sale del programa --> sys.exit(0)
		
		----
		
		# EXTRA SI LE PASAMOS SEÑALES 10 12 Y 15
		
		1. 10 SIGUSR1 - Muestra los SE HAN CONECTADO al SERVIDOR. (llistaPeers)
		
		2. 12 SIGUSR2 - Muestra CUANTOS SE HAN CONECTADO al SERVIDOR. len(llistaPeers)
		
		3. 15 Termina y sale del programa --> ACCIÓN: Printa los QUE SE HAN CONECTADO y CUANTOS (llistaPeers) se han CONECTADO (len(llistaPeers)).


		----- IMPORTANTE
		
		* EL SERVIDOR NO MUESTRA EL CONTENIDO DE PS AX -->
		
			* SINO QUE LO GUARDA EN EL FICHERO.
			
		* Lo visualizamos en /tmp/
		
keshi@KeshiKiD03:/tmp$ ls -l

total 264
-rw-rw-r-- 1 keshi keshi 24749 feb  9 23:58 127.0.0.1-52192-20220209-235856.log
-rw-rw-r-- 1 keshi keshi 24782 feb  9 23:59 127.0.0.1-52194-20220209-235955.log
-rw-rw-r-- 1 keshi keshi 25013 feb 10 00:04 127.0.0.1-52196-20220210-000434.log
-rw-rw-r-- 1 keshi keshi 25047 feb 10 00:05 127.0.0.1-52198-20220210-000506.log
-rw-rw-r-- 1 keshi keshi 25150 feb 10 00:09 127.0.0.1-52200-20220210-000909.log
-rw-rw-r-- 1 keshi keshi 23671 feb 10 00:15 127.0.0.1-52202-20220210-001504.log


		* Observamos que se la sintaxis cumple con lo indicado.
		
			127.0.0.1-52192-20220209-235856.log
			
			[127.0.0.1] = addr[0] = IP ORIGEN 
			
			[52192] = addr[1] = PUERTO DINÁMICO ORIGEN
			
			[20220209-235856] = strftime
			
			("%Y%m%d-%H%M%S").log
			
			
	DENTRO: 
	
	keshi@KeshiKiD03:/tmp$ cat 127.0.0.1-52192-20220209-235856.log 
b'    PID TTY      STAT   TIME COMMAND\n'b'      1 ?        Ss     0:07 /sbin/init splash\n'b'      2 ?        S      0:00 [kthreadd]\n'b'      3 ?        I<     0:00 [rcu_gp]\n'b'      4 ?        I<     0:00 [rcu_par_gp]\n'b'      6 ?        I<     0:00 [kworker/0:0H-events_highpri]\n'b'      8 ?        I<     0:00 [mm_percpu_wq]\n'b'      9 ?        S      0:00 [rcu_tasks_rude_]\n     10 ?        S      0:00 [rcu_tasks_trace]\n     11 ?        S      0:00 [ksoftirqd/0]\n     12 ?        I      0:02 [rcu_sched]\n'b'     13 ?        S      0:00 [migration/0]\n     14 ?        S      0:00 [idle_inject/0]\n     16 ?        S      0:00 [cpuhp/0]\n     17 ?        S      0:00 [cpuhp/1]\n     18 ?        S      0:00 [idle_inject/1]\n     19 ?        S      0:00 [migration/1]\n     20 ?        S      0:00 [ksoftirqd/1]\n     22 ?        I<     0:00 [kworker/1:0H-events_highpri]\n     23
		

####################################################3


### CORREGIDA EN CLASE

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
