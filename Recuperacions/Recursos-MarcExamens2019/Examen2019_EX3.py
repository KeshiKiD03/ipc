# /usr/bin/python
#-*- coding: utf-8-*-
# prog [-d|--debug] [-p|--port]
#------------------------------
# ASIX M06 Curs 2021-2022 Examen 2019 processos python
# client
# Enunciat:

#---------------------------------

# EXERCICI 3

#---------------------------------
import argparse, sys, socket
from subprocess import Popen, PIPE
# -------------------------------------------------
# Validem els arguments
parser = argparse.ArgumentParser(description='Consulta el calendari ai un servidor')

parser.add_argument("-p", help='Port on realitzar la consulta',type=int,\
     dest="port", required=False, default="51000")

parser.add_argument("-d","--debug",type=str, dest="debug", help="Descrivim tot el que està passant")

args = parser.parse_args()
# -------------------------------------------------
# Crea el SOCKET TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Es connecta al HOST i al PORT, és l'antònim del accept
s.connect(('', args.port))
# -------------------------------------------------

while True:   # Bucle infinit de recepció de dades
  
  dades = s.recv(1024)  # Límit de dades a rebre (llegim el socket)
  if dades[-1:] == b'\x04': # Si rep la senyal de EOT, surt (man ascii -> 004)
    break
  
dades=str(dades)
dades_u = dades.split('\\n') 
#print (list(dades_u)) 
nomFitxer = "/tmp/" + dades_u[0]  # Nombrem el fitxer --> addr[1] : núm port 
fitxer = open(nomFitxer,"w")  # L'obrim
fitxer.write(str(dades_u[2])) # Escribim al fitxer
fitxer.close()    # Tanquem el fitxer
if args.debug:
    print ("Fitxer" & dades_u[0]  & "guardat")
print ("Exit")
s.close()
sys.exit(0)

    