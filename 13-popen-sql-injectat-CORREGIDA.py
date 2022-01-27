# /usr/bin/python
#-*- coding: utf-8-*-
#
# popen-sql.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
from subprocess import Popen, PIPE
# -------------------------------------------------------


command = "psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c \"select * from clientes; \""
pipeData = Popen(command,shell=True,stdout=PIPE)
for line in pipeData.stdout:
  print(line.decode("utf-8"), end="")
exit(0)

# SOLUCIÓN



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

