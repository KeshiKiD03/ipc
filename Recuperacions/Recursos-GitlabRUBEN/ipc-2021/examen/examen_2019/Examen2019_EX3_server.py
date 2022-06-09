# /usr/bin/python
#-*- coding: utf-8-*-
#
# 26-telnetServer.py [-p port] [-d debug]
#
#accepta la connexió
#while True:
#   recv * (s'hauria de fer un bucle recv)
#   Popen 
#   for line in Popen.stdout:
#       read (Popen)
#       send Popen
#   send (chr4) --> ascii 004
#   tanquem connexió
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# Genera un diàleg amb el client, on aquest l'indica una consulta a 
# realitzar i el servidor li retorna el resultat, quan el client envia un Enter
# el servidor tanca la connexió. El servidor escoltant a altres clients.
# Implementar un servidor i un client telnet. Client i server fan un diàleg.
# Cal un senyal de “yatà” Usem chr(4).
# Si s’indica debug el server generarà per stdout la traça de cada connexió.
# -------------------------------------
import sys, socket, os, argparse
from subprocess import Popen, PIPE
# -----------------------
# Validem els arguments
parser = argparse.ArgumentParser(description='Guarda ps ax a un fitxer')

parser.add_argument("-p", type=int, help="Port on escoltar",\
    default=51000, dest="port")

parser.add_argument("-d","--debug",action='store_true',default=False)

args = parser.parse_args()
# -----------------------
# Per totes les IP del meu host
HOST = ''
# Connexió tipus TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Reutilitza l'adreça encara que estigui bloquejada per alguna acció anterior
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Lliga la IP del meu host i el port
s.bind((HOST,args.port))
# Indica que s'ha de posar a escoltar, però continua
s.listen(1)
# -------------------------------------------------
MYEOT = bytes(chr(4), 'utf-8')
while True:
# Es posa a escoltar fins que es produeixi una connexió
  conn, addr = s.accept()
  command = "cat %s" %("entrada.txt")
  pipeData = Popen(command,shell=True, stdout=PIPE)
  for line in pipeData.stdout:
    conn.send(line)
  conn.send(MYEOT)