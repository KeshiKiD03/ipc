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
HOST = ''
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1) # Escolta
conn, addr = s.accept() # Accepta la connexió
print("Connected by", addr) # Rep la connexió
command = ["date"]  # Li especifiquem el command que utiltizarem
pipeData = Popen(command,stdout=PIPE)   # Executem el popen

for line in pipeData.stdout:    # Retornem les línees
  conn.send(line)   # Enviem la líena
conn.close()    # Tanquem la connexió

sys.exit(0)

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







"""

