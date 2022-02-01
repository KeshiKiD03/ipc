# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket,argparse
parser = argparse.ArgumentParser(description="""CAL server""")
parser.add_argument("-s","--server",type=str, default='')
parser.add_argument("-p","--port",type=int, default=50001)
args=parser.parse_args()
HOST = args.server
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
  data = s.recv(1024)
  if not data: break
  print('Data:', str(data))
s.close()
sys.exit(0)



"""

## NOMBRE DEL PROGRAMA + SINTAXIS

24 CLIENTE

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
