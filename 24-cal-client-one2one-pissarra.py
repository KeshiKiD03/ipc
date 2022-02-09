# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket,argparse # Importar ARGPARSE
parser = argparse.ArgumentParser(description="""CAL client""")
parser.add_argument("-s","--server",type=str, default='') # Se conecta cualquiera
parser.add_argument("-p","--port",type=int, default=50001)
args=parser.parse_args()
HOST = args.server
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # Se conecta
while True:
  data = s.recv(1024) # Receptor
  if not data: break
  print('Data:', str(data))
s.close()
sys.exit(0)

"""
**24-calendar-client-one2one.py [-s server] [-p port]**

**24-calendar-server-one2one.py [-p port] [-a any]**

  Calendar server amb un popen, el client es connecta i rep el calendari. El server 
  tanca la connexió amb el client un cop contestat però continua escoltant noves connexions.

  El server ha de governar-se amb senyals que fan:
   - sigusr1: llista de peers i plega.
   - sigusr2: count de listpeer i plega.
   - sigterm: llista de peers, count i plega.

  El server és un daemon que es queda en execució després de fer un fork del seu
  pare (que mor) i es governa amb senyals.

  Que sigui el servidor qui rep l'any com a argument és una tonteria, seria més lògic
  fer-ho en el client, però el diàleg client servidor queda per a una pràctica
  posterior. Aquí es vol practicar usar un arg en el popen.
  
  
### SOLUCIÓN


"""
