# /usr/bin/python
#-*- coding: utf-8-*-
#
# popen-sql-multi.py
# *nota* no tracta el cas de num_clie inexistent
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
# Utilitza el docker edtasixm06/postgres
# -----------------------------------------
#commandLocal = "psql -qtA -F ';' lab_clinic -c 'select * from pacients;'"
#commandRemote = "psql -qtA -h i11 -U postgres -F ';' training -c "select * from oficinas;"
# -------------------------------------------
import sys
from subprocess import Popen, PIPE
import argparse
#clieList=[]
parser = argparse.ArgumentParser(description='Consulta SQL interactiva')
parser.add_argument("-d","--database", help="base de dades a usar",\
     default="training")
parser.add_argument('-c',"--client", help='client',type=str,\
     action="append",dest="clieList",required="True")
args = parser.parse_args()

cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres "+ args.database
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

for num_clie in args.clieList:
  sqlStatment="select * from clientes where num_clie=%s;" % (num_clie)
  pipeData.stdin.write(sqlStatment+"\n")
  print(pipeData.stdout.readline(), end="")

pipeData.stdin.write("\q\n")
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

## Metodología Y APUNTES

################### VERIFICACIÓN Y SOLUCIÓN ##########################


######################################################################





python3 14-popen-sql-multi.py -c 2111 -c 2111

isx36579183@i11:~/Documents/ipc$ python3 14-popen-sql-multi.py -c 2111 -c 2111
2111,JCP Inc.,103,50000.00
2111,JCP Inc.,103,50000.00
isx36579183@i11:~/Documents/ipc$ 


python3 14-popen-sql-multi.py -c 2111 -c 2111 -c 2102 -c 2103

isx36579183@i11:~/Documents/ipc$ python3 14-popen-sql-multi.py -c 2111 -c 2111 -c 2102 -c 2103
2111,JCP Inc.,103,50000.00
2111,JCP Inc.,103,50000.00
2102,First Corp.,101,65000.00
2103,Acme Mfg.,105,50000.00
isx36579183@i11:~/Documents/ipc$ 


* No es capaz de leer una respuesta, por si le ponemos PERE.

* No se


# Solución 14






######################################################################












######################################################################










######################################################################
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

