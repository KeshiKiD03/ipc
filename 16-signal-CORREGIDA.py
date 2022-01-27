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



"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**01-head.py [file]**
  
  Mostrar les deu primeres línies de file o stdin

# ----------------------------------------------

## Explicación

Signals:
EXS: kill - $(pgrep )
kill - 
jobs --> per veure el jobs actius
pgrep  Per veure el seu PID (Proccess ID)
pstree -pl  (p --> process, l --> + info)
CTRL + Q --> Atura el procés en execució (EX: tree /)
CTRL + S --> Continua el procés aturat (EX: tree /)


Senyals: (Per mirar aquests: kill -l)
1 - SIGHUP (Senyal que reinicia el procés)
2 - SIGINT (Senyal que plega el programa --> equivalent a CTRL + C)
9 - SIGKILL (Senyal que mata el procés)
10 - SIGUSR1 (Senyal sense funció assignada, està així perquè l'usuari el defineixi)
12 - SIGUSR2 (Senyals sense funció assignada, està així perquè l'usuari el defineixi)
14 - SIGALRM (Senyal que envia una alarma)
15 - SIGTERM (Senyal que li demana al programa que plegui)
18 - SIGCONT (Senyal que li demana al procés que continuï --> equivalent a CTRL + Q)
19 - SIGSTOP (Senyal que para el procés --> equivalent a CTRL + S / CTRL + Z)


# ----------------------------------------------

## Metodología

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

