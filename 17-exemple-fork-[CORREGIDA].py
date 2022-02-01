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


###################### VERIFICACIÓN Y COMPROBACIÓN ##################


# 17.py

# fork

# exec

### Tenemos un programa, proceso Padre, programa Padre,

codi 

codi

codi

	fork()
	
codi

codi

codi

PID = 1345

pare


# FORK() --> Cuando hacemos un FORK, se crea una RÉPLICA EXACTA de un PROCESO. Llamado HIJO.

### La funciÓN FORK() -- En el HIJO retorna 0. En el padre, retorna el número de PID del HIJO que acaba de Generar.

### Duplicar 2 cosas y cada uno es saber QUIÉN ES QUIÉN.

### El apache creaban el mismo, pero tienen diferente PID. Crear PROCESOS y SUBPROCESOS.

----------------------------------------------------

17. PY

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

### Import SYS, OS

### Printa el PID del Padre os.getpid()


pid=os.fork()

### Crea un FORK, se divide en 2 programas. os.fork() --> Retorna 2 procesos, uno el proceso PADRE y el proceso HIJO.

if pid !=0:

### 3342 es diferente ed 0, espera a que termine el HIJO. Los procesos padre pueden terminar. Competencia entre procesos. 

  os.wait()
  
### El valor que retorna FORK es 0 para el HIJO. Si el PID es diferente a 0, es el PADRE. El PID del HIJO, lo recibe del FORK.
  print("Programa Pare", os.getpid(), pid)
else:
  print("Programa fill", os.getpid(), pid)

print("Hasta lugo lucas!")
sys.exit(0)


----------------------------

isx36579183@i11:~/Documents/ipc$ python3 17-exemple-fork.py 
Hola, començament del programa principal
PID pare:  8862

# Simplemente describe el PID del PADRE.

Programa fill 8863 0
Hasta lugo lucas!

# Estas lineas, los escribe el HIJO. Recibe el PID 0.

Programa Pare 8862 8863
Hasta lugo lucas!

# Estas lineas, los escribe el HIJO. El padre es el 8862 y su hijo el 8863.

isx36579183@i11:~/Documents/ipc$ 

--------------------


# El wait espera a que termine.




 

¿Me podrias pasar las grabaciones del Canet de M06 desde que empezamos Pyhthon?



###############################################################

18.FORK-SIGNAL.PY

isx36579183@i11:~/Documents/ipc$ python3 18-fork-signal.py 
Hola, començament del programa principal
PID pare:  9386
Programa Pare 9386 9387
Hasta lugo lucas!
Programa fill 9387 0


## Está haciendo un bucle infinito, está vivo aún el daemon.

## El programa se ha encendido. Se ha reproducido y se ha muerto. Y ha quedado el proceso hijo ejecutandose en backgroup en un DAEMON. En bucle infinito.

## ¿Cómo gestionarlo?

## Recargarse, pararse.

## kill - $(pgrep python)

## /var/run/pid (nombre de fichero y pid) --> Sino no sabe como pararlo, aturarlo, etc.

## Bifurca y genera un demonio, y se queda en el infinito




DEBERES

## El programa 18, pero que este programa sea controlable por 2 SEÑALES. 

	USR 1 / USR 2 que continue o USR 2 que termine. Enviar 2 señales. Señal 1 continue y señal 2 termina. 

## /var/run/pid es donde están todos.


## Matarlo normal

## kill 9708

## pgrep python




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

