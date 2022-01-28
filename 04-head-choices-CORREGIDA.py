# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n 5|10|15] file
#  10 lines, file
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys, argparse
parser = argparse.ArgumentParser(description=\
        """Mostrar les N primereslínies """,\
        epilog="thats all folks")
parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies 5|10|15, def 10",\
        dest="nlin", metavar="numLines", \
        default=10,\
        choices=[5,10,15])
parser.add_argument("fitxer",type=str,\
        help="fitxer a processar", metavar="file")
args=parser.parse_args()
print(args)
# -------------------------------------------------------
MAXLIN=args.nlin
fileIn=open(args.fitxer,"r")
counter=0
for line in fileIn:
  counter+=1
  print (line, end='')
  if counter==MAXLIN: break
fileIn.close()
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

