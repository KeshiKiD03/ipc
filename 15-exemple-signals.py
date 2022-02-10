# /usr/bin/python3
#-*- coding: utf-8-*-
#
# signal-exemple.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, os, signal
def myhandler(signum,frame):
  print("Signal handler called with signal:", signum)
  print("hasta luego lucas!")
  sys.exit(1)
def mydeath(signum,frame):
  print("Signal handler called with signal:", signum)
  print("no em dona la gana de morir!")
signal.signal(signal.SIGALRM,myhandler) # 14 # Recibe una alarma.
signal.signal(signal.SIGUSR2,myhandler) # 12 RECIBE EL 12
signal.signal(signal.SIGUSR1,mydeath)   # 10 RECIBE EL 10
signal.signal(signal.SIGTERM,signal.SIG_IGN) # Si recibe un TERMINATED SIGTERM (15) lo IGNORA con SIG_IGN.
signal.signal(signal.SIGINT,signal.SIG_IGN) # Si recibe un CTRL + C SIGINT (2) lo IGNORA con SIG_IGN.
signal.alarm(60) # En 60 segundos suena una alarma
print(os.getpid()) # Obtiene el PID
while True: # Hay un bucle infinito
  pass # PASA
signal.alarm(0) # El 0 vuelve a estar 0
sys.exit(0)
