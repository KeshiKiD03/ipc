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
command = " psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c \"select * from clientes; \""
pipeData = Popen(command,shell=True,stdout=PIPE)
for line in pipeData.stdout:
  print(line.decode("utf-8"), end="")
exit(0)

# Resumen
# 1. Se importan las librerías correspondientes.
# 2. En una variable se importa un "string" que en este caso es una sentencia para conectarse a la BD.
# 3. En stdin entrará el "command", shell=True es importante y la salida estándar saldrá por el PIPE por un tubo.
# 4. Se recorre la salida estándar y printa cada línea.
#
#
#

