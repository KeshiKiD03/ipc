# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-fork.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,os, signal
def mysigusr1(signum,frame):
  global upp
  print("Signal handler called with signal:", signum)
  print("Hola radiola")

def mysigusr2(signum,frame):
  print("Signal handler called with signal:", signum)
  print("Adeu andreu!")
  sys.exit(0)
    
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  print("Programa Pare", os.getpid(), pid)
  print("Hasta lugo lucas!")
  sys.exit(0)
  
print("Programa fill", os.getpid(), pid)
signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
while True:
  pass


