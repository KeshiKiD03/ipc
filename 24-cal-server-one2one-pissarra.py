# /usr/bin/python
#-*- coding: utf-8-*-
# cal-server-one2one-pissara.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse # 1. Se importan LIBRERÍAS
from subprocess import Popen, PIPE # 2. Se importe PIPE y POPEN de SUBPROCESS.

# -------------------- ARGPARSE

parser = argparse.ArgumentParser(description="""CAL server""") # 3. Se inicializa el ARGPARSE como CAL SERVER.
parser.add_argument("-a","--any",type=int, default=2019) # 4. Argumento posicional e Indica que por defecto un ANY por defecto 2019 (Puerto)
parser.add_argument("-p","--port",type=int, default=50001) # 5. Se crea un argumento POSICIONAL del tipo Integer y por defecto es 50001.
args=parser.parse_args() # 6. Se pulsa el botón del ARGPARSE

# --------------------- SOCKETS PLANTILLA

llistaPeers=[] # 1. Se define una LISTA de las conexiones. 
HOST = '' # 2. Se define una constante HOST (Localhost)
PORT = args.port # 3. Se define el PORT donde cogerá por el ARGUMENTO (parser) (PARSER)
ANY = args.any # 4. Se define una constante ANY que igual que el PORT, lo cogerá por el (parser)

# -------------------- SIGNALS

# Definimos funciones para las SEÑAlES

# Por parámetro de cada función, cogerá el "SIGNUM" y el "FRAME".

def mysigusr1(signum,frame): # 1. Definim la funció del signal usr1 (kill -10)
  print("Signal handler called with signal:", signum) # 2. Printa la señal recibida
  print(llistaPeers) # 3. Llistem la llista de connexions
#  sys.exit(0) # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos
  
def mysigusr2(signum,frame): # 1. # Definim la funció del signal usr2 (kill -12)
  print("Signal handler called with signal:", signum) # 2. 
  print(len(llistaPeers)) # 3. # Printem el len de la llista de connexions # Con la función len(lista)
#  sys.exit(0) # 4. SALE # Si se quiere mantener y saber cuantos tenemos, lo comentamos

def mysigterm(signum,frame): # 1. # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum) # 2. 
  print(llistaPeers, len(llistaPeers)) # 3. # Mostrem una llista amb les connexions i el len de totes les connexions que han hagut
  sys.exit(0) # 4. SALE
  
# -------------------- SIGNALS
  
pid=os.fork() # 1. # Crea una copia del PID, es decir crea un HIJO.
if pid !=0: # 2. # Fem l'if en funció el PID al pare.
  print("Engegat el server CAL:", pid) # 3. El padre ha muerto pero el hijo sigue encendido.
  sys.exit(0) # 4. Sale del programa (Está en DETACH)
  
  
  
signal.signal(signal.SIGUSR1,mysigusr1) # 1. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 10 (KILL -10)) recibida  (signal.SIGUSR1) + Llamará a la FUNCIÓN (mysigur1) = Listará la lista de Conexiones) 


signal.signal(signal.SIGUSR2,mysigusr2) # 2. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 12 (KILL -12)) recibida  (signal.SIGUSR2) + Llamará a la FUNCIÓN (mysigur2) = Listará la LONGITUD de CONEXIONES (len))

 
signal.signal(signal.SIGTERM,mysigterm) # 3. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGTERM = 15 (KILL -15)) recibida  (signal.SIGTERM) + Llamará a la FUNCIÓN (mysigterm) = Terminará el programa y LISTARÁ la lista y la LONGITUD de CONEXIONES (len)) 


# -------------------- SERVIDOR SE PONE A ESCUCHAR (SOCKET)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1. Se activa el SOCKET
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 2. Se reusa el SOCKET
s.bind((HOST,PORT)) # 3. Hace el enlace de HOST y PORT
s.listen(1) # 4. Se queda escuchando.


############# 


while True: # Bucle infinit # Para que esté escuchando, para que esté atendiendo una conexión detrás de otro
  conn, addr = s.accept() # # Implementa el ACCEPT. 
        # Hasta que no acepte la conexión, no hace el accept.
	# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).
  print("Connected by", addr) # Indica quién está conectado.
  llistaPeers.append(addr) # Lo registra en la LISTA de conexiones
  # En la lista vacía, cada HOST que se conecte al SERVIDOR, lo REGISTRA. Hace un APPEND. Lo añade al final de la LISTA (OBJETO).
  command = "cal %d" % (ANY) # Se establece el comando CAL y se le pasa a ANY (PUERTO)
  
  # %d es para pasar una VARIABLE. # Pasará la orden CAL por el PUERTO ANY (Puerto dinámico para el Puerto ORIGEN)
  
  pipeData = Popen(command,shell=True,stdout=PIPE) # En la variable pipeData, le pasamos un POPEN(Contiene el COMANDO y la salida estándar PIPE) 
	# La salida estándar será el PIPE
# RECORRE EL POPEN Y LE ENVÍA EL COMANDO
  # Shell = True es IMPORTANTE
  for line in pipeData.stdout: # Para cada línea de la salida estándar
    conn.send(line) # Envía cada LÍNEA al CLIENTE
  conn.close() # Cierra la conexión con el CLIENTE.

sys.exit(0) # Sale del PROGRAMA.
  
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
  
  
  
  
 
### SOLUCIÓN

# CLIENTE

	1. Se conecta a ATACAR al SERVIDOR que quiere. Y el PUERTO también.
	
	2. Se conecta al SOCKET destino, mediante HOST y PORT y se queda ESCUCHANDO.
	
	3. Cuando ya no tenga más datos a RECIBIR. Hace un BREAK. Finaliza y muestra la información en DESCODIFICACIÓN DE BINARIO A UTF8

# SERVIDOR

	1. Se abre el SERVIDOR en DETACH, el CLIENTE se conecta. 
	
	2. El servidor CALENDAR, le vomita la información.
	
	3. El CLIENTE finaliza.
	
	4. El SERVIDOR escucha al siguiente y lo añade a una LISTA VACÍA mediante APPEND.
	
	5. Le envíamos con un KILL -15 $(pgrep python).
	
	6. El SERVIDOR responde:
	
	ubuntu@keshi:~/Documents/ipc$ kill -15 $(pgrep python)
ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52574), ('127.0.0.1', 52576)] 2

	7. Significa que ha recibido la SEÑAL 15 que es SIGTERM --> Si ha recibido esa señal, termina el programa Y MOSTRARÁ QUIÉN SE HA CONECTADO + LA LONGITUD de USUARIOS CONECTADOS 
	
	
	---
	
	
## KILL y PRUEBAs

1. Se enciende el SERVIDOR en DETACH.

2. El cliente se conecta (s.connect((HOST,PORT)))y hace PETICIONES, se queda ESCUCHANDO y RECIBIENDO MENSAJES Infinitamente. Hasta que no tenga nada más que recibir.

3. El cliente finaliza y se conecta otro desde otro puerto dinámico de ORIGEN.

4. El servidor va registrando quién entra IP y PORT y CUENTA cuantos usuarios HAN ENTRADO (Lista vacía llistaPeers.append(addr, lo printa con un len print(llistaPeers, len(llistaPeers)) )
	
5. Desde otra CONSOLA le enviamos: (Se han CONECTADO 3 CLIENTES 1by1, de uno en uno)

	kill -10 $(pgrep python) --> SIGUSR1 (Print de CONEXIONES ACTIVAS)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 10
[('127.0.0.1', 52582), ('127.0.0.1', 52584)]
Connected by ('127.0.0.1', 52586)

	
	kill -12 $(pgrep python) --> SIGUSR2 (Print de CUANTOS SE HAN CONECTADO (LEN(lista)))

	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 12
3


	kill -15 $(pgrep python) --> SIGTERM 15 (TERMINA EL PROGRAMA)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52582), ('127.0.0.1', 52584), ('127.0.0.1', 52586)] 3

	
	
IMPORTANTE EL SYS.EXIT(0) LO HEMOS QUITADO UN MOMENTO DEL CLIENTE

#  sys.exit(0) # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos


"""



