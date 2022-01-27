# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-fork.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,os
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  os.wait()
  print("Programa Pare", os.getpid(), pid)
else:
  print("Programa fill", os.getpid(), pid)

print("Hasta lugo lucas!")
sys.exit(0)

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

