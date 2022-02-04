# /usr/bin/python3

# PROGRAMA QUE HACE LS MEDIANTE UN TUBO SE LE PASA POR PARÁMETRO 

import sys, argparse
from subprocess import Popen, PIPE # Importamos CONSTRUCTORES de la clase SUBPROCESS
parser = argparse.ArgumentParser(description="Exemple Popen",epilog="Adios")

parser.add_argument("ruta", type=str, help="Directorio a listar") # Argumento posicional
#parser.add_argument("-r","--ruta", type=str, help="Directorio a listar") # Argumento opcional
#parser.add_argument("-f","--fit", type=str, help="fitxer a processar", dest="fitxer") # Argumento opcional
args=parser.parse_args() # Apretamos el botón de ARGPARSE
#---------------
command = ["ls", args.ruta] # Definimos una LISTA donde el primer elemento es el comando LS y el segundo, del argumento de ARGPARSE, la variable ruta.
#command = [input("Comando: "), args.ruta, args.fitxer] # Definimos una LISTA donde el primer elemento es el comando LS y el segundo, del argumento de ARGPARSE, la variable ruta.
pipeData = Popen(command, stdout=PIPE) # Definimos el PIPE
for line in pipeData.stdout: # Recorremos la salida estándar de nuestro PIPE. Para cada línea..
    print(line.decode("utf-8"), end="")
exit(0)
