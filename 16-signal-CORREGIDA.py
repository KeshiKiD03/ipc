# /usr/bin/python3
#-*- coding: utf-8-*-
#
# signal-exemple.py
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, os, signal

# LIBRERIAS DE PYTHON 

# ---------------------------------------

parser = argparse.ArgumentParser(description="Gestionar l'alarma")
parser.add_argument("segons", type=int, help="segons")
args=parser.parse_args()
global upp
global down
upp = 0
down = 0

# ------------------------------------------------------


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

#   
  
  
  
  
  
# Es una función, es un método "myhandler" que recibirá señales --> Recibirá una estructura de datos que representa una señal y hará una serie de Acciones.

# La función después TERMINA --> con sys.exit(1).

# TERMINAMOS .

# Tenemos una FUNCIÓN donde RECIBE SEÑALES y EJECUTA la función.

# Un handler es cuando le pasen algo hace algo especial.  
  

# Función donde MATA el proceso.
  
signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGHUP,mysighup)
signal.signal(signal.SIGTERM,mysigterm)
signal.signal(signal.SIGALRM,mysigalarm)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.alarm(args.segons)
print(os.getpid())


#





# signal.signal permite asociar una FUNCIÓN con una SEÑAL. Cuando el programa reciba la SEÑAL, ejecutará una FUNCIÓN.

# signal. SIG_IGN --> Cuando reciba la señal SIGTERM --> Ignora 

# signal.alarm(60) --> Define que 60 segundos suene una alarma.

while True:
  pass
signal.alarm(0)
sys.exit(0)

#


# Printa el PID DEL PROGRAMA Y HACE UN BUCLE INFINITO. os.getpid() --> Obtiene el PID del PROCESO

# WHILE TRUE

----------------

# Una función es un template, se le pasa una señal y una "caja" = "función" que tenemos predefinida arriba.
