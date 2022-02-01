# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n 5|10|15] file
#  10 lines, file
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys, argparse # Importa LIBRERIA SYS + ARGPARSE
parser = argparse.ArgumentParser(description=\
        """Mostrar les N primereslínies """,\
        epilog="thats all folks") # Llamamos el ARGUMENT PARSE
parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies 5|10|15, def 10",\
        dest="nlin", metavar="numLines", \
        default=10,\
        choices=[5,10,15]) # Definimos un ARGUMENTO del tipo OPCIONAL. # Usa choices para definir un conunto de valores válidos.
parser.add_argument("-f","--fit","fitxer",type=str,\
        help="fitxer a processar", metavar="file", \
        required=True, dest="fitxer") # Definimos un ARGUMENTO del tipo OPCIONAL. Pero como tiene REQUIRED, pasa a ser OBLIGATORIO.
args=parser.parse_args() # Pulsamos el botón de argparse. Parse_args()
print(args)
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
