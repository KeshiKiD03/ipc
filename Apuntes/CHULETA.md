-----------
-- PLANTILLA --
-----------

<!---
# Plantilla H1
## Plantilla H2
### Plantilla H3
-->
<!--- <img src="https://phoneky.co.uk/thumbs/screensavers/down/original/linux_3rj131p8.gif" />
-->

⭐️ **PLANTILLA** ⭐️

| 🔥PLANTILLA TALBA❗🔥 | 
| ------------- |
| *Plantilla* |


--------------------------------------------------------------------------------

### ARGPARSE

ARGPARSE = Analizador de Argumentos.

import sys, **argparse**

**parser** = argparse.**ArgumentParser**(description="""CAL server""",epilog="Adios")

parser.add_argument(**"-s"**,**"--sort"**,**type**=str,metavar="criteria",choices=["gid,"gname,"nusers"], **help**="Ordenar",dest=crtieria") --> **OPCIONAL**, con **CHOICES**, VAR(Criteria), solo 1 de ello + help --help

parser.add_argument("userFile",type=str,\
        help="user file (/etc/passwd style)", metavar="userFile") --> **Definir fitxer**, es **POSICIONAL**

parser.add_argument("fit", type=str, help="fitxer") --> **POSICIONAL**, string fitxer.

args=parser.parse_args() --> Pulsa

**OPCIONES ARGPARSE**

"-s", "--sort" o "sort" **OPCIONAL O POSICIONAL**.
help="text", metavar="alias", dest="variable", choices=["1","2"], default="valorDefecto" required="True/False" (Posicional a Obligatorio), action="store_true" (Guarda bool) o "append"(Hace un Append), nargs="*" (Rellena)

---- **Llamada**

args.criteria()

args.fitxer

### POPEN (PIPE)

PIPE = Une 2 Dispositivos. Abre una tuberia, puede ser en modo r o w.

0 -> Entrada Estandar

1 -> Salida Estándar

2 -> Salida Error

isx36579183@i11:/tmp/m01$ ls -l /proc/10113/fd
total 0
lrwx------ 1 isx36579183 hisx2 64 Jan 18 10:42 0 -> /dev/pts/1
l-wx------ 1 isx36579183 hisx2 64 Jan 18 10:42 1 -> /tmp/m01/nom.txt
lrwx------ 1 isx36579183 hisx2 64 Jan 18 10:42 2 -> /dev/pts/1


* La salida estandar, no está en la terminal --> /dev/pts/1 (Es la terminal)

* La SALIDA de orden CAT, la envía al flujo 1 (Entrada estándar), pero el SISTEMA OPERATIVO ha redirigido que todo lo que vaya al 1, en realidad está asociada al fichero /tmp/m01/nom.txt (Fichero)

/dev/pts/1 --> Es la consola



##### CON LA ORDEN mkfifo /tmp/dades --> CREAMOS PIPES

prw-rw-r-- .. /tmp/dades

tail -f /tmp/dades --> Sale todo al tubo.


date > /tmp/dades

keshi@KeshiKiD03:~/Documents$ tail -f /tmp/dades
vie 04 feb 2022 00:01:06 CET
vie 04 feb 2022 00:45:48 CET



##### CON ESTO OBTENEMOS UN "named pipe"

##### /proc es una habitación donde se almacenan los procesos.

##### fd --> fileDescriptor. cmdline --> Lista de ordenes | environ --> Variables de entorno | stat --> estados


### COMUNICACIÓN BIDIRECCIONAL pipeData = Popen(command,stdin=PIPE, shell=True,stdout=PIPE)


### 11.py

from subprocess import Popen, PIPE

command = ["ls", args.ruta]

pipeData = Popen(command, shell=True, stdout=PIPE) --> Crea un TUBO y CMD lo pasa al PIPE de salida estandar.

for line in pipeData.stdout:
        print(line.decode("utf-8"), end="") 



### 12.py

* Se le pasa una consulta SQL en la salida estándar a stdout=PIPE.

* Printa resultado, en el stdout del SQL en el programa de Python.


### 14.py

#### pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

* Es una comunicación BIDIRECCIONAL.

for num_clie in args.clieList:
  sqlStatment="select * from clientes where num_clie=%s;" % (num_clie)
  pipeData.stdin.write(sqlStatment+"\n")
  print(pipeData.stdout.readline(), end="")

pipeData.stdin.write("\q\n")

1. En la entrada estandar --> pipeData.stdin --> Hacemos un .write(sqlStatment)

2. En la salida estandar --> pipeData.stoud --> Hacemos un readline()

### SIGNALS

kill -l (Vemos la lista de SEÑALES)

SIGKILL - 9 (KILL PROCESS)
SIGTERM - 15 (TERMINATE)
SIGUSR1 - 10 (MYHANDLER)
SIGUSR2 - 12 (MYHANDLER)
SIGALRM - 14 (ALARM)
SIGINT - 2 (CTRL + C)
SIGHUP - 1 (REBOOT)
SIGCONT - 18 (CTRL + Q) (CONTINUE)
SIGSTOP - 19 (CTRL + Z)

ps ax | top o jobs

pstree -pl (Process, l + info)

pgrep (Ver proceso activo)

CTRL Z --> CTRL Q

## os --> Librería de signals

os.execv()
os.command()

## myhandler() -> Es una función que recibirá un signal.SIGNAL (Recibirá una estructura de datos (OBJETO) que representa una SEÑAL) y hará una serie de acciones.


## La función después termina. 

## Sys.exit(0) – Los programas si quieres no terminas. 


## Un handler, es “cuando haga una cosa, hará esto”. Cuando reciba una señal, hará algo determinado.

## Mydeath() → Es una función que cuando reciba una señal → Se ejecuta y  muere

## signal.signal → Asocia una función o señal. Cuando recibas la señal 1, canta Keshi .. etc




(OPCIONAL)

### 16.py

Pasados N segundos, terminar con SIGALARM (Enviar una alarma).

SIGUSR1 (10) + 1 MINUTO (+60 SEGUNDOS) ----  SIGUSR2 (12) – 1 MINUTO (-60 SEGUNDOS)

SI RECIBE LA SEÑAL SIGHUP → Reiniciar el CONTADOR Con los que habíamos recibido anteriormente.

Si recibe un SIGTERM → Mostrar cuantos segundos faltan. Los cuenta el SISTEMA OPERATIVO.

El programa no permite que se haga control + C (signal.signal(signal.SIGINT,signal.SIG_IGN)) # Ignora el CONTROL C

Sigalarm → Muestra el número de UP y DOWN y acaba. 

Cuantas veces ha subido 1 minuto o ha bajado 1 minuto.



### FORK()

# FORK() --> Cuando hacemos un FORK, se crea una RÉPLICA EXACTA de un PROCESO. Llamado HIJO.

### La funciÓN FORK() -- En el HIJO retorna 0. En el padre, retorna el número de PID del HIJO que acaba de Generar.

### Duplicar 2 cosas y cada uno es saber QUIÉN ES QUIÉN.

### El apache creaban el mismo, pero tienen diferente PID. Crear PROCESOS y SUBPROCESOS.


* pgrep python

17.py


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







##### 18.py



**18-fork-signal.py**

  Usant el programa d'exemple fork fer que el procés fill (un while infinit) es
  governi amb senyals. Amb siguser1 mostra "hola radiola" i amb sigusr2 mostra
  "adeu andreu" i finalitza. El programa pare genera el procés fill i finalitza.


# El wait espera a que termine.






### EXECV()


### 19.py

import sys,os
# ------------------------------------------------
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  print("Programa Pare", os.getpid(), pid)
  sys.exit(0)

#-------------------------------------------------
print("Programa fill", os.getpid(), pid)

# os.execv("/usr/bin/ls",["/usr/bin/ls","-ls","/"])  # 'v' ACCEPTA llistes i tuples

# os.execl("/usr/bin/ls","/usr/bin/ls","-ls","/") # 'l' NO ACCEPTA llistes i tuples, només li podem passar paràmetres fixes.

# os.execlp("ls","ls","-ls","/") # 'l' hem de passar-li els arguments literals, 'p' buscarà ell el PATH fins l'executable (no ens cal posar-li la ruta absoluta (/usr/bin/ls))

# os.execvp("uname",["uname", "-a"])  # Amb 'p' buscarà l'executable 'uname' i executarà l'ordre '-a'

# os.execv("/bin/bash",["/bin/bash", "show.sh"]) # executem el programa 'show.sh'

# os.execle("/bin/bash", "/bin/bash", "show.sh", {"nom":"joan", "edat":"25"})  # 'e' li passem variables d'entorn (com a diccionari)






#-------------------------------------------------
print("Hasta lugo lucas!")   # Mai és veurà!!!!!
sys.exit(0)



  Ídem anterior però ara el programa fill execula un “ls -la /”. Executa un nou 
  procés carregat amb execv. Aprofitar per veure les diferents variants de *exec*.
  Provar cada un dels casos.


### EXECV() --> V es la versión.

* Execv ejecuta el proceso y nunca ejecuta el último, se autosustituye.

* Lanza un subproceso con un programa que nosotros queramos.

* Execv --> El programa que le queremos pasar en formato STRING y una LISTA y un elemento [0] --> Nombre del programa



* os.execv("/usr/bin/ls",["/usr/bin/ls","-ls","/"])  

# 'v' ACCEPTA llistes i tuples

* os.execl("/usr/bin/ls","/usr/bin/ls","-ls","/") 

# 'l' NO ACCEPTA llistes i tuples, només li podem passar paràmetres fixes.

* os.execlp("ls","ls","-ls","/") 

# 'l' hem de passar-li els arguments literals, 'p' buscarà ell el PATH fins l'executable (no ens cal posar-li la ruta absoluta (/usr/bin/ls))

* os.execvp("uname",["uname", "-a"])  

# Amb 'p' buscarà l'executable 'uname' i executarà l'ordre '-a'

* os.execv("/bin/bash",["/bin/bash", "show.sh"]) 

# executem el programa 'show.sh'

* os.execle("/bin/bash", "/bin/bash", "show.sh", {"nom":"joan", "edat":"25"})   

# 'e' li passem variables d'entorn (com a diccionari)

----


### SOCKETS

### CLIENT

#####################################################################

#### 21-ECHO-CLIENT-SIMPLE.py (CLIENTE)

imprt sys,socket

## Importar libreria 

HOST = 'localhost' - DONDE ATACAR
PORT = 7 - DONDE ATACAR

## Donde atacar

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

## Inicializa el CONSTRUCTOR SOCKET

s.connect((HOST, PORT)) 

# Se conecta al SERVIDOR y se queda ENGANCHADO HASTA QUE SE CONECTE Y EL SERVIDOR ACEPTE.

s.send(b'Hello Horld') 

## Está Hardcoded, lo normal es con un while True:.

data = s.recv(1024)

## Recibe el mensaje, está HARDCODED.

print("Received", data.decode("utf-8")) # Printa lo que hemos recibido.

sys.exit(0) 

# Sale



#####################################################################




#### 22-DAYTIME-SIMPLE.py (CLIENTE)

HOST = 'localhost'  

# Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem. # Se define una constante al HOST a la que atacar
PORT = 50001 

# Se define una constante al PUERTO a atacar. Del SERVIDOR

#PORT = 13 

# Ataca DIRECTAMENTE al servidor XINETD de DAYTIME. Nmap localhost 13 daytime

#### -------- PLANTILLA SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Se crea el constructor del SOCKET

s.connect((HOST, PORT)) 

# Se conecta al HOST y PUERTO

#### -----------------

#### ----- EL CLIENTE SE PONE A ESCUCHAR INFINITAMENTE

while True: 

# Bucle que permite escuchar Infinitamente, porque no sabemos cuantas líneas enviará. # Bucle perquè no sabem quan acabarà ja que no sabem quantes línees ens enviarà


  data = s.recv(1024)   
  
  # El client rep la data del servidor. # Rep el missatge i contestarà. 
# Està hardcoded, rebra un tamany fix de 1024


  if not data: 
  
  # s'ha tancat la connexió (SERVER FINALITZA!!!!)
      break
  print('Data:', repr(data)) 
  
  # Printa resultados con b''
s.close() 

# Cierra la conexión con el CLIENTE.

sys.exit(0)


#####################################################################



## 23-DAYTIME-CLIENT-ARGS.PY  

import sys,socket,argparse

## --------------- ARGPARSE

parser = argparse.ArgumentParser(description="""Client """) 

# Iniciar ARGPARSE (Analizador de Argumentos)
parser.add_argument("-s","--server",type=str, default='') 

# Optional parameter type String, default SERVER = localhost
parser.add_argument("-p","--port",type=int, default=50001) 

# Optional parameter type Integer, default PORT = 50001
args=parser.parse_args() 

# Apretar el botón de ARGPARSE.

## ----------------- SOCKET + ARGPARSE

HOST = args.server 

# Indicamos que en la variable posicional de "args", me seleccionas .server = localhost
PORT = args.port 

# Indicamos que en la variable posicional de "args", me seleccionas .port = 50001 (Port defecto) o indicar.

# -------------- Sockets

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.

s.connect((HOST, PORT)) 

# Se conecta al SERVIDOR (IP DESTINO + PORT DESTINO)


##  ----------Daytime client ARGS

while True: 
# Bucle infinito # Bucle perquè no sabem quan acabarà ja que no sabem quantes línees ens enviarà

  data = s.recv(1024) 
  
  # Estará recibiendo datos provenientes del servidor.
  
  if not data: break 
  
  # S'ha tancat la connexió (SERVER FINALITZA)
  
  print('Data:', str(data)) 
  
  # Representa los datos obtenidos del Servidor,
s.close() 

# Cierra la conexión con el SERVIDOR.
sys.exit(0)




### SOLUCIÓN

SOLUCIÓN: Se añaden argumentos al programa PYTHON con ARGPARSE. Se establece una conexión con el SERVIDOR y cuando vea que haya una conexión, vomitará información.

1. Se importan librerías de sys, socket y argparse.

2. Se inicializa el ARGPARSE cliente.

3. Se añaden argumentos del "opcional" y del tipo "string" = --server e "integer" = --port

4. El puerto por defecto es 50001 del SERVIDOR. 

5. Se pulsa el botón de ARGPARSE.

6. Se definen las CONSTANTES HOST y PORT de forma "DINÁMICA" con el ARGPARSE.

7. Se hace un bucle infinito para estar ESCUCHANDO INFORMACIÓN.

8. Cuando ya no tiene más datos a recibir de parte del SERVIDOR. Éste hace un BREAK. Finaliza el SERVIDOR.

9. Cierra la conexión con el SERVIDOR. (El cliente).




#####################################################################



import sys,socket,argparse # Importar ARGPARSE

# ARGPARSE

parser = argparse.ArgumentParser(description="""CAL client""") # Se inicializa el ARGPARSE
parser.add_argument("-s","--server",type=str, default='',dest="server") # Se conecta cualquiera. Si no se especifica el SERVIDOR, se conecta a cualquiera a LOCALHOST.
parser.add_argument("-p","--port",type=int, default=50001,dest="port") # El puerto a atacar es 50001
args=parser.parse_args() # Se pulsa el ARGPARSE

# SOCKETS

HOST = args.server # Se definen constantes para indicar a que HOST nos conectaremos, dest=server (Variable del ARGPARSE)
PORT = args.port # Se definen constantes para indicar a que PORT nos conectaremos, dest=port (Variable del ARGPARSE)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Se inicializa el SOCKET para conectarse
s.connect((HOST, PORT)) # Se conecta al SERVIDOR
while True: # Bucle infinit # Para que esté escuchando por si le envían más de 1 línea.
  data = s.recv(1024) # Recibe datos del SERVIDOR.
  if not data: break
  print('Data:', data.decode("utf-8")) # Se printa en modo UTF 8 con DECODE data.decode("utf-8")
s.close()
sys.exit(0)

"""
**24-calendar-client-one2one.py [-s server] [-p port]**

**24-calendar-server-one2one.py [-p port] [-a any]**

  Calendar server amb un popen, el client es connecta i rep el calendari. El server 
  tanca la connexió amb el client un cop contestat però continua escoltant noves connexions.

  El server ha de governar-se amb senyals que fan:
   - sigusr1: llista de peers i plega.
   - sigusr2: count de listpeer i plega.
   - sigterm: llista de peers, count i plega.

  El server és un daemon que es queda en execució després de fer un fork del seu
  pare (que mor) i es governa amb senyals.

  Que sigui el servidor qui rep l'any com a argument és una tonteria, seria més lògic
  fer-ho en el client, però el diàleg client servidor queda per a una pràctica
  posterior. Aquí es vol practicar usar un arg en el popen.
  
  
### SOLUCIÓN

# CLIENTE

	1. Se conecta a ATACAR al SERVIDOR que quiere. Y el PUERTO también.
	
	2. Se conecta al SOCKET destino, mediante HOST y PORT y se queda ESCUCHANDO.
	
	3. Cuando ya no tenga más datos a RECIBIR. Hace un BREAK. Finaliza y muestra la información en DESCODIFICACIÓN DE BINARIO A UTF8

# SERVIDOR

	1. Se abre el SERVIDOR en DETACH, el CLIENTE se conecta. 
	
	2. El servidor CALENDAR, le vomita la información.
	
	3. El CLIENTE finaliza.
	
	4. El SERVIDOR escucha al siguiente y lo añade a una LISTA VACÍA mediante APPEND.
	
	5. Le envíamos con un KILL -15 $(pgrep python).
	
	6. El SERVIDOR responde:
	
	ubuntu@keshi:~/Documents/ipc$ kill -15 $(pgrep python)
ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52574), ('127.0.0.1', 52576)] 2

	7. Significa que ha recibido la SEÑAL 15 que es SIGTERM --> Si ha recibido esa señal, termina el programa Y MOSTRARÁ QUIÉN SE HA CONECTADO + LA LONGITUD de USUARIOS CONECTADOS 
	
	
	---
	
	
## KILL y PRUEBAs

1. Se enciende el SERVIDOR en DETACH.

2. El cliente se conecta (s.connect((HOST,PORT)))y hace PETICIONES, se queda ESCUCHANDO y RECIBIENDO MENSAJES Infinitamente. Hasta que no tenga nada más que recibir.

3. El cliente finaliza y se conecta otro desde otro puerto dinámico de ORIGEN.

4. El servidor va registrando quién entra IP y PORT y CUENTA cuantos usuarios HAN ENTRADO (Lista vacía llistaPeers.append(addr, lo printa con un len print(llistaPeers, len(llistaPeers)) )
	
5. Desde otra CONSOLA le enviamos: (Se han CONECTADO 3 CLIENTES 1by1, de uno en uno)

	kill -10 $(pgrep python) --> SIGUSR1 (Print de CONEXIONES ACTIVAS)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 10
[('127.0.0.1', 52582), ('127.0.0.1', 52584)]
Connected by ('127.0.0.1', 52586)

	
	kill -12 $(pgrep python) --> SIGUSR2 (Print de CUANTOS SE HAN CONECTADO (LEN(lista)))

	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 12
3


	kill -15 $(pgrep python) --> SIGTERM 15 (TERMINA EL PROGRAMA)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52582), ('127.0.0.1', 52584), ('127.0.0.1', 52586)] 3

	
	
IMPORTANTE EL SYS.EXIT(0) LO HEMOS QUITADO UN MOMENTO DEL CLIENTE

#  sys.exit(0) # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos



















#####################################################################


## 24-CAL-CLIENT-ONE2ONE.PY (CLIENTE)

import sys,socket,argparse 

# Importar ARGPARSE

# ARGPARSE

parser = argparse.ArgumentParser(description="""CAL client""") 

# Se inicializa el ARGPARSE

parser.add_argument("-s","--server",type=str, default='',dest="server") 

# Se conecta cualquiera. Si no se especifica el SERVIDOR, se conecta a cualquiera a LOCALHOST.

parser.add_argument("-p","--port",type=int, default=50001,dest="port") 

# El puerto a atacar es 50001

args=parser.parse_args() 

# Se pulsa el ARGPARSE

# SOCKETS

HOST = args.server 

# Se definen constantes para indicar a que HOST nos conectaremos, dest=server (Variable del ARGPARSE)

PORT = args.port 

# Se definen constantes para indicar a que PORT nos conectaremos, dest=port (Variable del ARGPARSE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Se inicializa el SOCKET para conectarse

s.connect((HOST, PORT)) 

# Se conecta al SERVIDOR

while True: # Bucle infinit 

# Para que esté escuchando por si le envían más de 1 línea.

  data = s.recv(1024) 
  
  # Recibe datos del SERVIDOR.

  if not data: break
  
  print('Data:', data.decode("utf-8")) 
  
  # Se printa en modo UTF 8 con DECODE data.decode("utf-8")

s.close() 

# Se cierra la conexión con el SERVIDOR
sys.exit(0)



### METODOLOGIA

**24-calendar-client-one2one.py [-s server] [-p port]**

**24-calendar-server-one2one.py [-p port] [-a any]**

  Calendar server amb un popen, el client es connecta i rep el calendari. El server 
  tanca la connexió amb el client un cop contestat però continua escoltant noves connexions.

  El server ha de governar-se amb senyals que fan:
   - sigusr1: llista de peers i plega.
   - sigusr2: count de listpeer i plega.
   - sigterm: llista de peers, count i plega.

  El server és un daemon que es queda en execució després de fer un fork del seu
  pare (que mor) i es governa amb senyals.

  Que sigui el servidor qui rep l'any com a argument és una tonteria, seria més lògic
  fer-ho en el client, però el diàleg client servidor queda per a una pràctica
  posterior. Aquí es vol practicar usar un arg en el popen.
  
  
### SOLUCIÓN

# CLIENTE

	1. Se conecta a ATACAR al SERVIDOR que quiere. Y el PUERTO también.
	
	2. Se conecta al SOCKET destino, mediante HOST y PORT y se queda ESCUCHANDO.
	
	3. Cuando ya no tenga más datos a RECIBIR. Hace un BREAK. Finaliza y muestra la información en DESCODIFICACIÓN DE BINARIO A UTF8

# SERVIDOR

	1. Se abre el SERVIDOR en DETACH, el CLIENTE se conecta. 
	
	2. El servidor CALENDAR, le vomita la información.
	
	3. El CLIENTE finaliza.
	
	4. El SERVIDOR escucha al siguiente y lo añade a una LISTA VACÍA mediante APPEND.
	
	5. Le envíamos con un KILL -15 $(pgrep python).
	
	6. El SERVIDOR responde:
	
	ubuntu@keshi:~/Documents/ipc$ kill -15 $(pgrep python)
ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52574), ('127.0.0.1', 52576)] 2

	7. Significa que ha recibido la SEÑAL 15 que es SIGTERM --> Si ha recibido esa señal, termina el programa Y MOSTRARÁ QUIÉN SE HA CONECTADO + LA LONGITUD de USUARIOS CONECTADOS 
	
	
	---
	
	
## KILL y PRUEBAs

1. Se enciende el SERVIDOR en DETACH.

2. El cliente se conecta (s.connect((HOST,PORT)))y hace PETICIONES, se queda ESCUCHANDO y RECIBIENDO MENSAJES Infinitamente. Hasta que no tenga nada más que recibir.

3. El cliente finaliza y se conecta otro desde otro puerto dinámico de ORIGEN.

4. El servidor va registrando quién entra IP y PORT y CUENTA cuantos usuarios HAN ENTRADO (Lista vacía llistaPeers.append(addr, lo printa con un len print(llistaPeers, len(llistaPeers)) )
	
5. Desde otra CONSOLA le enviamos: (Se han CONECTADO 3 CLIENTES 1by1, de uno en uno)

	kill -10 $(pgrep python) --> SIGUSR1 (Print de CONEXIONES ACTIVAS)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 10
[('127.0.0.1', 52582), ('127.0.0.1', 52584)]
Connected by ('127.0.0.1', 52586)

	
	kill -12 $(pgrep python) --> SIGUSR2 (Print de CUANTOS SE HAN CONECTADO (LEN(lista)))

	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 12
3


	kill -15 $(pgrep python) --> SIGTERM 15 (TERMINA EL PROGRAMA)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52582), ('127.0.0.1', 52584), ('127.0.0.1', 52586)] 3

	
	
IMPORTANTE EL SYS.EXIT(0) LO HEMOS QUITADO UN MOMENTO DEL CLIENTE

#  sys.exit(0) # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos







## (IMPORTANTE)








TERMINAR DE HACER ESTOS APUNTES + VER APUNTES DE COMPAÑEROS + HACER LA PARTE PRÁCTICA DEL EXAMEN + DOCUMENTAR





#####################################################################



## 25-ps-client-one2one.py (CLIENTE)



import sys,socket,argparse 

# Importamos librerias

from subprocess import Popen, PIPE

# ------------- ARGPARSE

parser = argparse.ArgumentParser(description="""PS Client""")

# Se inicializa el ARGPARSE

parser.add_argument("-p","--port",type=int, default=50001) 

# Optional parameter como puerto default 50001

parser.add_argument("server",type=str) 

# Se conecta cualquiera

args=parser.parse_args()

# ---------------------------------------

# ------------- SOCKETS

HOST = args.server 

# A la constante se le pasa un ARGUMENTO POSICIONAL.

PORT = args.port 

# A la constante se le pasa un ARGUMENTO OPCIONAL.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Abre el SOCKET TCP # Se inicializa el SOCKET para conectarse

s.connect((HOST, PORT)) # Se conecta AL SERVIDOR



# ------------ POPEN

command = "ps ax" 

# Le pasamos el comando PS AX 

# Especifiquem la commanda que s'executarà (%d (integer), %s (string)--> any passat per argument)


pipeData = Popen(command, shell=True, stdout=PIPE) 

# Popen (shell=True --> es perquè funcioni)

# En la variable pipeData, le pasamos un POPEN(Contiene el COMANDO y la salida estándar PIPE) 

# 	# La salida estándar será el PIPE

# RECORRE EL POPEN Y LE ENVÍA EL COMANDO

  # Shell = True es IMPORTANTE

for line in pipeData.stdout: 

# Recorre el tubo # Enviem per el socket les linees

	s.send(line) 
        
#        # Recoge el tubo 
	
s.close()  

# Tanquem el socket (connexió)

sys.exit(0)



#### METODOLOGIA

	1. El cliente se conecta (Se le pasan argumentos)
	
	2. Se abre el SOCKET TCP del CLIENTE.
	
	3. El cliente LE MANDA EL comando "ps ax" al SERVIDOR.
	
		* Para cada línea de la salida estándar de pipeData, le envías con un s.send(line) al SERVIDOR.
	
	4. El servidor lo VOMITA y hace un PRINT.


	* El cliente cierra la conexión y se va.
	
	
NOTAS: No hace falta While true porque estamos enviando un comando y sabemos que el comando retornará un valor definido.

PRUEBAS: Con nc

	1. nc -l 50001
	
	2. python3 25-ps-client*.py localhost
	
	3. En el SERVIDOR se verifica y printa:
	

```
  23369 pts/0    S+     0:00 nc -l 50001
  23371 pts/1    Ss     0:00 bash
  23398 pts/1    S+     0:00 python3 25-ps-client-one2one.py localhost
  23399 pts/1    S+     0:00 /bin/sh -c ps ax
  23400 pts/1    R+     0:00 ps ax
keshi@KeshiKiD03:~$ 
```











#####################################################################



## 26-TELNET-CLIENT.PY (CLIENTE)





import sys,socket,argparse


from subprocess import Popen, PIPE 

## IMPORT ARGPARSE, SYS, SOCKET, SUBPROCESS --> POPEN Y PIPE


# ----------------- ARGPARSE

parser = argparse.ArgumentParser(description="""PS Client""")
parser.add_argument("-p","--port",type=int, default=50001)
parser.add_argument("server",type=str) # Se conecta cualquiera
args=parser.parse_args()

# ---------------------------------------

# ------------------ SOCKETS

HOST = args.server
PORT = args.port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Abre el SOCKET TCP

s.connect((HOST, PORT)) # Se conecta

# ----- IMPORTANTE FI DE CARACTER

## chr(4) es EOT = End of Transmition

FI = bytes(chr(4), 'utf-8') # Me convierte en BYTES el caracter 4 (EOT), se le asigna a la CONSTANTE FI




# Lo de ARRIBA es una plantilla

# Aquí es donde hacemos todo EL CLIENTE TELNET

while True: 

# Este bucle infinito, estará esperando a el servidor le conteste.
	command = input("%s> " % HOST) 
        
#        # Establecemos el input, string del comando

	if command == 'exit': break 
        
#        # Si el comando introducido es exit, salimos del programa

	s.send(bytes(command, 'utf-8')) 
        
#        # Envía mediante el socket el comando introducido en modo bytes
	
	while True: 
        
#        # Se realiza otro bucle para recibir y mostrar las líneas. 
	
		data = s.recv(1024) 
                
#                # Recibe las líneas

		if data[-1:] == FI: break 
                
#                # Si la última línea de los datos es el FI, sale del bucle. Hace un slicind. Significa que si el último DATO [-1:] recibido es = FI

		print(data.decode("utf-8")) 
                
#                # Printamos resultados

s.close()  

# Tanquem el socket (connexió)

sys.exit(0)


### METODOLOGIA Y SOLUCIÓN


METODOLOGIA:
	
1. El **CLIENTE** se conecta al **SERVIDOR** de **TELNET**.
		
2. El **CLIENTE** va haciendo **comandos** y el **SERVIDOR** le **RESPONDE**.
		
3. Si el **COMANDO** es igual a **EXIT**, hace un **BREAK**. O **"if not data: break"**
		
4. El **CLIENTE** envía los datos **(El comando)** al **SOCKET** al **SERVIDOR**.
		
5. El **SERVIDOR** recibe los datos **(El comando)** del **CLIENTE**
		
6. Se realiza otro **Bucle** para **escuchar**, *recibir* y *mostrar* las líneas provenientes del *SERVIDOR*.
		
7. Se queda *escuchando* el *SERVIDOR*.
		
8. Si la última *línea* de los *DATOS* *recibidos* del *SERVIDOR* es *FI*, sale del *BUCLE*. Hace un **"slicing"**. Significa que **empieza** desde el **final**, o si la última línea es **FI**, hace un **BREAK**.
		
9. Va *mostrando los resultados* de los **comandos** que va haciendo.
		
10. Cierra la *conexión* del **SOCKET** con el **SERVIDOR**.
		
11. Sale del *programa*.
		
		
	PRUEBAS / SOLUCIÓN:
	
	SÓLO CLIENTE: (USANDO NC)
	
	CLIENTE CON EL SERVIDOR:
	
	keshi@KeshiKiD03:~/Documents/ipc$ python3 26-telnet-client.py --port 50001 localhost
localhost> ls
01-head-[CORREGIDA].py

01-head.py
02-argument-[CORREGIDA].py
02-argument.py

03-head-args-[CORREGIDA].py

03-head-args.py

04b-head-choices-[CORREGIDA].py

04b-head-choices.py

04-head-choices-[CORREGIDA].py

04-head-choices.py















#####################################################################











#####################################################################


### SERVIDOR


#####################################################################

#### 21-ECHO-SERVER-SIMPLE.py (SERVIDOR)

HOST = ''
PORT = 50001

## Define el HOST, se conecta cualquiera y el PUERTO a abrir

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

## Abre constructor de SOCKET

s.bind((HOST,PORT)) 

# Crea el ENLACE de HOST y PORT.

s.listen(1) 

# Se queda ESCUCHANDO

conn, addr = s.accept()

# Guardem les variables conn i addr # # Implementa el ACCEPT. 
# Hasta que no acepte la conexión, no hace el accept.
# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).

print("Connected by", addr) 

### Printem quan és faci la connexió



while True: 

# Bucle infinit (per quan hi hagi dades)
  data = conn.recv(1024)    
  
  # El client envia les dades, el servidor les rep i les torna
  if not data:  
  
  # if not data = s'ha tancat la connexió, el servidor finalitzarà (SERVIDOR!)
      break
  conn.send(data)   
  
  # Tornem les dades
conn.close()    

# Client tanca la connexió (CLIENT!)

#####################################################################



## 22-DAYTIME-SERVER.py (SERVIDOR)



import sys,socket
from subprocess import Popen, PIPE

# ------------------------------------

HOST = ''   

# Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem.

#HOST = 'i23'

PORT = 50001    
# Definim port per connectar-nos al servidor (ex 21 (server))
#PORT = 13    

# Definim el 'PORT' contra el que volem connectar-nos (13 = DAYTIME)


### --------- PLANTILLA SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

# Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   

# Ens permet reutilitzar les IPs

s.bind((HOST,PORT)) 

# Hace el enlace del HOST y PORT. 

s.listen(1) 

# Se pone a escuchar.

conn, addr = s.accept() 

# Implementa el ACCEPT. # Hasta que no acepte la conexión, no hace el accept.

# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).

print("Connected by", addr) 

# Printem qui s'ha connectat. Mostra IP

#### -------- 

# ------------ POPEN

command = ["date"]  

# Li especifiquem el command que utiltizarem
pipeData = Popen(command,stdout=PIPE)   

# Executem el popen # La salida estándar será el PIPE

# RECORRE EL POPEN Y LE ENVÍA EL COMANDO
for line in pipeData.stdout:    

# Retornem les línees
  
  conn.send(line)   
  
  # Enviem la líena
conn.close()    

# Tanquem la connexió

sys.exit(0)

"""
# ----------------------------------------------

## Metodología

1. Ataca a un servidor DAYTIME y le contesta al CLIENTE con la FECHA. Se usa POPEN para redirigir y vomitar toda la información en "la salida estándar".


#####################################################################


## 23-DAYTIME-SERVER ONE2ONE.PY (SERVIDOR)



import sys, socket, argparse 

# Importa LIBRERIA SYS + ARGPARSE + SOCKET


from subprocess import Popen, PIPE 

# De subprocess, importa Popen y PIPE

## ARGPARSE

parser = argparse.ArgumentParser(description="""Daytime server""") 

# Llamamos el ARGUMENT PARSE
parser.add_argument("-p","--port",type=int, help="Port per on connectar nos", default=50001, dest="port")


args=parser.parse_args()


## --------------- SOCKET

HOST = ''
PORT = args.port 

# Indicamos que en la variable posicional de "args", me seleccionas .port = 50001 (Port defecto) o indicar.



#-------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# Ens permet reutilitzar les IPs


s.bind((HOST,PORT)) 

# Hace el enlace del HOST y PORT. 

s.listen(1)

# Se pone a escuchar

## DAYTIME SERVER ARGS --PORT

while True: 

# Bucle infinito # Bucle perquè no sabem quan acabarà ja que no sabem quantes línees ens enviarà

	conn, addr = s.accept() 
# Implementa el ACCEPT. 

# Hasta que no acepte la conexión, no hace el accept.

# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).

	print("Connected by", addr) 
        
# Printem qui s'ha connectat. Mostra IP


	command = ["date"]

# Li especifiquem el command que utiltizarem

	pipeData = Popen(command,shell=True,stdout=PIPE)  
        
# En la variable pipeData, le pasamos un POPEN(Contiene el COMANDO y la salida estándar PIPE) 

# La salida estándar será el PIPE



## # RECORRE EL POPEN Y LE ENVÍA EL COMANDO

# Shell = True es IMPORTANTE



	for line in pipeData.stdout: 
        
# Para cada línea de la salida estándar

		conn.send(line) 
                
# Envía cada LÍNEA AL CLIENTE


	conn.close() 
        
# Cierra la conexión con el CLIENTE.

sys.exit(0) 

# Sale del PROGRAMA.




"""
	* 23-daytime-server-one2one.py --> Se le pasa ARGUMENTO OPCIONAL --port o por default 50001.
	
		* Se abre una tubería para la SALIDA ESTÁNDAR.
		
		* Se le manda el pipeData para cada línea del .stdout del PIPE.
		
**23-daytime-server-one2one.py**

  Ídem exercici anterior, generar un daytime-server que accepta múltiples clients
  correlatius, és a dir, un un cop finalitzat l'anterior: *One2one*.

 * *One2one*: No té sentint que un servidor atengui un client i finalitzi. Una millora 
   (elemental) és anar atenent els clients un a un. Es connecta un client, se l'atén, es tanca
   la conexió amb aquest client i es passa a escoltar per rebre una nova conexió.
   En aquest cas el server fa un bucle ininit, va atenent clients infinitament un darrera l'altre
   (o si més no s'espera a entendre'ls). És per això que cal governar el servidor, per exemple
   amb senyals.

      * 23-daytime-server-one2one.py
      * 24-calendar-slient-one2one.py / 24-calendar-server-one2one.py









#####################################################################




### 24-CAL-SERVER-ONE2ONE.PY (REVISAR AQUI IMPORTANTE) (SERVIDOR)


import sys,socket,os,signal,argparse 

# 1. Se importan LIBRERÍAS

from subprocess import Popen, PIPE 

# 2. Se importe PIPE y POPEN de SUBPROCESS.

# -------------------- ARGPARSE

parser = argparse.ArgumentParser(description="""CAL server""") 

# 3. Se inicializa el ARGPARSE como CAL SERVER.


parser.add_argument("-a","--any",type=int, default=2019) 

# 4. Argumento posicional e Indica que por defecto un ANY por defecto 2019 (Puerto)

parser.add_argument("-p","--port",type=int, default=50001) 

# 5. Se crea un argumento POSICIONAL del tipo Integer y por defecto es 50001.

args=parser.parse_args() # 6. Se pulsa el botón del ARGPARSE

# --------------------- SOCKETS PLANTILLA

llistaPeers=[] 

# 1. Se define una LISTA de las conexiones. 
HOST = '' 

# 2. Se define una constante HOST (Localhost)
PORT = args.port 

# 3. Se define el PORT donde cogerá por el ARGUMENTO (parser) (PARSER)
ANY = args.any 

# 4. Se define una constante ANY que igual que el PORT, lo cogerá por el (parser)

# -------------------- SIGNALS MYHANDLER

# Definimos funciones para las SEÑAlES

# Por parámetro de cada función, cogerá el "SIGNUM" y el "FRAME".

def mysigusr1(signum,frame): 

# 1. Definim la funció del signal usr1 (kill -10)

  print("Signal handler called with signal:", signum) 
  
  # 2. Printa la señal recibida

  print(llistaPeers) 
  
  # 3. Llistem la llista de connexions

#  sys.exit(0) # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos
  
def mysigusr2(signum,frame): 

# 1. # Definim la funció del signal usr2 (kill -12)

  print("Signal handler called with signal:", signum) 
  
  # 2. Printará la señal recibida 

  print(len(llistaPeers)) 
  
  # 3. # Printem el len de la llista de connexions # Con la función len(lista)

#  sys.exit(0) # 4. SALE # Si se quiere mantener y saber cuantos tenemos, lo comentamos

def mysigterm(signum,frame): 

# 1. # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum) 
  
  # 2. Printa la señal recibida
  
  print(llistaPeers, len(llistaPeers)) # 3. 
  
  # Mostrem una llista amb les connexions i el len de totes les connexions que han hagut
  
  sys.exit(0) 
  
  # 4. SALE
  
# -------------------- SIGNALS + FORK()
  
pid=os.fork() 

# 1. # Crea una copia del PID, es decir crea un HIJO.

if pid !=0: 

# 2. # Fem l'if en funció el PID al pare.
  print("Engegat el server CAL:", pid) 
  
  # 3. El padre ha muerto pero el hijo sigue encendido.
  sys.exit(0) 
  
  # 4. Sale del programa (Está en DETACH)
  
  
  
signal.signal(signal.SIGUSR1,mysigusr1) 

# 1. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 10 (KILL -10)) recibida  (signal.SIGUSR1) + Llamará a la FUNCIÓN (mysigur1) = Listará la lista de Conexiones) 


signal.signal(signal.SIGUSR2,mysigusr2) 

# 2. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGUSR1 = 12 (KILL -12)) recibida  (signal.SIGUSR2) + Llamará a la FUNCIÓN (mysigur2) = Listará la LONGITUD de CONEXIONES (len))

 
signal.signal(signal.SIGTERM,mysigterm) 

# 3. Se asocia al constructor de SIGNAL.signal --> por parámetro (La SEÑAL (SIGTERM = 15 (KILL -15)) recibida  (signal.SIGTERM) + Llamará a la FUNCIÓN (mysigterm) = Terminará el programa y LISTARÁ la lista y la LONGITUD de CONEXIONES (len)) 


# -------------------- SERVIDOR SE PONE A ESCUCHAR (SOCKET)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 1. Se activa el SOCKET

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# 2. Se reusa el SOCKET

s.bind((HOST,PORT)) 

# 3. Hace el enlace de HOST y PORT

s.listen(1) 

# 4. Se queda escuchando.


######################################################

######  AQUÍ ES DONDE SE HACE TODA LA OPERACIÓN


while True: # Bucle infinit 

# Para que esté escuchando, para que esté atendiendo una conexión detrás de otro
  conn, addr = s.accept() 
  
## Implementa el ACCEPT. 
#       # Hasta que no acepte la conexión, no hace el accept.
#     	# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).


  print("Connected by", addr) 
  
  # Indica quién está conectado.
  llistaPeers.append(addr) 
  
  # Lo registra en la LISTA de conexiones

  # En la lista vacía, cada HOST que se conecte al SERVIDOR, lo REGISTRA. Hace un APPEND. Lo añade al final de la LISTA (OBJETO).

  command = "cal %d" % (ANY) 
  
  # Se establece el comando CAL y se le pasa a ANY (PUERTO)
  
  # %d es para pasar una VARIABLE. 
  
  # Pasará la orden CAL por el PUERTO ANY (Puerto dinámico para el Puerto ORIGEN)
  
  pipeData = Popen(command,shell=True,stdout=PIPE) 
  
  # En la variable pipeData, le pasamos un POPEN(Contiene el COMANDO y la salida estándar PIPE) 
	# La salida estándar será el PIPE
# RECORRE EL POPEN Y LE ENVÍA EL COMANDO
  # Shell = True es IMPORTANTE

  for line in pipeData.stdout: 
  
  # Para cada línea de la salida estándar
    conn.send(line) 
    
#   # Envía cada LÍNEA al CLIENTE

  conn.close() 
  
#  # Cierra la conexión con el CLIENTE.

sys.exit(0) 

# Sale del PROGRAMA.
  
##################################################

# SOLUCIÓN:


**24-calendar-client-one2one.py [-s server] [-p port]**

**24-calendar-server-one2one.py [-p port] [-a any]**

  Calendar server amb un popen, el client es connecta i rep el calendari. El server 
  tanca la connexió amb el client un cop contestat però continua escoltant noves connexions.

  El server ha de governar-se amb senyals que fan:
   - sigusr1: llista de peers i plega.
   - sigusr2: count de listpeer i plega.
   - sigterm: llista de peers, count i plega.

  El server és un daemon que es queda en execució després de fer un fork del seu
  pare (que mor) i es governa amb senyals.

  Que sigui el servidor qui rep l'any com a argument és una tonteria, seria més lògic
  fer-ho en el client, però el diàleg client servidor queda per a una pràctica
  posterior. Aquí es vol practicar usar un arg en el popen.
  
  
  
  
 
### SOLUCIÓN

# CLIENTE

	1. Se conecta a ATACAR al SERVIDOR que quiere. Y el PUERTO también.
	
	2. Se conecta al SOCKET destino, mediante HOST y PORT y se queda ESCUCHANDO.
	
	3. Cuando ya no tenga más datos a RECIBIR. Hace un BREAK. Finaliza y muestra la información en DESCODIFICACIÓN DE BINARIO A UTF8

# SERVIDOR

	1. Se abre el SERVIDOR en DETACH, el CLIENTE se conecta. 
	
	2. El servidor CALENDAR, le vomita la información.
	
	3. El CLIENTE finaliza.
	
	4. El SERVIDOR escucha al siguiente y lo añade a una LISTA VACÍA mediante APPEND.
	
	5. Le envíamos con un KILL -15 $(pgrep python).
	
	6. El SERVIDOR responde:
	
	ubuntu@keshi:~/Documents/ipc$ kill -15 $(pgrep python)
ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52574), ('127.0.0.1', 52576)] 2

	7. Significa que ha recibido la SEÑAL 15 que es SIGTERM --> Si ha recibido esa señal, termina el programa Y MOSTRARÁ QUIÉN SE HA CONECTADO + LA LONGITUD de USUARIOS CONECTADOS 
	
	
	---
	
	
## KILL y PRUEBAs

1. Se enciende el SERVIDOR en DETACH.

2. El cliente se conecta (s.connect((HOST,PORT)))y hace PETICIONES, se queda ESCUCHANDO y RECIBIENDO MENSAJES Infinitamente. Hasta que no tenga nada más que recibir.

3. El cliente finaliza y se conecta otro desde otro puerto dinámico de ORIGEN.

4. El servidor va registrando quién entra IP y PORT y CUENTA cuantos usuarios HAN ENTRADO (Lista vacía llistaPeers.append(addr, lo printa con un len print(llistaPeers, len(llistaPeers)) )
	
5. Desde otra CONSOLA le enviamos: (Se han CONECTADO 3 CLIENTES 1by1, de uno en uno)

	kill -10 $(pgrep python) --> SIGUSR1 (Print de CONEXIONES ACTIVAS)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 10
[('127.0.0.1', 52582), ('127.0.0.1', 52584)]
Connected by ('127.0.0.1', 52586)

	
	kill -12 $(pgrep python) --> SIGUSR2 (Print de CUANTOS SE HAN CONECTADO (LEN(lista)))

	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 12
3


	kill -15 $(pgrep python) --> SIGTERM 15 (TERMINA EL PROGRAMA)
	
	ubuntu@keshi:~/Documents/ipc$ Signal handler called with signal: 15
[('127.0.0.1', 52582), ('127.0.0.1', 52584), ('127.0.0.1', 52586)] 3

	
	
IMPORTANTE EL SYS.EXIT(0) LO HEMOS QUITADO UN MOMENTO DEL CLIENTE

#  sys.exit(0) # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos
























#####################################################################
















#####################################################################




















#####################################################################


-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 



















-------------------------------------------------------------------------------- 
