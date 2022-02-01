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

def myhandler(signum,frame): # Definimos una FUNCIÓN myhandler donde tendremos parámetros el número de señal y el frame.
  print("Signal handler called with signal:", signum)
  print("hasta luego lucas!")
  sys.exit(1)

# Es una función, es un método "myhandler" que recibirá señales --> Recibirá una estructura de datos que representa una señal y hará una serie de Acciones.

# La función después TERMINA --> con sys.exit(1).

# TERMINAMOS .

# Tenemos una FUNCIÓN donde RECIBE SEÑALES y EJECUTA la función.

# Un handler es cuando le pasen algo hace algo especial.    
  
 
def mydeath(signum,frame):
  print("Signal handler called with signal:", signum)
  print("no em dona la gana de morir!")
  
# Función donde MATA el proceso.

signal.signal(signal.SIGALRM,myhandler) # 14
signal.signal(signal.SIGUSR2,myhandler) # 12
signal.signal(signal.SIGUSR1,mydeath)   # 10
signal.signal(signal.SIGTERM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.alarm(60)

# signal.signal permite asociar una FUNCIÓN con una SEÑAL. Cuando el programa reciba la SEÑAL, ejecutará una FUNCIÓN.

# signal. SIG_IGN --> Cuando reciba la señal SIGTERM --> Ignora 

# signal.alarm(60) --> Define que 60 segundos suene una alarma.


print(os.getpid())
while True:
  pass
signal.alarm(0)
sys.exit(0)

# Printa el PID DEL PROGRAMA Y HACE UN BUCLE INFINITO. os.getpid() --> Obtiene el PID del PROCESO

# WHILE TRUE --> Bucle infinito

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


###################### SIGNALS ##########################



# SIGNALS


$ ---> []

* Kill -1s Sigterm

* Kill -9 Sigkill

kill -l --> Obtenemos ...

```
isx36579183@i11:~/Documents/ipc$ kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
63) SIGRTMAX-1	64) SIGRTMAX	
isx36579183@i11:~/Documents/ipc$ 

```

* Nos interesa tener.

1. 1 SIGHUP --> Hace un reinicio del DEMONIO.

	SIGINT --> ES CTRL + C [SIG INTERRUMPIR --> DEJARÁ DE FUNCIONAR]

2. 9 SIGKILL --> Mata un proceso.

3. 10 SIGUSER1 --> Son señales VACÍAS para que se puedan programar el USUARIO.

4. 12 SIGUSER2 --> Definidos por el usaurio.

5. 14 SIGALRM --> Genera una alarma.

6. 15 SIGTERM --> Termina / acaba procesos

7. 18 SIGCONT --> Continua un proceso

8. 19 SIGSTOP --> Para un proceso CTRL + Z


#########################################################


################### EJEMPLOS #############################


sleep 9999999 --> ^C matarlo


sleep 9999999 --> ^Z aturarlo



pgrep sleep --> Obtenemos el PID del SLEEP


kill -2 [pid_sleep] --> Matarlo



kill -19 $(pgrep sleep) --> Para proceso

[1]+  Stopped                 sleep 99999999
isx36579183@i11:~/Documents/ipc$ 


kill -19 $(pgrep sleep) --> Para proceso

jobs


--- Segundo plano

isx36579183@i11:~/Documents/ipc$ jobs
[1]+  Running                 sleep 99999999 &
isx36579183@i11:~/Documents/ipc$ 

---


# apt-get update

# apt-get install apache2

# systemctl start apache2

# systemctl status apache2

# ps ax --> Enciende 3 procesos del C Group

# pstree --> Enciende procesos

# pstree -pl 


----
root@i11:~# pstree -pl 10311
apache2(10311)─┬─apache2(10312)─┬─{apache2}(10318)
               │                ├─{apache2}(10320)
               │                ├─{apache2}(10322)
               │                ├─{apache2}(10324)
               │                ├─{apache2}(10326)
               │                ├─{apache2}(10329)
               │                ├─{apache2}(10331)
               │                ├─{apache2}(10332)
               │                ├─{apache2}(10336)
               │                ├─{apache2}(10338)
               │                ├─{apache2}(10340)
               │                ├─{apache2}(10341)
               │                ├─{apache2}(10342)
               │                ├─{apache2}(10343)
               │                ├─{apache2}(10344)
               │                ├─{apache2}(10349)
               │                ├─{apache2}(10351)
               │                ├─{apache2}(10353)
               │                ├─{apache2}(10355)
               │                ├─{apache2}(10356)
               │                ├─{apache2}(10357)
               │                ├─{apache2}(10358)
               │                ├─{apache2}(10364)
               │                ├─{apache2}(10366)
               │                ├─{apache2}(10367)
               │                └─{apache2}(10368)
               └─apache2(10313)─┬─{apache2}(10317)
                                ├─{apache2}(10319)
                                ├─{apache2}(10321)
                                ├─{apache2}(10323)
                                ├─{apache2}(10325)
                                ├─{apache2}(10327)
                                ├─{apache2}(10328)
                                ├─{apache2}(10330)
                                ├─{apache2}(10333)
                                ├─{apache2}(10334)
                                ├─{apache2}(10335)
                                ├─{apache2}(10337)
                                ├─{apache2}(10339)
                                ├─{apache2}(10345)
                                ├─{apache2}(10346)
                                ├─{apache2}(10347)
                                ├─{apache2}(10348)
                                ├─{apache2}(10350)
                                ├─{apache2}(10352)
                                ├─{apache2}(10354)
                                ├─{apache2}(10359)
                                ├─{apache2}(10360)
                                ├─{apache2}(10361)
                                ├─{apache2}(10362)
                                ├─{apache2}(10363)
                                └─{apache2}(10365)


----

kill -1 10311 [SIGHUP]


#########################################################

#### SHORTCUTS ###


CTRL + Q --> 18

CTRL + S --> 19


#########################################################


VIM 15

https://docs.python.org/3/library/signal.html?highlight=signal#module-signal 

15-exemple-signal.py


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

def myhandler(signum,frame):
  print("Signal handler called with signal:", signum)
  print("hasta luego lucas!")
  sys.exit(1)
  
# Es una función, es un método "myhandler" que recibirá señales --> Recibirá una estructura de datos que representa una señal y hará una serie de Acciones.

# La función después TERMINA --> con sys.exit(1).

# TERMINAMOS .

# Tenemos una FUNCIÓN donde RECIBE SEÑALES y EJECUTA la función.

# Un handler es cuando le pasen algo hace algo especial.  
  


def mydeath(signum,frame):
  print("Signal handler called with signal:", signum)
  print("no em dona la gana de morir!")

# Función donde MATA el proceso.
  
signal.signal(signal.SIGALRM,myhandler) # 14
signal.signal(signal.SIGUSR2,myhandler) # 12
signal.signal(signal.SIGUSR1,mydeath)   # 10
signal.signal(signal.SIGTERM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.alarm(60)

# signal.signal permite asociar una FUNCIÓN con una SEÑAL. Cuando el programa reciba la SEÑAL, ejecutará una FUNCIÓN.

# signal. SIG_IGN --> Cuando reciba la señal SIGTERM --> Ignora 

# signal.alarm(60) --> Define que 60 segundos suene una alarma.

print(os.getpid())
while True:
  pass
signal.alarm(0)
sys.exit(0)

# Printa el PID DEL PROGRAMA Y HACE UN BUCLE INFINITO. os.getpid() --> Obtiene el PID del PROCESO

# WHILE TRUE



#########################################################



################# VERIFICACIÓN Y SOLUCIÓN ###########################





*Si no ejecutas algo en 60 segundos, termina y printa*. Envia la SEÑAL 14. SIGALRM.

kill -15 11469 --> IGNORA

kill -10 11469 --> NO QUIERE MORIRSE

isx36579183@i11:~/Documents/ipc$ python3 15-exemple-signals.py 
11511
Signal handler called with signal: 10
no em dona la gana de morir!


kill -12 11511 --> Termina

isx36579183@i11:~/Documents/ipc$ kill -12 11511
isx36579183@i11:~/Documents/ipc$ 

Signal handler called with signal: 12
hasta luego lucas!
isx36579183@i11:~/Documents/ipc$ 


kill -2 11469 --> IGNORA

CTRL + C --> SE AUTOPROTEGE





#########################################################


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

