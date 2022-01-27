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



"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**18-fork-signal.py**

  Usant el programa d'exemple fork fer que el procés fill (un while infinit) es
  governi amb senyals. Amb siguser1 mostra "hola radiola" i amb sigusr2 mostra
  "adeu andreu" i finalitza. El programa pare genera el procés fill i finalitza.

# ----------------------------------------------

## Explicación

**18-fork-signal.py**

  Usant el programa d'exemple fork fer que el procés fill (un while infinit) es
  governi amb senyals. Amb siguser1 mostra "hola radiola" i amb sigusr2 mostra
  "adeu andreu" i finalitza. El programa pare genera el procés fill i finalitza.


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

