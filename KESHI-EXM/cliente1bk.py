# /usr/bin/python3
# -------------------------------------
import sys,socket,argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""Examen practica""")
parser.add_argument("-s",type=str, dest="server")
parser.add_argument("-p",type=int,  dest="port")
args=parser.parse_args()

if args.server and args.port:
	
	HOST = args.server
	PORT = args.port

else:
	print(" selieccionar host e ip")
	consola = input("client_ftp_trivial>")
	if 'connect' in consola:
		
		HOST = consola.split()[1].split(':')[1]
		PORT = consola.split()[1].split(':')[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:

    entrada = input("client_ftp_trivial>")
    
    if entrada == 'quit':

        s.close()
        
        break



    if 'get' in entrada:
        
        fitxero = open(entrada.split()[1].split('/')[-1],'a')

        entrada = "cat " + entrada.split()[1] 

    rata = entrada

    entrada = entrada.encode()
    s.send(entrada)

    while True:
    
        data = s.recv(1024)
        
        print(data.decode("utf-8"))
        
        if 'cat' in rata:

            fitxero.write(str(data))
            
            
        else:

            print (data.decode("utf-8"))

        if data[-1:] == b'\x04':

            break

    
    
## USAGE 

## 1. python3 servidor.py 50001

## 1. python3 cliente.py localhot 50001

## ls

## get


sys.exit(0)


"""
A continuación se encuentran algunos de los comandos de FTP más comunes que podemos utilizar:

    help o ? – Enumerar todos los comandos de FTP disponibles.
    cd – Cambia el directorio en la máquina remota.
    lcd – Cambiar el directorio en la máquina local.
    ls – Ver los nombres de los archivos y directorios en el directorio remoto actual.
    mkdir – Crea un nuevo directorio dentro del directorio remoto.
    pwd – Imprime el directorio de trabajo actual en la máquina remota.
    delete – Elimina un archivo en el directorio remoto actual.
    rmdir- Elimina un directorio en el directorio remoto actual.
    get – Copia un archivo del servidor remoto a la máquina local.
    mget – Permite copiar múltiples archivos del servidor remoto a la máquina local.
    put – Copia un archivo de la máquina local a la máquina remota.
    mput – Copia un archivo de la máquina local a la máquina remota.

"""
