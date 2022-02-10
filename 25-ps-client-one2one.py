# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse # Importamos librerias
from subprocess import Popen, PIPE

# ------------- ARGPARSE

parser = argparse.ArgumentParser(description="""PS Client""")
parser.add_argument("-p","--port",type=int, default=50001) # Optional parameter como puerto default 50001
parser.add_argument("server",type=str) # Se conecta cualquiera
args=parser.parse_args()

# ---------------------------------------

# ------------- SOCKETS

HOST = args.server # A la constante se le pasa un ARGUMENTO POSICIONAL.
PORT = args.port # A la constante se le pasa un ARGUMENTO OPCIONAL.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abre el SOCKET TCP # Se inicializa el SOCKET para conectarse
s.connect((HOST, PORT)) # Se conecta AL SERVIDOR

command = "ps ax" # Le pasamos el comando PS AX # Especifiquem la commanda que s'executarà (%d (integer), %s (string)--> any passat per argument)
pipeData = Popen(command, shell=True, stdout=PIPE) # Popen (shell=True --> es perquè funcioni)
# En la variable pipeData, le pasamos un POPEN(Contiene el COMANDO y la salida estándar PIPE) 
	# La salida estándar será el PIPE
# RECORRE EL POPEN Y LE ENVÍA EL COMANDO
  # Shell = True es IMPORTANTE

for line in pipeData.stdout: # Recorre el tubo # Enviem per el socket les linees
	s.send(line) # Recoge el tubo 
	
s.close()  # Tanquem el socket (connexió)
sys.exit(0)

"""
	1. El cliente se conecta (Se le pasan argumentos)
	
	2. Se abre el SOCKET TCP del CLIENTE.
	
	3. El cliente LE MANDA EL comando "ps ax" al SERVIDOR.
	
		* Para cada línea de la salida estándar de pipeData, le envías con un s.send(line) al SERVIDOR.
	
	4. El servidor lo VOMITA y hace un PRINT.


	* El cliente cierra la conexión y se va.
	
	
NOTAS: No hace falta While true porque estamos enviando un comando y sabemos que el comando retornará un valor definido.

PRUEBAS: Con nc

	1. nc -l 50001
	
	2. python3 25-ps-client*.py localhost
	
	3. En el SERVIDOR se verifica y printa:
	
	```

  23369 pts/0    S+     0:00 nc -l 50001
  23371 pts/1    Ss     0:00 bash
  23398 pts/1    S+     0:00 python3 25-ps-client-one2one.py localhost
  23399 pts/1    S+     0:00 /bin/sh -c ps ax
  23400 pts/1    R+     0:00 ps ax
keshi@KeshiKiD03:~$ 

	```

"""
