# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-server.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket
from subprocess import Popen, PIPE
# ------------------------------------
HOST = ''   # Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem.
#HOST = 'i23'
PORT = 50001    # Definim port per connectar-nos al servidor (ex 21 (server))
#PORT = 13    # Definim el 'PORT' contra el que volem connectar-nos (13 = DAYTIME)

### --------- PLANTILLA SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Ens permet reutilitzar les IPs

s.bind((HOST,PORT)) # Hace el enlace del HOST y PORT. 

s.listen(1) # Se pone a escuchar.

conn, addr = s.accept() # Implementa el ACCEPT. # Hasta que no acepte la conexión, no hace el accept.
# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).
print("Connected by", addr) # Printem qui s'ha connectat. Mostra IP

#### -------- 

# POPEN

command = ["date"]  # Li especifiquem el command que utiltizarem
pipeData = Popen(command,stdout=PIPE)   # Executem el popen # La salida estándar será el PIPE
# RECORRE EL POPEN Y LE ENVÍA EL COMANDO
for line in pipeData.stdout:    # Retornem les línees
  conn.send(line)   # Enviem la líena
conn.close()    # Tanquem la connexió

sys.exit(0)

"""
# ----------------------------------------------

## Metodología

1. Ataca a un servidor DAYTIME y le contesta al CLIENTE con la FECHA. Se usa POPEN para redirigir y vomitar toda la información en "la salida estándar".


## NOMBRE DEL PROGRAMA + SINTAXIS

 * 22-daytime-client.py / 22-daytime-server.py 


 * *One2one*: No té sentint que un servidor atengui un client i finalitzi. Una millora 
   (elemental) és anar atenent els clients un a un. Es connecta un client, se l'atén, es tanca
   la conexió amb aquest client i es passa a escoltar per rebre una nova conexió.
   En aquest cas el server fa un bucle ininit, va atenent clients infinitament un darrera l'altre
   (o si més no s'espera a entendre'ls). És per això que cal governar el servidor, per exemple
   amb senyals.


"""
