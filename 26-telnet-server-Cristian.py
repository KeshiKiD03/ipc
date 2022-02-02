# /usr/bin/python
#-*- coding: utf-8-*-
# telnet-server.py
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """TELNET SERVER""")

parser.add_argument("-p","--port",type=int, default=50001)

args=parser.parse_args()
# -------------------------------------


HOST = ''   # Definim com a HOST (localhost)
PORT = args.port    # Definim el PORT que l'agafarà per l'argument (parser)
FI = bytes(chr(4), 'utf-8')

# ---------------------------------------

# ---------- Saber el proceso ---------- 

pid=os.fork() # Hace un duplicado, lo creaba y se ejecutaba.


if pid != 0:    # Fem l'if en funció el PID al pare.
  print("Engegat el server CAL:", pid)
  sys.exit(0)   # Apaga el proceso padre, mientras que el hijo seguía encendido.

# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!

# --- Todo lo de abajo es el proceso hijo ----

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)


# Lo de arriba es una plantilla

# Aquí es donde se hace TODO

while True: # Bucle infinit # Bucle infinit (atendre connexions un darrera l'altre)
  conn, addr = s.accept() # Guardem les variables conn i addr
  print("Connected by", addr) #  Printem
  while True:
  llistaPeers.append(addr) # Lo añade a una LISTA
  fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%S"))
  fileLog=open(fileName,"w")
  while True:
  	data = conn.recv(1024)
  	if not data: break # Cuando el otro me ha penjado el teléfono cierra
  	fileLog.write(str(data))
  conn.close() # Cierra la conexión # Liberar el SOCKET.
  fileLog.close() # Cierra
  
  
  	
	pipeData = Popen(command, shell=True, stdout=PIPE) # Popen (shell=True --> es perquè funcioni) # El Popen para enviarle la ORDEN al SERVIDOR, mediante el SOCKET
	
	for line in pipeData.stdout: # Recorremos cada línea del stdout (pipeData)
    		s.send(line) # Lo envia en el servidor
  # Acepta un CLIENTE
  
  
  # EDITAR EL SERVIDOR Y VERIFICAR
  
