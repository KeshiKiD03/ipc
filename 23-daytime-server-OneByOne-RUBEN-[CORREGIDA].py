# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-server-one2one.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse,os,signal
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """Server One by One""")

parser.add_argument("-p","--port", type=int, help="port al qual ens connectem",\
     default=50001, dest="port")

args=parser.parse_args()
# -------------------------------------
HOST = ''
PORT = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

while True:
  conn, addr = s.accept()
  print("Connected by", addr)
  command = ["date"]
  pipeData = Popen(command,stdout=PIPE)
  for line in pipeData.stdout:
    conn.send(line)
  conn.close()
  
  
  
  
"""

## NOMBRE DEL PROGRAMA + SINTAXIS

 * 22-daytime-client.py / 22-daytime-server.py 


 * *One2one*: No té sentint que un servidor atengui un client i finalitzi. Una millora 
   (elemental) és anar atenent els clients un a un. Es connecta un client, se l'atén, es tanca
   la conexió amb aquest client i es passa a escoltar per rebre una nova conexió.
   En aquest cas el server fa un bucle ininit, va atenent clients infinitament un darrera l'altre
   (o si més no s'espera a entendre'ls). És per això que cal governar el servidor, per exemple
   amb senyals.


# ----------------------------------------------

## Metodología

1. nc -l 5001

2. 

3.

4.

5.

6.

7.

8.

9.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

20.
