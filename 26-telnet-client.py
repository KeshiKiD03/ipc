# /usr/bin/python3
#-*- coding: utf-8-*-
# telnet-client.py
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse
from subprocess import Popen, PIPE

# ----------------- ARGPARSE

parser = argparse.ArgumentParser(description="""PS Client""")
parser.add_argument("-p","--port",type=int, default=50001)
parser.add_argument("server",type=str) # Se conecta cualquiera
args=parser.parse_args()

# ---------------------------------------

# ------------------ SOCKETS

HOST = args.server
PORT = args.port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abre el SOCKET TCP
s.connect((HOST, PORT)) # Se conecta

# ----- IMPORTANTE FI DE CARACTER

## chr(4) es EOT = End of Transmition

FI = bytes(chr(4), 'utf-8') # Me convierte en BYTES el caracter 4 (EOT), se le asigna a la CONSTANTE FI




# Lo de ARRIBA es una plantilla

# Aquí es donde hacemos todo EL CLIENTE TELNET

while True: # Este bucle infinito, estará esperando a el servidor le conteste.
	command = input("%s> " % HOST) # Establecemos el input, string del comando

	if command == 'exit': break # Si el comando introducido es exit, salimos del programa

	s.send(bytes(command, 'utf-8')) # Envía mediante el socket el comando introducido en modo bytes
	
	while True: # Se realiza otro bucle para recibir y mostrar las líneas. 
	
		data = s.recv(1024) # Recibe las líneas
		if data[-1:] == FI: break # Si la última línea de los datos es el FI, sale del bucle. Hace un slicind. Significa que si el último DATO [-1:] recibido es = FI
		print(data.decode("utf-8")) # Printamos resultados

s.close()  # Tanquem el socket (connexió)
sys.exit(0)

"""
	METODOLOGIA:
	
		1. El CLIENTE se conecta al SERVIDOR de TELNET.
		
		2. El CLIENTE va haciendo comandos y el SERVIDOR le RESPONDE.
		
		3. Si el COMANDO es igual a EXIT, hace un BREAK. O "if not data: break"
		
		4. El CLIENTE envía los datos (El comando) al SOCKET al SERVIDOR.
		
		5. El SERVIDOR recibe los datos (El comando) del CLIENTE
		
		6. Se realiza otro Bucle para escuchar, recibir y mostrar las líneas provenientes del SERVIDOR.
		
		7. Se queda escuchando el SERVIDOR.
		
		8. Si la última línea ed los DATOS recibidos del SERVIDOR es FI, sale del BUCLE. Hace un "slicing". Significa que empieza desde el final, o si la última línea es FI, hace un BREAK.
		
		9. Va mostrando los resultados de los comandos que va haciendo.
		
		10. Cierra la conexión del SCOKEt con el SERVIDOR.
		
		11. Sale del programa.
		
		
	PRUEBAS / SOLUCIÓN:
	
	SÓLO CLIENTE: (USANDO NC)
	
	CLIENTE CON EL SERVIDOR:
	
	keshi@KeshiKiD03:~/Documents/ipc$ python3 26-telnet-client.py --port 50001 localhost
localhost> ls
01-head-[CORREGIDA].py

01-head.py
02-argument-[CORREGIDA].py
02-argument.py

03-head-args-[CORREGIDA].py

03-head-args.py

04b-head-choices-[CORREGIDA].py

04b-head-choices.py

04-head-choices-[CORREGIDA].py

04-head-choices.py




"""


