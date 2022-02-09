# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-client.py  
# Fem una connexió amb el servidor, i ell quan vegi una connexió ens vomitarà informació.
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket
# -------------------------------------
HOST = 'localhost'  # Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem.
PORT = 50001
#PORT = 13

#### -------- PLANTILLA SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#### -----------------

#### ----- EL CLIENTE SE PONE A ESCUCHAR INFINITAMENTE

while True: # Bucle perquè no sabem quan acabarà ja que no sabem quantes línees ens enviarà
  data = s.recv(1024)   # El client rep la data
  if not data: # s'ha tancat la connexió (SERVER FINALITZA)
      break
  print('Data:', repr(data)) # Printa resultados con b''
s.close() # Cierra la conexión con el CLIENTE.

sys.exit(0)
