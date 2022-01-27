#/usr/bin/python3
#
# Python documentation:
# https://docs.python.org/3/library/argparse.html 

# ¡¡¡ https://ellibrodepython.com/python-argparse !!! LEERSE
# argparse tutorial: 

import argparse

"""
  * Importamos la librería "argparse"
"""

parser=argparse.ArgumentParser(description=\
  "programa exemple de processar arguments",prog="02-arguments.py",epilog="hasta luegu lucas!")

"""
  * A la variable parser, CREA UN OBJETO DEL TIPO ARGPARSE.
  
  * Es como si crease una caja que tiene BOTONES.
  
  * Se le pasan parámetros dentro ()
  
  * El gestor de argumentos, tendrá una DESCRIPCIÓN, un PROGRAMA y un EPÍLOGO.
"""


parser.add_argument("-e","--edat", type=int, dest="useredat", help="edat a processar", metavar="edat")

"""
  * Se añaden argumentos del tipo INTEGER para la EDAD. *Parámetro opcional
"""


parser.add_argument("-f","--fit", type=str, help="fitxer a processar", dest="fitxer")

"""
  * Se añaden argumentos del tipo STRING para el FICHERO. *Parámetro opcional
"""

parser.add_argument("-n","--nom", type=str, help="nom de usuari")

"""
  * Se añaden argumentos del tipo STRING. *Parámetro opcional
"""


# parser.add_argument("fit", type=str, help="fitxer")

"""
  * Se añaden argumentos del tipo STRING. *Parámetro posicional. Tiene "nombre" y no = -n -e .. ES OBLIGATORIO
"""

args=parser.parse_args()
#print(parser)
print(args)

"""
  * Apreta el botón, analiza todos los argumentos según el parser y se añade ().

  * parse_args() --> Analiza los argumentos --> Según toda la construcción de la caja que hemos hecho y lo añade a la variable args.
"""

#print(args.fitxer, args.useredat)
print(args.useredat, args.nom)

"""
	# Hacer prints para ver las cosas

	# Ver el objeto parser, args, args.fitxer, args.userdat

"""


exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**02-exemple-args.py**

  Exemple fet interactivament per mostrar el funcionament
  de argparser. Pyton documentation 15.4.

 *Argparser (Python documentation 14.5 / argparse tutorial):*
   
   * creació objecte. afegir arguments.

   * paràmetres posicionals i opcionals.

   * help, description, epíleg, prog, metavar.

   * destination, type.

   * fer el parse. diccionari de resultats.

   * fitxers de tipus file (inconvenients) o str.

   * validació automàtica i missatges d’error. Independència de l’ordre dels 
     arguments opcionals (no dels posicionals).

   * validació automàtica del tipus dels arguments.

   * Els *paràmetres posicionals* es defineixen per ordre i simplement amb el
      “nom”. Els *opcionals* poden anar en qualsevol ordre i cal definir “-n” i “--nom”.

# ----------------------------------------------

## Explicación

¿Que es ARGPARSE?

El módulo argparse facilita la escritura de interfaces de línea de comandos amigables. El programa define qué argumentos requiere, y argparse averiguará cómo analizar los de sys. argv .

# ----------------------------------------------

## Apuntes

*  FITXER --> Es el nom que queda gravat per defecte. Es el METAVAR.

* OPTIONAL ARGUMENTS 

* POSITIONAL ARGUMENTS

Els *paràmetres posicionals* es defineixen per ordre i simplement amb el
      “nom”. Els *opcionals* poden anar en qualsevol ordre i cal definir “-n” i “--nom”.


PROG -e -m conte.txt treball.pdf

   ------  --------------
optional arg       positional

Positional parameter --> El orden por el cual lo pones




# si no hay -- es positional

isx36579183@i11:~/Documents/ipc$ python3 02-argument.py -e 12
usage: 02-arguments.py [-h] [-e edat] [-f FITXER] [-n NOM] fit
02-arguments.py: error: the following arguments are required: fit
isx36579183@i11:~/Documents/ipc$ 














# ----------------------------------------------

## Metodología y pruebas

1. python3 02-argument.py -h --> Pide el HELP



usage: 02-arguments.py [-h] [-e edat] [-f FITXER] [-n NOM] fit

programa exemple de processar arguments

positional arguments:
  fit                   fitxer

optional arguments:
  -h, --help            show this help message and exit
  -e edat, --edat edat  edat a processar
  -f FITXER, --fit FITXER
                        fitxer a processar
  -n NOM, --nom NOM     nom de usuari

hasta luegu lucas!




2. python3 02-argument.py -e 14 -f file.txt

Namespace(fitxer='file.txt', nom='None', useredat=44)
44 None




3. python3 02-argument.py -e 15 -f file.txt -e 44 -n keshi --> # Lee la del final

Namespace(fitxer='prueba.txt', nom='keshi', useredat=44)
44 keshi


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

