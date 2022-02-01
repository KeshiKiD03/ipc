# /usr/bin/python3
#-*- coding: utf-8-*-
# cal-client-one2oned-pissarra.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description="""PS Client""")
parser.add_argument("-p","--port",type=int, default=50001)
parser.add_argument("server",type=str) # Se conecta cualquiera
args=parser.parse_args()

# ---------------------------------------
HOST = args.server
PORT = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abre el SOCKET TCP
s.connect((HOST, PORT)) # Se conecta

# Lo de arriba es una plantilla

# Aquí es donde hacemos todo EL CLIENTE

while True:
	command = input("%s> " % HOST) # Establecemos el input, string del comando

	if command == 'exit': break # Si el comando introducido es exit, salimos del programa
	
	pipeData = Popen(command, shell=True, stdout=PIPE) # Popen (shell=True --> es perquè funcioni) # El Popen para enviarle la ORDEN al SERVIDOR, mediante el SOCKET
	
	for line in pipeData.stdout: # Recorremos cada línea del stdout (pipeData)
    		s.send(line) # Lo envia en el servidor

	while True:
		data = s.recv(1024) # Lo recoge del Socket
		if str(data) == 'yata': break
		print(str(data))

s.close()  # Tanquem el socket (connexió)
sys.exit(0)


