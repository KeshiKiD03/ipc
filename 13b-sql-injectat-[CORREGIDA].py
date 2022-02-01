# /usr/bin/pyhton3
#-*-coding: utf-8-*-
#
# 13-sql-injectat.py
#
# usage: python3 13-sql-injectat.py "select * from oficinas"
# ------------------------------------------------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# ------------------------------------------------------------------------------

import sys,argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description=\
        """Consulta a la base de dades entrada per argument al prigrama.""")
parser.add_argument("cons",type=str,\
        help="consulta a la base de dades training")
args=parser.parse_args()

# ------------------------------------------------------------------------------

command = [f"psql -qtA -F',' -h 172.17.0.2 -U postgres training -c \"{args.cons}\""]
pipeData = Popen(command, stdout=PIPE, shell=True)


for line in pipeData.stdout:
    print(line.decode("utf-8")[:-1])

exit(0)

# Lo pone en una variable.



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

