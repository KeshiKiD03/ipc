# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket,argparse # Importar ARGPARSE

# ARGPARSE

parser = argparse.ArgumentParser(description="""CAL client""") # Se inicializa el ARGPARSE
parser.add_argument("-s","--server",type=str, default='',dest="server") # Se conecta cualquiera. Si no se especifica el SERVIDOR, se conecta a cualquiera a LOCALHOST.
parser.add_argument("-p","--port",type=int, default=50001,dest="port") # El puerto a atacar es 50001
args=parser.parse_args() # Se pulsa el ARGPARSE

# SOCKETS

HOST = args.server # Se definen constantes para indicar a que HOST nos conectaremos, dest=server (Variable del ARGPARSE)
PORT = args.port # Se definen constantes para indicar a que PORT nos conectaremos, dest=port (Variable del ARGPARSE)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Se inicializa el SOCKET para conectarse
s.connect((HOST, PORT)) # Se conecta al SERVIDOR
while True: # Bucle infinit # Para que esté escuchando por si le envían más de 1 línea.
  data = s.recv(1024) # Recibe datos del SERVIDOR.
  if not data: break
  print('Data:', data.decode("utf-8")) # Se printa en modo UTF 8 con DECODE data.decode("utf-8")
s.close()
sys.exit(0)

"""
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
