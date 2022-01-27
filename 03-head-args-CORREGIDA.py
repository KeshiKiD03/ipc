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
import sys, argparse
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

**01-head.py [file]**
  
  Mostrar les deu primeres línies de file o stdin

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

