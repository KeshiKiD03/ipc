# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [-n 5|10|15] [-f file]...
#  10 lines, file... 
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys, argparse # Importamos los módulos sys y argparse
fileList=[] # Establecemos una LISTA VACÍA, fileList
parser = argparse.ArgumentParser(description=\
        """Mostrar les N primereslínies """,\
        epilog="thats all folks") # Llamamos el ARGUMENT PARSE
parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies 5|10|15, def 10",\
        dest="nlin",\
        metavar="numLines",default=10,\
        choices=[5,10,15]) # Definimos un ARGUMENTO del tipo OPCIONAL. Del tipo Integer. # Usa choices para definir un conunto de valores válidos. Por defecto es 10, pero podemos escoger de 5, 10 o 15
parser.add_argument("-f", "--file",type=str,\
        help="fitxer a processar", metavar="file",\
        dest="fileList", nargs="*") # Definimos un ARGUMENTO del tipo OPCIONAL. Del tipo STRING. 
        # Metavar es el alias. 
        # Dest es el nombre de la VARIABLE. 
        # Action es el comando a realizar, en este caso APPEND. Añade al final.
        # Usa NARGS para rellenar con *
parser.add_argument("-v", "--verbose",action="store_true",default=False)
args=parser.parse_args()
print(args)
# -------------------------------------------------------
MAXLIN=args.nlin # Establecemos una CONSTANTE MAXLIN que analizará el número de líneas.

def headFile(fitxer): # Definimos una FUNCIÓN para acordar NUESTRO CÓDIGO. Dentro de la función le pasamos como PARÁMETRO FITXER.
  fileIn=open(fitxer,"r") # Abrimos el fichero en modo READ.
  counter=0 # Establecemos el contador
  for line in fileIn: # Recorremos fileIn
    counter+=1 # Incrementamos el contador
    print(line, end='') # Para cada línea me printas el valor de linea y un salto de línea
    if counter==MAXLIN: break # Si el contador es igual al número de argumentos haces un BREAK.
  fileIn.close() # Cerramos el fichero.

if args.fileList: # Si la lista fileList
  for fileName in args.fileList: # Para cada fileName en la lista fileList
    if args.verbose: print("\n",fileName, 40*"-") # Si hay -v / Booleano, muestra una cabecera con el nombre del fichero a listas. 
    headFile(fileName) # Llamamos la función headFile y mostramos el fileName.

exit(0)

