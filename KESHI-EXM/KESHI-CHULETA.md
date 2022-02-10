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


### 25-PS-SERVER-ONE2ONE.PY (SERVIDOR)



import sys,socket,os,signal,argparse,time


from subprocess import Popen, PIPE



# SE IMPORTAN LIBRERÍAS SYS, SOCKET, OS, SIGNAL, ARGPARSE, TIME Y DE SUBPROCESS POPEN, PIPE

## --------- ARGPARSE

# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """PS server""")

parser.add_argument("-a","--any",type=int, default=2022)

parser.add_argument("-p","--port",type=int, default=50001)

args=parser.parse_args()


# -------------------------------------

## --------- SOCKETS

llistaPeers=[]  

# Definim la llista buida de les connexions

HOST = ''   

# Definim com a HOST (localhost)
PORT = args.port    

# Definim el PORT que l'agafarà per l'argument (parser)
ANY = args.any  

# Definim ANY que a l'igual que PORT, ho agafarà per (parser)

## --------- SIGNALS MYHANDLER

def mysigusr1(signum,frame): 

# 1. Definim la funció del signal usr1 (kill -10)
  print("Signal handler called with signal:", signum) 
  
  # 2. Printa la señal recibida
  print(llistaPeers) 
  
  # 3. Llistem la llista de connexions
  sys.exit(0) 
  
  # 4. Sale del programa # Si se quiere mantener y saber cuantos tenemos, lo comentamos

def mysigusr2(signum,frame): 

# 1. # Definim la funció del signal usr2 (kill -12)
  
  print("Signal handler called with signal:", signum) 
  
  # 2. Printamos la señal recibida

  print(len(llistaPeers)) 
  
  # 3. # Printem el len de la llista de connexions # Con la función len(lista)
  
  sys.exit(0) 
  
  # 4. SALE # Si se quiere mantener y saber cuantos tenemos, lo comentamos

def mysigterm(signum,frame): 

# 1. # Definim la funció del signal term (kill -15)

  print("Signal handler called with signal:", signum)  
  
  # 2. Printamos la señal recibida
  
  print(llistaPeers, len(llistaPeers)) 
  
  # 3. # Mostrem una llista amb les connexions i el len de totes les connexions que han hagut

  sys.exit(0) 
  
  # 4. SALE

# ---------------------------------------

# -------------------- SIGNALS + FORK()


pid=os.fork() 

# 1. # Crea una copia del PID, es decir crea un HIJO.

if pid !=0: 

# 2. # Fem l'if en funció el PID al pare.

  print("Engegat el server CAL:", pid) 
  
  # 3. El padre ha muerto pero el hijo sigue encendido.
  
  sys.exit(0) 
  
  # 4. Sale del programa (Está en DETACH)


# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!



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


# ---------------------------------- EL PROGRAMA

############# 


# Lo de arriba es una plantilla

# Aquí es donde se hace TODO

while True: 

# Bucle infinit # Bucle infinit (atendre connexions un darrera l'altre)
  conn, addr = s.accept() 
  
  # Guardem les variables conn i addr # # Implementa el ACCEPT. 

#        # Hasta que no acepte la conexión, no hace el accept.

#	# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).

  print("Connected by", addr) 
  
  # Indica quién está conectado.

  llistaPeers.append(addr) 
  
  # Lo registra en la LISTA de conexiones
  
  # En la lista vacía, cada HOST que se conecte al SERVIDOR, lo REGISTRA. Hace un APPEND. Lo añade al final de la LISTA (OBJETO).
  
  
  
  # --- APERTURA DE FICHERO (IMPORTANTE!)
  
  fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%S")) # Se especifica en la variable, la ruta del FICHERO. 

  # fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%S"))
  	
#  	# 1. %s - %s - %s.log --> Indica que son 3 variables STRING.
  	
#  	# 2. En la primera posición de la ADDR[0] = Irá la IP.
  	
#  	# 3. En la segunda posición de la ADDR[1] = Irá el PUERTO.
  	
#  	# 4. Luego se especifica otro string, este caso, de la librería time. --> Usamos strftime(""%Y%m%d-%H%M%S"") --> Tendrá un Formato de Año, Mes, Dia, Hora, Min y Seg.
  
  fileLog=open(fileName,"w") 
  
  # Se abre un FICHERO especificado en fileName con sus características.
  
  # -----------------------------
  
  while True: 
  
  # Se realiza un BUCLE INFINITO para estar ESCUCHANDO el SERVIDOR.
  	
  	
  	data = conn.recv(1024) 
    
#    # El servidor está recibiendo DATOS del CLIENTE. (Está recibiendo porque el CLIENTE le manda el COMANDO.)
  	
  	
  	if not data: break 
    
#    # Cuando el otro me ha penjado el teléfono cierra. Si ya no hay más datos a recibir por parte del CLIENTE, salta del programa.
  	
  	
  	fileLog.write(str(data)) 
    
#    # Se realiza un write del fileLog(str(data)) --> Se lo pasamos en formato string plano.
  	
  conn.close() 
  
  # Cierra la conexión con el CLIENTE # Liberar el SOCKET.
  
  fileLog.close() 
  
  # Cierra EL FICHERO.
  
  # Acepta un CLIENTE

# No le ponemos el SYS.EXIT(0) porque sino se va y el CLIENTE no mostrará




###############################################




### METODOLOGIA 25-PS-SERVER.PY


##	TROUBLESHOOT: 
	
		¿En que casos usar "ESTAR ESCUCHANDO" -->data = s.recv(1024) (Si es CLIENTE) o conn.recv(1024) (Si es SERVIDOR)?
		
			* En este caso SIEMPRE que haya alguien "TANTO CLIENTE como SERVIDOR estén ENVIANDO datos a través del SOCKET"
			
				* En este caso el CLIENTE manda el COMANDO por POPEN (stdout) y el SERVIDOR lo recive (data = conn.recv(1024))

##	RESUMEN:
	
1. El **CLIENTE** quiere conectarse al **SERVIDOR**.
		
2. El **SERVIDOR** acepta el **CLIENTE**.
		
3. Cada **CLIENTE** que se conecte se guardará su **ADDR (IP y PUERTO ORIGEN)** a una **lista (llistaPeers)** y se añadirá al final de cada *línea* del fichero.
		
4. El **CLIENTE** le manda el **COMANDO** **"PS AX"** y todo su *CONTENIDO LO VOMITA* en la salida estándar del *PIPE*.
		
5. El *CLIENTE*, para cada línea del *COMANDO* **(No requiere While true)**, hace un **s.send(line)** --> Envía cada línea por el **SOCKET de DESTINO**.
		
6. El **SERVIDOR** recibe los **DATOS del CLIENTE** --> data = conn.recv(1024) 

### ESCUCHA DEL SOCKET
		
7. Se quedará escuchando hasta que el **CLIENTE** termine de enviarle **DATOS**. Ahí data valdrá **NONE**, entonces salta un **BREAK**.
		
8. Para cada dispositivo que se conecte al **SERVIDOR**, se escribirá en el fichero **fileLog** quién se ha CONECTADO (**(IP y PUERTO)** y la **HORA TIMESTAMP**).
		
9. El **CLIENTE** termina la conexión con el **SERVIDOR**. --> *s.close()*
		
10. El **SERVIDOR** termina la conexión con el **CLIENTE**. --> conn.close() 

### CIERRA EL SOCKET
		
11. El **SERVIDOR** cierra su fichero **fileLog**. --> **fileLog.close()**
		
12. Sale del *programa* --> *sys.exit(0)*
		
		----
		
		# EXTRA SI LE PASAMOS SEÑALES 10 12 Y 15
		
1. **10 SIGUSR1** - Muestra los SE HAN CONECTADO al SERVIDOR. **(llistaPeers)**
		
2. **12 SIGUSR2** - Muestra CUANTOS SE HAN CONECTADO al SERVIDOR. **len(llistaPeers)**
		
3. 15 Termina y sale del programa --> *ACCIÓN*: Printa los **QUE SE HAN CONECTADO** y **CUANTOS (llistaPeers)** se han **CONECTADO (len(llistaPeers)**).


----- IMPORTANTE
		
* EL SERVIDOR NO MUESTRA EL CONTENIDO DE PS AX -->
		
	* SINO QUE LO GUARDA EN EL FICHERO.
			
  * Lo visualizamos en /tmp/
		

keshi@KeshiKiD03:/tmp$ ls -l

total 264
-rw-rw-r-- 1 keshi keshi 24749 feb  9 23:58 127.0.0.1-52192-20220209-235856.log
-rw-rw-r-- 1 keshi keshi 24782 feb  9 23:59 127.0.0.1-52194-20220209-235955.log
-rw-rw-r-- 1 keshi keshi 25013 feb 10 00:04 127.0.0.1-52196-20220210-000434.log
-rw-rw-r-- 1 keshi keshi 25047 feb 10 00:05 127.0.0.1-52198-20220210-000506.log
-rw-rw-r-- 1 keshi keshi 25150 feb 10 00:09 127.0.0.1-52200-20220210-000909.log
-rw-rw-r-- 1 keshi keshi 23671 feb 10 00:15 127.0.0.1-52202-20220210-001504.log


* Observamos que se la sintaxis cumple con lo indicado.
		
		127.0.0.1-52192-20220209-235856.log
		
		[127.0.0.1] = addr[0] = IP ORIGEN 
			
		[52192] = addr[1] = PUERTO DINÁMICO ORIGEN
			
		[20220209-235856] = strftime
			
		("%Y%m%d-%H%M%S").log
			
			
	DENTRO: 
	
	keshi@KeshiKiD03:/tmp$ cat 127.0.0.1-52192-20220209-235856.log 
b'    PID TTY      STAT   TIME COMMAND\n'b'      1 ?        Ss     0:07 /sbin/init splash\n'b'      2 ?        S      0:00 [kthreadd]\n'b'      3 ?        I<     0:00 [rcu_gp]\n'b'      4 ?        I<     0:00 [rcu_par_gp]\n'b'      6 ?        I<     0:00 [kworker/0:0H-events_highpri]\n'b'      8 ?        I<     0:00 [mm_percpu_wq]\n'b'      9 ?        S      0:00 [rcu_tasks_rude_]\n     10 ?        S      0:00 [rcu_tasks_trace]\n     11 ?        S      0:00 [ksoftirqd/0]\n     12 ?        I      0:02 [rcu_sched]\n'b'     13 ?        S      0:00 [migration/0]\n     14 ?        S      0:00 [idle_inject/0]\n     16 ?        S      0:00 [cpuhp/0]\n     17 ?        S      0:00 [cpuhp/1]\n     18 ?        S      0:00 [idle_inject/1]\n     19 ?        S      0:00 [migration/1]\n     20 ?        S      0:00 [ksoftirqd/1]\n     22 ?        I<     0:00 [kworker/1:0H-events_highpri]\n     23
		

####################################################3


### CORREGIDA EN CLASE

PROGRAMA TIENE LA SEÑAL 1

VA ACUMULANDO LAS SEÑALES

SERVIDOR ONE 2 ONE --> ACEPTA UNA CONEXIÓN AL MISMO TIEMPO.


Todo el programa va en el WHILE TRUE (Está todo ahí)

El resto es una PLANTILLA. [IMPORTANTE]







Se conectan al puerto 50001 y se guarda en un FICHERO.

El servidor hace un WHILE TRUE (Cada iteración atiende un cliente, a la propera atiende a otro)




## CORREGIR PROGRAMA SERVIDOR

## EXPLICACIÓN

WHILE TRUE:
-----
	aceptar la conexión

	nom = generar_nom

	open del fitxer
	
	bucle
	
		read del socket
		
		write fitxer

	cerrar el fitxer

	socket.close() --> Cerrar el socket

----






1. Necesitamos el NETCAT

	nc -l 50001

2. Se conecta, vomita y cierra. --> python3 25-ps-client... localhost

3. En el SERVIDOR se verifica


isx36579183@i11:~/Documents/ipc$ nc -l 50001
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:02 /sbin/init
      2 ?        S      0:00 [kthreadd]
      3 ?        I<     0:00 [rcu_gp]
      4 ?        I<     0:00 [rcu_par_gp]
      6 ?        I<     0:00 [kworker/0:0H-events_highpri]
      8 ?        I      0:00 [kworker/u16:0-flush-259:0]
      9 ?        I<     0:00 [mm_percpu_wq]
     10 ?        S      0:00 [rcu_tasks_rude_]
     11 ?        S      0:00 [rcu_tasks_trace]
     12 ?        S      0:00 [ksoftirqd/0]
     13 ?        I      0:00 [rcu_sched]
     14 ?        S      0:00 [migration/0]
     15 ?        S      0:00 [cpuhp/0]
     16 ?        S      0:00 [cpuhp/1]
     17 ?        S      0:00 [migration/1]
     18 ?        S      0:00 [ksoftirqd/1]
     20 ?        I<     0:00 [kworker/1:0H-events_highpri]
     21 ?        S      0:00 [cpuhp/2]
     22 ?        S      0:00 [migration/2]
     23 ?        S      0:00 [ksoftirqd/2]
     25 ?        I<     0:00 [kworker/2:0H-kblockd]
     26 ?        S      0:00 [cpuhp/3]
     27 ?        S      0:00 [migration/3]

.......














#####################################################################


## 26-TELNET-SERVER.PY (SERVIDOR)

import sys,socket,os,signal,argparse,time

from subprocess import Popen, PIPE

# -------------------------------------

parser = argparse.ArgumentParser(description=\
        """TELNET SERVER""")


parser.add_argument("-p","--port",type=int, default=50001)

parser.add_argument("-d","--debug",action='store_true',default=False) 

# La opción es para que le aparezca debug


args=parser.parse_args()


# -------------------------------------


HOST = ''   

# Definim com a HOST (localhost)

PORT = args.port    

# Definim el PORT que l'agafarà per l'argument (parser)

FI = bytes(chr(4), 'utf-8')

# ---------------------------------------

# ---------- Saber el proceso ---------- 

pid=os.fork() 


# Hace un duplicado, lo creaba y se ejecutaba.


if pid != 0:    


# Fem l'if en funció el PID al pare.

  print("Engegat el server TELNET:", pid)

  sys.exit(0)   
  
  
  # Apaga el proceso padre, mientras que el hijo seguía encendido.

# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!

# --- Todo lo de abajo es el proceso hijo ----

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reusa SOCKET
s.bind((HOST,PORT))
s.listen(1)


# Lo de arriba es una plantilla

# Aquí es donde se hace TODO
while True: 

# Bucle infinit # Bucle infinit (atendre connexions un darrera l'altre)

    conn, addr = s.accept() 
    
#    # Guardem les variables conn i addr

    print("Connected by", addr) 
    
#    #  Printem

    while True:
        command = conn.recv(1024) 
        
#        # Recibe data

        if args.debug: 
        
#        # Args.debug = DebugImprime en el servidor el resultado

            print ("Telnet> %s" % (command)) 
            
#            # Imprime el comando

        if not command: break 
        
#        # Cuando el otro me ha penjado el teléfono cierra.

        pipeData = Popen(command, shell=True, stdout=PIPE, stderr=PIPE) 
        
#        # Hace un Popeen que hace PWD 

#		# Iterar linea a linea y muestra el resultado de este POPEN

        for line in pipeData.stdout: 
        
#        # Recorre cada linea del Popen # Pipe de SALIDA
 
            if args.debug:

                print(line) 
                
#                # Printa cada línea.

            conn.sendall(line) 
            
#            # Envía la línea # Se asegura de vacíar el bufer, envía todo.

        for line in pipeData.stderr:
        
#        # Pipe de ERROR

            if args.debug:

                print("Error: %s" % line)
            
            conn.sendall(line) 
            
#            # Envía la línea    
 
        conn.sendall(FI)
 
    conn.close() 
    
#    # Cierra la conexión # Liberar el SOCKET. # El cliente termina la conexión

# s.close()

sys.exit(0)

  # Acepta un CLIENTE
  
  
  # EDITAR EL SERVIDOR Y VERIFICAR















#####################################################################


-------------------------------------------------------------------------------- 



## 27-ECHO-SERVER-MULTI.PY (SERVIDOR)

# UF2 - Scripts / Programació de Sistemes

# IPC Inter Process Comunication

##################################################

# COLOR DE TERMINAL #00FF64 + #000000

## EXAMEN CON PREGUNTAS 20 PREGUNTAS ## 

## HACER UN PROGRAMA EN PYTHON PRÁCTICO ## UF2 ES TODO LO QUE HEMOS HECHO DE PYTHON ##

##################################################

## EJERCICIO 27 ECHO SERVER MULTI ##

* Para atender múltiples CONEXIONES

	* Select.select (Python)
	
* Recibe argumentos 3 iterables de cosas que pueden esperar. --> Listas de espera.

*  

" The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned. "

* Retorna una triple lista, de un subconjunto que había en el inicio.


* EJEMPLO

* Retornará el nombre de esas 2 personas que han levantado el brazo para ser atendidos

* Cuando haya acabado de atenderlos, volverá al "select.select"

* Mirar si hay alumnos con el brazo levantado, volverá a atenderlos y sino, estarán esperando.

* El juego es, mandaar una faena, cuando se termine, levantar el brazo.

+ En algún momento 2 alumnos levantan el brazo, se atienden.

+ Se termina, vuelve a mirar si alguien ha levantado el brazo y se atiende.



## METODOLOGIA

1. El cliente 1 se conecta al conns=[s]

2. Si un cliente quiere conexión, levanta el brazo.

3. Se almacena en ACTIUS (Los que han levantado el brazo).

4. Hay un bucle porque puede que hayan persoans que han levantado el brazo.

5. for actual = s in actius:

6. 	if actual == s: # Es una conexión nueva? La s es el SOCKET VIRGEN. Para saberlo es lo que se ha movido es una s

7.	El primer bucle es si hay una conexión nueva.

	* Hace el accept() --> Pasa a tener una conn, addr (CONEXIÓN)
	
	* Se añade a una lista de cosas pendientes. --> conns.append(conn) # Es un objeto que se mete a "conns". 
	
	* conns = [s, c1, c2, c3]

8.	El segundo es de los que ya están.

9.	Si un nuevo cliente quiere conectarse, sacude el cable. Entra al bucle, busca la "s"

Si se cierra y se abre, será una conexión nueva.



---


## ¿Cómo se programa?

## Hay una lista se llama conns=[s] | Socket es la oreja que escucha | Cuando se conecta alguien se crea una CONEXIÓN.

conns = [s, c1, c2, c3]



## conns = Socket que escucha --> Lista conns --> Es poner la s (socket que escucha)





---------

[REVISAR LA ÚLTIMA PARTE DEL AUDIO 02.02.22 - 27 PY]

actius: [s, c1] --> Genera actividad en el cable. 

El bucle iterará 2.



--------




### PROGRAMA 27-ECHO-SERVER-MULTI.PY

import socket, sys, select, os

HOST = ''                 
PORT = 50007             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(os.getpid())
conns=[s] # Es el socket que "escucha", manda deberes y se pone a escuchar si alguien le llama.
while True:
    actius,x,y = select.select(conns,[],[]) # Llama el select.select, la primera es una lista de objetos iterables que se esperen para ser leídos, los 2 son read y write.
    
    # Actius = Retorna los que han levantado el brazo.
    
    # Actius : s, c1
    
    for actual in actius: # actual: s, c1, c2, c3, Si son nuevas conexiones # Es lo que se está procesando actualmente, no sabemos si es c1, c2, c3
        if actual == s: # Si el actual es s
            conn, addr = s.accept()
            print('Connected by', addr)
            conns.append(conn)
        else: # Echo Server # Si no son nuevas conexiones
            data = actual.recv(1024) # Escucha y recibe
            if not data: # Si me han colgado
                sys.stdout.write("Client finalitzat: %s \n" % (actual))
                actual.close()
                conns.remove(actual)
            else:
                actual.sendall(data) # Rebota, retorna el "hola" # Vuelve al bucle.
                #actual.sendall(chr(4),socket.MSG_DONTWAIT)
s.close()
sys.exit(0)



### SE TRATA DE ENTENDER ###

### CONSTRUIR EL TELNET MÚLTIPLE
















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
