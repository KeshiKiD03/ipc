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
        epilog="thats all folks")
parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies",dest="nlin",\
        metavar="numLines",default=10)
parser.add_argument("-f","--fit",type=str,\
        help="fitxer a processar", metavar="file",\
        default="/dev/stdin",dest="fitxer")
args=parser.parse_args()
print(args)
# -------------------------------------------------------
MAXLIN=args.nlin
fileIn=open(args.fitxer,"r")
counter=0
for line in fileIn:
  counter+=1
  print(line, end='')
  if counter==MAXLIN: break
fileIn.close()
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

## Metodología

1. # Si no le pasamos n lineas, procesa 10, si le pasamos datos procesa entrada estandar.

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

