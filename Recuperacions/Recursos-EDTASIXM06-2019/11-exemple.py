# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-popen.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description=\
        """Exemple popen""")
parser.add_argument("ruta",type=str,\
        help="directori a llistar")
args=parser.parse_args()
# -------------------------------------------------------
command = ["ls", args.ruta]
pipeData = Popen(command, stdout=PIPE)
for line in pipeData.stdout:
    print(line.decode("utf-8"), end=" ")
exit(0)






