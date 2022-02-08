#!/usr/bin/python
#-*- coding: utf-8-*-
'''
# -----------------------------------------------------------------
# Escola del treball de Barcelona
# ASIX Hisi2 M06-ASO UF2NF1-Scripts
# @edt Curs 2021-2022
# Gener 2022
# Telnet server multiple-connexions
# -----------------------------------------------------------------
'''
import socket, sys, select, os # Importamos liberías
from subprocess import Popen, PIPE
HOST = '' # Declaramos el host
PORT = 50006 # Usamos el puerto 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abrir el SOCKET
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reutiliza SOCKET
s.bind((HOST, PORT)) # s.bind --> Enlaza el socket a la dirección con HOST y PUERTO
s.listen(1) # Se mantiene escuchando

FI = bytes(chr(4), 'utf-8')

# ---------- Saber el proceso ----------

print(os.getpid()) # Coge el PID del PROCESO

# pid=os.fork()

#if pid != 0:    # Fem l'if en funció el PID al pare.
#  print("Engegat el server CAL:", pid)
#  sys.exit(0) 

conns=[s] # Almacena en la lista los que están ACTIVOS (Los que levantan el brazo), de momento está escuchando.
while True:
    actius,x,y = select.select(conns,[],[])
    for actual in actius:
        if actual == s:
            conn, addr = s.accept()
            print('Connected by', addr)
            conns.append(conn)
        else:
            while True:
                conn, addr = s.accept()
                print('Connected by', addr)
                while True:
                    command = conn.recv(1024) # Recibe data
#                    if args.debug: # Args.debug = DebugImprime en el servidor el resultado
#                        print ("Telnet> %s" % (command)) # Imprime el comando
                    if not command: break # Cuando el otro me ha penjado el teléfono cierra.
                    pipeData = Popen(command, shell=True, stdout=PIPE, stderr=PIPE) # Hace un Popeen que hace PWD 
				    # Iterar linea a linea y muestra el resultado de este POPEN
                    for line in pipeData.stdout: # Recorre cada linea del Popen # Pipe de SALIDA
#                       if args.debug:
#                           print(line) # Printa cada línea.
                        conn.send(line) # Envía la línea # Se asegura de vacíar el bufer, envía todo.
                    for line in pipeData.stderr:# Pipe de ERROR
#                       if args.debug:
#                           print("Error: %s" % line)
                        conn.send(line) # Envía la línea    
                    conn.send(FI)
#conn.close() # Cierra la conexión # Liberar el SOCKET. # El cliente termina la conexión
s.close()
sys.exit(0)
