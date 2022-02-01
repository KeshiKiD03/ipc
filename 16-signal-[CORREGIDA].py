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

## Metodología Y APUNTES


############################################################################



#16-SIGNAL.PY 16


* PASADOS N SEGUNDOS --> TERMINAR CON SIGALRM.

* SIGUSER1 --> +1 MINUT --> HARÁ QUE LA ALARMA SERÁ 1 MINUTO MÁS (+ 60 SEGUNDOS).

* SIGUSER2 --> -1 MINUTO --> HARÁ QUE LA ALARMA SERÁ -1 MINUTO MÁS (- 60 SEGUNDOS).

* SI RECIBE SIGHUP -> REINICIAR EL CONTADOR --> PONE EL VALOR ORIGINAL DEL CONTADOR.

* SIGTERM --> MOSTRAR CUANTOS SEGUNDOS FALTAN.

	* LOS CUENTA EL SISTEMA.
	
---
	
* El programa no permite que se haga CTRL + C.

* SIGALARM --> Número de UP y DOWN y ACABA.



HELP -- TENER CONTADORES PARA CADA UNO



############################################################################





######################## ANALISIS ####################################




### Es una variable GLOBAL (upp) - VARIABLE GLOBAL.

### No se puede modificar la estructura por parámetro, no se le pueden pasar más argumentos.

### Signum = SEÑAL, frame = CAJA tipo Signal.

### upp = Variable GLOBAL.

### Scope 

### Incrementa la cantidad de DOWN y le resta 60 el valor de alarma.

### Siempre y cuando que la actual se resta -60<0.

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
  
### Reinicia el servicio, reinicia la alarma.

### args.segons = Es una variable GLOBAL.

### 

### 

### 

def mysigterm(signum,frame):
  print("Signal handler called with signal:", signum)
  falta=signal.alarm(0)
  signal.alarm(falta)
  print("Falten actualment %d segons" % (falta))
  
### Indicar cuanto falta. Obtiene el valor de la alarma. Y lo tiene que volver a poner.



    


def mysigalarm(signum,frame):
  global upp, down
  print("Signal handler called with signal:", signum)
  print("Finalitzant.... upp:%d  down:%d" % (upp, down))
  sys.exit(1)
  
### Cuando le pasemos un SIGALARM, el programa devuelve cuanto ha devuelto.

### Muestra información.

### 

### 

### 

signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGHUP,mysighup)
signal.signal(signal.SIGTERM,mysigterm)
signal.signal(signal.SIGALRM,mysigalarm)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.alarm(args.segons)
print(os.getpid())

### Llamar la función.

### signal.signal(signal.SIGINT,signal.SIG_IGN) = CTRL + C se Ignora.

while True:
  pass
signal.alarm(0)
sys.exit(0)



######################## VERIFICACIÓN Y SOLUCIÓN ########################


kill -10 $(pgrep python)


isx36579183@i11:~/Documents/ipc$ python3 16-signal.py 60
8589
^CSignal handler called with signal: 10




kill -15 $(pgrep python)

isx36579183@i11:~/Documents/ipc$ python3 16-signal.py 60
8589
^CSignal handler called with signal: 10
Signal handler called with signal: 10
Signal handler called with signal: 15
Falten actualment 107 segons

kill -12 $(pgrep python)




kill -10 

# aumente suma 60 segundos

kill -12 

# restart

kill -15

# Muestra cuanto tiene ahora



----

<pre>Finalitzant.... upp:0  down:1
<font color="#859900"><b>isx36579183@i11</b></font>:<font color="#268BD2"><b>~/Documents/ipc</b></font>$ </pre>
----




Finalitzant.... upp:2  down:1



Signal handler called with signal: 12
ignored 52



<pre>Finalitzant.... upp:0  down:1
<font color="#859900"><b>isx36579183@i11</b></font>:<font color="#268BD2"><b>~/Documents/ipc</b></font>$ </pre>




<pre>Finalitzant.... upp:0  down:1
<font color="#859900"><b>isx36579183@i11</b></font>:<font color="#268BD2"><b>~/Documents/ipc</b></font>$ </pre>




kill -14 termina.


---
isx36579183@i11:~/Documents/ipc$ python3 16-signal.py 60
8643
Signal handler called with signal: 10
Signal handler called with signal: 12
Signal handler called with signal: 15
Falten actualment 19 segons
Signal handler called with signal: 14
Finalitzant.... upp:1  down:1
isx36579183@i11:~/Documents/ipc$ 


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

