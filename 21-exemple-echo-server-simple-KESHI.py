# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-echo-server-KESHI.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket
#--------------------------------------
HOST = ''   # Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem.
#HOST = 'i23'
PORT = 50001    # Definim port per connectar-nos al servidor (ex 21 (server))
#PORT = 7    # Definim el 'PORT' contra el que volem connectar-nos (7 = echo)

#### -------- PLANTILLA SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Ens permet reutilitzar les IPs

s.bind((HOST,PORT)) # Hace el enlace del HOST y PORT. 

s.listen(1) # Se pone a escuchar.

conn, addr = s.accept() # Implementa el ACCEPT. # Hasta que no acepte la conexión, no hace el accept.
# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).
print("Connected by", addr) # Printem qui s'ha connectat. Mostra IP

#### -----------------

while True: # Bucle infinito que se pondrá a escuchar datos, SI HUBIERA MÁS DE 1
    data = conn.recv(1024) # El client envia les dades, el servidor rep el missatge i contestarà. 
    # Esta hardcoded, rebrà un tamany fix de 1024
    if not data: # Si no hi han més dades a rebre, tanca la sessió, fa un BREAK (EL SERVIDOR FINALITZA!)
        break
    conn.send(data) # Retorna les dades
conn.close()   # Tanquem la connexió (CLIENT!).

print('Received', data.decode("utf-8"))   # Printem el que hem rebut
sys.exit(0) # Sortim
