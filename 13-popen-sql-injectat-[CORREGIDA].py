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

# SOLUCIÓN
"""
  1. Se importa SYS y desde subproceso, Popen y PIPE.
  2. Se importa también argparse.
  3. Se inicializa el ARGPARSE con una descripción.
  4. Se añade un argumento que será una sentencia SQL, será posicional.
  5. La entrada estándar, salida estándar y salida de error será PIPE.
  6. En la entrada estándar, hacemos un WRITE hacemos una sentencia SQL. --> \n --> Salto de línea y \q es ENTER y \n salto de línea.
  7. Se recorre con un for la salida estándar de cada línea y se printa.
"""


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**13-popen-sql-injectat.py  consulta**

  Fer que la sentència sql a fer sigui un argument tot entre cometes 
  que es passa com a argument.
  sql injectat: perills d’injectar codi d’usuari en els programes.

# ----------------------------------------------

## Explicación

**13-popen-sql-injectat.py  consulta**

  Fer que la sentència sql a fer sigui un argument tot entre cometes 
  que es passa com a argument.
  sql injectat: perills d’injectar codi d’usuari en els programes.


# ----------------------------------------------




"""

