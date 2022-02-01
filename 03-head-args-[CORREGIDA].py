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

"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**03-head-args.py [-n nlin] [-f filein]**

  Mostar les n primeres línies (o 10)  de filein (o stdin).

  Definir els dos paràmetres opcionals i les variables on
  desar-los. Usar un str default de “/dev/stdin” com a nom 
  de fitxer per defecte, simplifica el codi, tenim sempre
  un string.

# ----------------------------------------------

## USAGE

# $ head.py -n 2 -f file.txt
# $ head.py < file.txt
# $ head.py -n 3
# $ head.py -f file.txt
# tots els altres casos d'error

# ----------------------------------------------

## Metodología y APUNTES

1. # Si no le pasamos n lineas, procesa 10, si le pasamos datos procesa entrada estandar.

2. args=parser.parse_args() --> Es cuando se procesan los argumentos

3. # MAXLIN=args.nlin --> Lo que me hayan pasado o por default 10

4. # fileIN --> Se abre lo que le hayan pasado o se abre /dev/stdin.

5.

6.



ARGPARSE

    name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.

    action - The basic type of action to be taken when this argument is encountered at the command line.

    nargs - The number of command-line arguments that should be consumed.

    const - A constant value required by some action and nargs selections.

    default - The value produced if the argument is absent from the command line and if it is absent from the namespace object.

    type - The type to which the command-line argument should be converted.

    choices - A container of the allowable values for the argument.

    required - Whether or not the command-line option may be omitted (optionals only).

    help - A brief description of what the argument does.

    metavar - A name for the argument in usage messages.

    dest - The name of the attribute to be added to the object returned by parse_args(). 
7.

8.

9.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

20.







"""

