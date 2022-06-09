# /usr/bin/python3
#-*- coding: utf-8-*-
#
# signal.py  segons
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,os, signal, argparse
parser = argparse.ArgumentParser(description="Gestionar l'alarma")
parser.add_argument("segons", type=int, help="segons")
args=parser.parse_args()
global upp
global down
upp = 0
down = 0

def mysigusr1(signum,frame):
  global upp
  print("Signal handler called with signal:", signum)
  upp+=1
  actual=signal.alarm(0)
  signal.alarm(actual+60)

def mysigusr2(signum,frame):
  global down
  print("Signal handler called with signal:", signum)
  down+=1
  actual=signal.alarm(0)
  if actual-60<0: 
    print("ignored %d" % (actual))
    signal.alarm(actual)
  else:
    signal.alarm(actual-60)

def mysighup(signum,frame):
  print("Signal handler called with signal:", signum)
  print("Restoring value: ", args.segons)
  signal.alarm(args.segons)

def mysigterm(signum,frame):
  print("Signal handler called with signal:", signum)
  falta=signal.alarm(0)
  signal.alarm(falta)
  print("Falten actualment %d segons" % (falta))
 
def mysigalarm(signum,frame):
  global upp, down
  print("Signal handler called with signal:", signum)
  print("Finalitzant.... upp:%d  down:%d" % (upp, down))
  sys.exit(1)

signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGHUP,mysighup)
signal.signal(signal.SIGTERM,mysigterm)
signal.signal(signal.SIGALRM,mysigalarm)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.alarm(args.segons)
print(os.getpid())

while True:
  pass
signal.alarm(0)
sys.exit(0)

