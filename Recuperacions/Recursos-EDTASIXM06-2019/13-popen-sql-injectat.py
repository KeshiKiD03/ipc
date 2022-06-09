# /usr/bin/python
#-*- coding: utf-8-*-
#
# popen-sql.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
# Utilitza el docker edtasixm06/postgres
# -----------------------------------------
#commandLocal = "psql -qtA -F ';' lab_clinic -c 'select * from pacients;'"
#commandRemote = "psql -qtA -h i11 -U postgres -F ';' lab_clinic -c 'select * from pacients;'"
# -------------------------------------------
import sys
from subprocess import Popen, PIPE
import argparse
parser = argparse.ArgumentParser(description='Consulta SQL interactiva')
parser.add_argument('sqlStatment', help='Sentència SQL a executar',metavar='sentènciaSQL')
args = parser.parse_args()

cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres  training"
#py2# pipeData = Popen(cmd, shell = True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
pipeData.stdin.write("select * from oficinas;\n\q\n")

for line in pipeData.stdout:
  print(line, end="")
sys.exit(0)


