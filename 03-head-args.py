# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n nlin] [-f file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
# $ head.py -n 2 -f file.txt
# $ head.py < file.txt
# $ head.py -n 3
# $ head.py -f file.txt
# tots els altres casos d'error
# -------------------------------------
import sys, argparse # Importa LIBRERIA SYS + ARGPARSE
parser = argparse.ArgumentParser(description=\
        """Mostrar les N primereslínies """,\
        epilog="thats all folks") # Llamamos el ARGUMENT PARSE
parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies",dest="nlin",\
        metavar="numLines",default=10) # Definimos un ARGUMENTO del tipo OPCIONAL
parser.add_argument("-f","--fit",type=str,\
        help="fitxer a processar", metavar="file",\
        default="/dev/stdin",dest="fitxer") # Definimos un ARGUMENTO del tipo OPCIONAL
args=parser.parse_args() # Inicializamos el parse_args() --> Botón de encendido
print(args) # Printamos
# -------------------------------------------------------
MAXLIN=args.nlin # Establecemos una CONSTANTE para el número de líneas. Add_argument --> "nlin"
fileIn=open(args.fitxer,"r") # Abrimos el fichero en modo read. Add_argument --> "fitxer"
counter=0 # Establecemos un contador a 0
for line in fileIn: # Recorremos para cada línea del fileIn.
  counter+=1 # Incrementamos el contador
  print(line, end='') # Para cada línea, al final le añadimos un espacio en blanco
  if counter==MAXLIN: break # Si el contador llega al MAXLIN, hacemos un BREAK. 
fileIn.close() # Cerramos el fichero
exit(0)
