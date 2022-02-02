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
		data = conn.recv(1024)
		print('Receive', repr(data))
		if not data: break # Cuando el otro me ha penjado el teléfono cierra. 
  	
  	pipeData = Popen(data, stdout=PIPE, stderr=PIPE, shell=True) # Hace un Popeen que hace PWD
  		# Iterar linea a linea y muestra el resultado de este POPEN
  	for line in pipeData.stdout: # Recorre cada linea del Popen
        conn.sendall(line) # Envía la línea # Se asegura de vacíar el bufer, envía todo
        if DEBUG: sys.stderr.write(str(line,'utf-8')) # Permite la depuración por si hay envío
       	for line in pipeData.stderr:
        		conn.sendall(line)
        		if DEBUG: sys.stderr.write(str(line,'utf-8'))        
        	conn.sendall(MYEOF)


	conn.close() # Cierra la conexión # Liberar el SOCKET. # El cliente termina la conexión

s.close()
sys.exit(0)

  
  
  	
  # Acepta un CLIENTE
  
  
  # EDITAR EL SERVIDOR Y VERIFICAR
  
