#/usr/bin/python3
#
# Python documentation:
# argparse tutorial: 

import argparse

"""
  * Importamos la librería "argparse"
"""

parser=argparse.ArgumentParser(description=\
  "programa exemple de processar arguments",prog="02-arguments.py",epilog="hasta luegu lucas!")

"""
  * 
"""


parser.add_argument("-e","--edat", type=int, dest="useredat", help="edat a processar", metavar="edat")

"""
  * 
"""


parser.add_argument("-f","--fit", type=str, help="fitxer a processar", dest="fitxer")

"""
  * 
"""

parser.add_argument("-n","--nom", type=str, help="nom de usuari")

"""
  * 
"""


parser.add_argument("fit", type=str, help="fitxer")

"""
  * 
"""

args=parser.parse_args()
#print(parser)
print(args)

"""
  * 
"""


print(args.useredat, args.nom)

"""
  * 
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

Mostrar les 10 primeres línies d'un fitxer. 
El nom del fitxer a mostrar es rep com a argument, sinó es rep, 

es mostren les deu primeres línies de  l'entrada estàndard. 

Sinpsys: $ head [file] 

# ----------------------------------------------

## Metodología

1. 

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

