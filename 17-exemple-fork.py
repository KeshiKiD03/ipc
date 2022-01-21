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
