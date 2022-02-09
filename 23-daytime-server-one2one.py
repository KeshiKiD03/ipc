# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-server-one2one.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, socket, argparse # Importa LIBRERIA SYS + ARGPARSE + SOCKET
from subprocess import Popen, PIPE # De subprocess, importa Popen y PIPE

## ARGPARSE

parser = argparse.ArgumentParser(description="""Daytime server""") # Llamamos el ARGUMENT PARSE
parser.add_argument("-p","--port",type=int, help="Port per on connectar nos", default=50001, dest="port")
args=parser.parse_args()


## SOCKET

HOST = ''
PORT = args.port # Indicamos que en la variable posicional de "args", me seleccionas .port = 50001 (Port defecto) o indicar.



#-------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Ens permet reutilitzar les IPs
s.bind((HOST,PORT)) # Hace el enlace del HOST y PORT. 
s.listen(1)

## DAYTIME SERVER ARGS --PORT

while True: # Bucle infinito # Bucle perquè no sabem quan acabarà ja que no sabem quantes línees ens enviarà
	conn, addr = s.accept() # Implementa el ACCEPT. 
        # Hasta que no acepte la conexión, no hace el accept.
	# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).
	print("Connected by", addr) # Printem qui s'ha connectat. Mostra IP
	command = ["date"]
	# Li especifiquem el command que utiltizarem
	pipeData = Popen(command,shell=True,stdout=PIPE)  # En la variable pipeData, le pasamos un POPEN(Contiene el COMANDO y la salida estándar PIPE) 
	# La salida estándar será el PIPE
# RECORRE EL POPEN Y LE ENVÍA EL COMANDO
  	# Shell = True es IMPORTANTE
	for line in pipeData.stdout: # Para cada línea de la salida estándar
		conn.send(line) # Envía cada LÍNEA AL CLIENTE
	conn.close() # Cierra la conexión con el CLIENTE.

sys.exit(0) # Sale del PROGRAMA.

"""
	* 23-daytime-server-one2one.py --> Se le pasa ARGUMENTO OPCIONAL --port o por default 50001.
	
		* Se abre una tubería para la SALIDA ESTÁNDAR.
		
		* Se le manda el pipeData para cada línea del .stdout del PIPE.
		
**23-daytime-server-one2one.py**

  Ídem exercici anterior, generar un daytime-server que accepta múltiples clients
  correlatius, és a dir, un un cop finalitzat l'anterior: *One2one*.

 * *One2one*: No té sentint que un servidor atengui un client i finalitzi. Una millora 
   (elemental) és anar atenent els clients un a un. Es connecta un client, se l'atén, es tanca
   la conexió amb aquest client i es passa a escoltar per rebre una nova conexió.
   En aquest cas el server fa un bucle ininit, va atenent clients infinitament un darrera l'altre
   (o si més no s'espera a entendre'ls). És per això que cal governar el servidor, per exemple
   amb senyals.

      * 23-daytime-server-one2one.py
      * 24-calendar-slient-one2one.py / 24-calendar-server-one2one.py

"""
