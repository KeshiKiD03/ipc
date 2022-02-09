# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-echoClient.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket
#--------------------------------------
HOST = 'localhost'   # Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem.
#HOST = 'i23'
#PORT = 50001    # Definim port per connectar-nos al servidor (ex 21 (server))
PORT = 7    # Definim el 'PORT' contra el que volem connectar-nos (7 = echo)

#### -------- PLANTILLA SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Ens permet reutilitzar les IPs

s.connect((HOST, PORT)) # Ens connectem, es quedarà enganxat fins que es pugui connectar # Es important


#### -------- 

s.send(b'Hello, world') # Enviem el missatge 'Hello, world' (b --> dades binàries)

data = s.recv(1024) # Rep el missatge i contestarà. # Està "hardcoded", rebrà un tamany fix de 1024
s.close()   # Tanquem la connexió.

print('Received', data.decode("utf-8"))   # Printem el que hem rebut
sys.exit(0) # Sortim
