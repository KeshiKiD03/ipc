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
        default=10,\ # Default 10
        choices=[5,10,15]) # Definimos un ARGUMENTO del tipo OPCIONAL. # Usa choices para definir un conunto de valores válidos.
parser.add_argument("fitxer",type=str,\
        help="fitxer a processar", metavar="file") # Definimos un ARGUMENTO del tipo POSICIONAL. Pasa a ser OBLIGATORIO.
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

"""

## NOMBRE DEL PROGRAMA + SINTAXIS


**04-head-choices.py [-n 5|10|15]   -f filein**

  Mostar les n primeres 5 o 10 o 15 (def 10)  de filein.
  Usar choices de argparse per definir un conjunt de valors vàlids.

# ----------------------------------------------

## Explicación


**04-head-choices.py [-n 5|10|15]   -f filein**

  Mostar les n primeres 5 o 10 o 15 (def 10)  de filein.
  Usar choices de argparse per definir un conjunt de valors vàlids.


# ----------------------------------------------

## Metodología

1. 


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

2.

3.

4.

5.

6.

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

