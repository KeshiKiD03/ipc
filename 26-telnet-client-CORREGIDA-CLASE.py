# /usr/bin/python3
#-*- coding: utf-8-*-
# telnet-client.py # ONE 2 ONE
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
FI = bytes(chr(4), 'utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abre el SOCKET TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.connect((HOST, PORT)) # Se conecta con el server


# Lo de arriba es una plantilla

# Aquí es donde hacemos todo EL CLIENTE TELNET

while True: # Este bucle infinito, estará esperando a el servidor le conteste.
	command = input("%s> " % HOST) # Establecemos el input, string del comando

	if command == 'exit': break # Si el comando introducido es exit, salimos del programa

	s.send(bytes(command, 'utf-8')) # Envía mediante el socket el comando introducido en modo bytes
	
	while True: # Se realiza otro bucle para recibir y mostrar las líneas. 
	
		data = s.recv(1024) # Recibe las líneas
		if data[-1:] == FI: 
			print('Received', repr(data[:-1])) # Muestra todo menos el último
			break # Si la última línea de los datos sea el FI, sale del bucle
		print('Received', repr(data))

s.close()  # Tanquem el socket (connexió)
sys.exit(0)


