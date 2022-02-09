# /usr/bin/python
#-*- coding: utf-8-*-
#
# 3-daytime-client-args.py  
# Fem una connexió amb el servidor, i ell quan vegi una connexió ens vomitarà informació.
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
# /usr/bin/python3
#-*- coding: utf-8-*-
# 23-daytime-client-args.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse

## ARGPARSE

parser = argparse.ArgumentParser(description="""Client """) # Iniciar ARGPARSE (Analizador de Argumentos)
parser.add_argument("-s","--server",type=str, default='') # Optional parameter type String, default SERVER = localhost
parser.add_argument("-p","--port",type=int, default=50001) # Optional parameter type Integer, default PORT = 50001
args=parser.parse_args() # Apretar el botón de ARGPARSE.

## SOCKET + ARGPARSE

HOST = args.server # Indicamos que en la variable posicional de "args", me seleccionas .server = localhost
PORT = args.port # Indicamos que en la variable posicional de "args", me seleccionas .port = 50001 (Port defecto) o indicar.

# Sockets

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
s.connect((HOST, PORT)) # Se conecta al SERVIDOR (IP DESTINO + PORT DESTINO)


## Daytime client ARGS

while True: # Bucle infinito # Bucle perquè no sabem quan acabarà ja que no sabem quantes línees ens enviarà
  data = s.recv(1024) # Estará recibiendo datos provenientes del servidor.
  if not data: break # S'ha tancat la connexió (SERVER FINALITZA)
  print('Data:', str(data)) # Representa los datos obtenidos del Servidor,
s.close() # Cierra la conexión con el SERVIDOR.
sys.exit(0)

"""
SOLUCIÓN: Se añaden argumentos al programa PYTHON con ARGPARSE. Se establece una conexión con el SERVIDOR y cuando vea que haya una conexión, vomitará información.

1. Se importan librerías de sys, socket y argparse.

2. Se inicializa el ARGPARSE cliente.

3. Se añaden argumentos del "opcional" y del tipo "string" = --server e "integer" = --port

4. El puerto por defecto es 50001 del SERVIDOR. 

5. Se pulsa el botón de ARGPARSE.

6. Se definen las CONSTANTES HOST y PORT de forma "DINÁMICA" con el ARGPARSE.

7. Se hace un bucle infinito para estar ESCUCHANDO INFORMACIÓN.

8. Cuando ya no tiene más datos a recibir de parte del SERVIDOR. Éste hace un BREAK. Finaliza el SERVIDOR.

9. Cierra la conexión con el SERVIDOR. (El cliente).



APUNTES:

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
