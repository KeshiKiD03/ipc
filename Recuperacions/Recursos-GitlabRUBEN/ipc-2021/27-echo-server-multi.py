#!/usr/bin/python
#-*- coding: utf-8-*-
# -----------------------------------------------------------------
# Escola del treball de Barcelona
# ASIX HISX2 M06-ASO UF2 NF1-Scripts
# @edt Curs 2021-2022
# Gener 2022
# Echo server multiple-connexions
# -----------------------------------------------------------------
import socket, sys, select, os
# -----------------------------------------------------------------
HOST = ''                 
PORT = 50001             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(os.getpid())
conns=[s]   # socket que escolta
# -----------------------------------------------------------------
while True:
    actius,x,y = select.select(conns,[],[])     # select.select = itera sobre 3 arguments (wait until ready for reading, wait until ready for writing, 
#                                               wait for an "exceptional condition"), ens retorna una triple llista dels subconjunts que hi havia al principi. 
#                                               --> conns (read) i la segona i tercera no li passem res (en aquest cas) --> 
#                                               fins ara l'unic "actius" és la 's', sempre que és connecti algú nou, 'actius' = 's'
    for actual in actius:
        if actual == s: # si l'actual es la 's'... (és una connexió nova?)
            conn, addr = s.accept() # Quan és connectin, passem de la 's' a 'conn'
            print('Connected by', addr)
            conns.append(conn)  # Afegim la connexió a la 'llista' de connexions pendents.
        else:   # si ja coneixiem la connexió... (atenem la connexió ja coneguda)
            data = actual.recv(1024)
            if not data:
                sys.stdout.write("Client finalitzat: %s \n" % (actual))
                actual.close()
                conns.remove(actual)    # Si el client tanca la connexió (l'ovlidem)
            else:   # Podem posar el que volem per escollir com actuarà el server
                actual.sendall(data)
                #actual.sendall(chr(4),socket.MSG_DONTWAIT)
s.close()

sys.exit(0)
