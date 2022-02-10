# UF2 - Scripts / Programació de Sistemes

## IPC Inter Process Comunication

## CHEAT SHEET REPRESENTATION 

* **HOST** = 'localhost'

* **PORT** = 7

* **s** = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Constructor de SOCKET.

* #**s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)**   # Ens permet reutilitzar les IPs

* **s.connect((HOST, PORT))** # Permite conectarnos, es *importante*.

* **s.send(b'Hello, world')** # Envía el mensaje Hello World en binario.

* **data = s.recv(1024)** Recibe el mensaje y contestará.

* **data.decode("utf-8")** --> Convierte el binario en convierte en UTF8. (Saldrá sin b'')

* **repr(data)** --> Representa en binario (Saldrá en b'Hello World')


* pgrep python

	* kill -15 $(pgrep python)

### SOCKETS

**CONCEPTOS GENERALES de REDES**

* Diálogo entre 2 interlocutores:

* Lo malo es que no sabemos cuando termina uno y cuando empieza el otro.

* ¿Cómo se resuelve?

	* CON UN PROTOCOLO.

		* Ejemplo1: HTTP

			* El cliente hace una petición HTTP --> Envía una CABECERA (GET, PUT, POST).

			* El servidor cuando recibe la petición, sabe separar la CABECERA.

				* Procesa la cabecera.

**LOS PROTOCOLOS DESCRIBEN CUANDO TOCA HABLAR EN CADA MOMENTO**

* Los protocolos se encargan de iniciar la conversación y que turno le toca.

* Está establecido todo el posible diálogo.

	* Ejemplo 2: SSH o Telnet. (Turnos)

		* El cliente envía una petición para conectarse.

		* El servidor responde: ¿Quién es?

		* El cliente contesta, soy PERE y mi password es PERE, déjame entrar.


**ES IMPORTANTE REMARCAR EL FINAL DE UN DIÁLOGO (YA ESTÁ)** = (
	
	**FI = bytes(chr(4), 'utf-8')**

	**conn.sendall(FI)**
	
	)**

**(Problema general de comunicación, por eso se necesitan protocolos para establecer la comunicación por orden.)**


### SOCKETS

* **¿Qué son?** Permiten comunicar 2 dispositivos en red. Cliente y Servidor. La conexión mediante sockets va por ([ip_origen] y [port_origen]) [socket_origen] + ([ip_destino] y [port_destino]) [socket_destino]

	* Client: Se conecta en el Servidor.

	* Servidor: Escucha por un puerto conocido.

	[Revisar_esquema]


* Ejemplo de puertos: *La IANA se encarga de reservar esos puertos*

	* El puerto de Postgres es el 5432

	* El puerto de SMB es el 139

	* El puerto de LDAP es el 389



**¿Cómo sabemos que la comunicación es única?**

	* Por la combinación de ([ip_origen] y [port_origen]) [socket_origen] + ([ip_destino] y [port_destino]) [socket_destino]


### EJEMPLOS PRÁCTICOS

**21-exemple-echo-client-simple.py**

**FINALIDAD** --> Enviar en el *socket* un *string* "hola", y contestar a este string con la *"misma"*. El programa, sabe que el servidor le responde y lo muestra por el **STDOUT** como prueba de que ha recibido la **respuesta del servidor**.

	* El CLIENTE. Envía un paquete por el puerto 7 (ECHO) y el SERVIDOR le devuelve el mensaje por STDOUT como acuse de recibo.

	* El SERVIDOR. Devuelve por STDOUT.

1. Instalar xinetd

```
apt-get install xinetd
```

2. Después de instalar `

*Editem els següents (possant 'disable = no'):*

	* echo
	* daytime
	* chargen

3. *Reiniciem i comprobem:*
```
systemctl stop xinetd + systemctl start xinetd + systemctl status xinetd
nmap localhost (han de sortir 7, 13 i 19)
```

STREAM = TCP (Es un flujo)

DATAGRAM = UDP

3. Con esto abrimos los puertos de ECHO (7), CHARGEN (19) (Vomita caracteres al infinito Char Generator ) y DAYTIME (13).

4. Probar los puertos:

	* **Con un cliente normal de Telnet.**

	* **Telnet es la orden cliente básica para órdenes TCP.**

		* telnet [7 / 13 / 19]

		* Para salir: CTRL + ALT GR + CLAUDATOR --> HO PAREM


**ÓRDENES CLIENTE**

* La primera es **NETCAT**
	
	* *echo_client*: nc localhost 7
	```
	ubuntu@keshi:/etc/xinetd.d$ nc localhost 7
	Hola
	Hola
	ls
	ls
	tumadre
	tumadre
	```

* La segunda es **TELNET**

	* *echo_client*: telnet localhost 7

	```
	ubuntu@keshi:/etc/xinetd.d$ telnet localhost 7
	Trying 127.0.0.1...
	Connected to localhost.
	Escape character is '^]'.
	Hola
	Hola
	adios
	adios
	tumadre
	tumadre
	```


5. El programa **CLIENTE** 21 ECHO:

1. Host y puerto donde atacar. HOST = "" | PORT = ""
2. Se abre el SOCKET. s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
3. Se conecta al SOCKET. s.connect((HOST, PORT))
4. Se envía el MENSAJE. s.send(b'Hello World')
5. Se RECIBE los datos. data = s.recv(1024)
6. Se CIERRA la conexión. s.close()
7. Se printan los datos recibidos. print('Received', repr(data)) o print('Received', data.decode("utf-8"))


## CLIENTE ECHO 21.PY

```
# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-echoClient.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket
#--------------------------------------
HOST = 'localhost'   # Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem.
#HOST = 'i23'
#PORT = 50001    # Definim port per connectar-nos al servidor (ex 21 (server))
PORT = 7    # Definim el 'PORT' contra el que volem connectar-nos (7 = echo)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Ens permet reutilitzar les IPs

s.connect((HOST, PORT)) # Ens connectem, es quedarà enganxat fins que es pugui connectar # Es important
s.send(b'Hello, world') # Enviem el missatge 'Hello, world' (b --> dades binàries)

data = s.recv(1024) # Rep el missatge i contestarà. # Està "hardcoded", rebrà un tamany fix de 1024
s.close()   # Tanquem la connexió.

print('Received', decode(data.decode("utf-8"))   # Printem el que hem rebut
sys.exit(0) # Sortim


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

-----------------------------------------------------------------------------
Sockets:
  * *Simple*: Exemples simples de construir un client/servidor. 

    - Simple indica que el servidor engega, escolta fins que rep una
    connexió, la atén i finalitza. Francament un servidor que processa un sol
    client en la seva vida útil és massa simple!.

    - Simple també indica que el contingut que es transmet del client al servidor i de retorn 
    al client és hardcoded i de mida limitada.


      * 21-exemple-echo-client-simple.py / 21-exemple-echo-server-simple.py


 * *Buffer*: El client (o el servidor) no té preestablert quanta informació es rebrà, per tant
   no n'hi ha prou de fer un sol reciv (escola un sol cop) sinó que cal fer un bucle per anar
   rebent informació mentre n'hi hagi. usualment és una estructura *"while not data"*.
"""
```

6. El programa **SERVIDOR** 21 ECHO:

	1. Se enciende el servidor y escucha conexiones. **s.listen(1)**

	2. El **CLIENTE** tiene que hacer un **CONNECT** y preguntar si se puede conectar. s.connect()

	3. Se crea el **CONSTRUCTOR de SOCKET**. s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	4. Se hace un **BIND**, hace **"ENLACE"** entre **HOST y PORT** de la máquina con el **servicio que estará escuchando con ese puerto**. BIND --> A que IP y PORT escucha.

	5. Se pone a escuchar **s.listen(1)**

	6. El SERVIDOR hace un **ACCEPT**. 
	
		Hasta que el SERVIDOR no acepta la conexión, la conexión no se establece. En el momento de hacer el ACCEPT, se establece la conexión. Sino estará esperando al infinito.

		**s.accept()** --> El servidor se queda colgado aquí hasta que el servidor ACEPTE una conexión. Retorna un OBJETO.

			* **Retorna una TUPLA**, retorna el primer elemento de la tupla connection --> ('conn') (OBJETO DEL TIPO CONNECTION) y el segundo elemento de la tupla es IP address --> ('addr') (OBJETO DEL TIPO IP Y PUERTO).

		* Una vez que se hace el ACCEPT --> Se printa el quién está conectado en el **SERVIDOR**. --> print("Connected by", addr) 

	7. Finalmente hace un **while True** para recorrer si hay datos. Se pone a escuchar si hubiera 1 o muchos datos. Y **break** si no recibe nada.

	8. Le envía al CLIENTE los datos que ha ido recibiendo y le contesta.

	9. Cierra la conexión del CLIENTE.


## SERVIDOR ECHO 21.PY

```
# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-echo-server-KESHI.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket
#--------------------------------------
HOST = ''   # Definim la constant 'HOST' --> Si no val res = 'localhost' --> Indica el host on atacarem.
#HOST = 'i23'
PORT = 50001    # Definim port per connectar-nos al servidor (ex 21 (server))
#PORT = 7    # Definim el 'PORT' contra el que volem connectar-nos (7 = echo)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Constructor de socket (socket.socket), construeix un "endoll" | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Ens permet reutilitzar les IPs

s.bind((HOST, PORT)) # Hace el enlace del HOST y PORT. 

s.listen(1) # Se pone a escuchar.

conn, addr = s.accept() # Implementa el ACCEPT. # Hasta que no acepte la conexión, no hace el accept.
# Retorna una TUPLA --> CONNECTION (SOCKET) Y ADDRESS (IP y PUERTO).
print("Connected by", addr) # Printem qui s'ha connectat. Mostra IP

while True: # Bucle infinito que se pondrá a escuchar datos, SI HUBIERA MÁS DE 1
    data = conn.recv(1024) # Rep el missatge i contestarà. # Està "hardcoded", rebrà un tamany fix de 1024
    if not data: # Si no hi han més dades a rebre, tanca la sessió, fa un BREAK (EL SERVIDOR FINALITZA!)
        break
    conn.send(data) # Retorna les dades
conn.close()   # Tanquem la connexió (CLIENT!).

print('Received', data.decode("utf-8"))   # Printem el que hem rebut
sys.exit(0) # Sortim

```



# ------------------------------------------------------------------------

### RESUMEN

0. Tanto CLIENTE como SERVIDOR abren los SOCKETS --> **s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)**

1. El SERVIDOR se pone a **ESCUCHAR** --> 

	s.bind((HOST,PORT))

	s.listen(1)

2. El CLIENTE quiere **CONECTARSE** --> s.connect((HOST,PORT))

3. El SERVIDOR **ACEPTA LA CONEXIÓN** --> conn, addr = s.accept() (Accepta el SOCKET ORIGEN y la ADDRESS (IP ORIGEN y PUERTO ORIGEN))

4. El SERVIDOR muestra quién se ha **CONECTADO**. --> print("Connected by", addr) (IP ORIGEN Y PUERTO ORIGEN)

5. El CLIENTE **ENVÍA** los **DATOS** al SERVIDOR --> s.send()

6. El SERVIDOR recibe los **DATOS** y con un **BUCLE INFINITO** **MANTIENE** la conexión hasta que **YA NO RECIBA DATOS** y termina la **SESIÓN DEL SERVIDOR**. Se queda escuchando hasta el infinito (
	while True:     
		data = conn.recv(1024)
	) esperando a recibir datos. Si lo recibe, devuelve datos al CLIENTE (conn.send(data) y si ya no recibe más (if not data:), finaliza el servidor (break) y finaliza sesión con el CLIENTE(break) y se va la conexión con el CLIENTE(conn.close()).

	data = conn.recv(1024) # Recibe el mensaje de tamaño fijo y contestará al cliente.

	if not data: # Si ya no hay más datos a recibir, cierra la **SESIÓN DEL SERVIDOR**
		
		break (Salta del bucle infinito)

7. El SERVIDOR le retorna los **DATOS RECIBIDOS** al CLIENTE.

	conn.send(data) # Envía datos al CLIENTE.

8. El CLIENTE recibe **DATA del SERVIDOR**, confirma que ha *recibido* su mensaje (ACK, acuse de recibo).

9. El CLIENTE **termina la sesión** con el SERVIDOR. 

	s.close()   # Tanquem la connexió con el SERVIDOR.

10. El SERVIDOR **termina su sesión** con el CLIENTE.

	conn.close() # Termina la sesión con el CLIENTE.





##################################################

# COLOR DE TERMINAL #00FF64 + #000000 

## EXAMEN CON PREGUNTAS 20 PREGUNTAS ## 

## HACER UN PROGRAMA EN PYTHON PRÁCTICO ## UF2 ES TODO LO QUE HEMOS HECHO DE PYTHON ##


###################################################

## BUCLE INFINIT | BUCLE INFINITO

* REBRE i ENVIAR

* ¿Cómo se cierra un **DIÁLOGO**?

* El que CORTA EL **DIÁLOGO** es el que **TERMINA LA COMUNICACIÓN**


**EL CLIENTE FINALIZA LA CONEXIÓN CON EL SERVIDOR s.close()**

	s.close()   # Tanquem la connexió con el SERVIDOR.

**EL SERVIDOR CUANDO YA NO TIENE MÁS DATOS A RECIBIR (if not data:), FINALIZA AQUÍ (break)**

	* Es importante remarcar que si eres el SERVIDOR y estás esperando DATOS, si no tienes el "if not data: break" --> Estará escuchando en el infinito (data = conn.recv(1024)).

######################################################

**ÓRDENES CLIENTE**

## EL CLIENTE 21 ECHO PY CONTRA SERVIDOR NC Y TELNET [FORMA_INTERACTIVA]

* La primera es **NETCAT**
	
	* *echo_client*: nc localhost 50001
	```
	keshi@KeshiKiD03:~/Documents/ipc$ nc localhost 50001
	Hola
	Hola
	Adios
	Adios
	tu madre
	tu madre
	```

	* *echo_server*:

* La segunda es **TELNET**

	* *echo_client*: telnet localhost 7

	```
	keshi@KeshiKiD03:~/Documents/ipc$ telnet localhost 50001
	Trying 127.0.0.1...
	Connected to localhost.
	Escape character is '^]'.
	Hola
	Hola
	Adios
	Adios
	Hallo
	Hallo
	```



## CONTRA EL SERVIDOR 21 ECHO PY [FORMA_INTERACTIVA]

* La primera es **NETCAT**
	
	* *echo_client*: nc localhost 50001
	```
	keshi@KeshiKiD03:~/Documents/ipc$ nc localhost 50001
	Hola
	Hola
	Adios
	Adios
	tu madre
	tu madre
	```

	* *echo_server*: nc -l 50002

	```
	SERVER NC INICIA y ESCUCHA POR EL 50002

	keshi@KeshiKiD03:~/Documents/ipc$ nc -l 50002

	CLIENTE ENVIA DATOS

	keshi@KeshiKiD03:~/Documents/ipc$ python3 21-exemple-echo-client-simple-KESHI.py
	Received (Indica que el cliente ha recibido la respuesta del servidor)

	keshi@KeshiKiD03:~/Documents/ipc$ 

	El servidor muestra el output.

	Hello, world
	keshi@KeshiKiD03:~/Documents/ipc$ 

	```

* La segunda es **TELNET**

	* *echo_client*: telnet localhost 50001

	```
	keshi@KeshiKiD03:~/Documents/ipc$ telnet localhost 50001
	Trying 127.0.0.1...
	Connected to localhost.
	Escape character is '^]'.
	Hola
	Hola
	Adios
	Adios
	Hallo
	Hallo
	```


######################################################

### APUNTES VARIADOS DE SOCKETS

* El servidor muestra quién está conectado y ofrece un puerto dinámico.

* El cliente cierra la conexión.

* El objeto conn = Es una caja que es un SOCKET (socket.socket) --> Contiene F4, Family String... --> Es una IP DEL SERVIDOR, PORT SERVER, IP del CLIENTE que se HA CONECTADO y PORT del CLIENTE que se ha conectado.

* **Connection Refused:** --> El SERVIDOR ha acabado, pero el puerto sigue **UTILIZÁNDOSE**, hay 2 formas, 1 usar la línea siguiente o 2 cambiar el puerto. Se verifica con SS. El SO tarda en liberar el puerto.

	**s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)**   # Ens permet reutilitzar les IPs

	**SE VERIFICA CON SS** --> Para saber DETALLADAMENTE info de los puertos.


* La conexión es **One 2 One**, quiere decir que hasta que no termine de ATENDER A 1 CLIENTE, no podrá escuchar el resto. Se mejorará después con el **MULTI**.

# telnet i nc (netcat) són ordres clients de qualsevol transmissió (TCP, UDP)
# nc -lk --> 'l' --> listen | 'k' --> Quan acaba una connexió, passa a la següent

* ss -t (TCP)

########################################################

#### REPASO RÁPIDO

1. Se ha definido un HOST PORT donde ESCUCHAR.

2. El SERVIDOR se espera.




########################################################

#### EJERCICIO 22 DAYTIME CLIENT SIMPLE PY

1. Abre un SOCKET dinámico que se conectará a un SERVIDOR de TIEMPO (DAYTIME).

	* Primero probar contra el puerto 13 de Xinetd

		* nc localhost 13

2. Cliente:

	* Establecerá una conexión. Llamará la conexión.

3. Servidor:

	* El SERVIDOR le vomita información al CLIENTE.

########################################################

#### PSEUDOCÓDIGO

* Ej 22

	* El CLIENTE quiere conectarse --> 
	
		s.connect()

		¿Cuantas líneas dialogan? No lo sabemos

			* El cliente debe hacer un bucle de Escuchar (while True: )

	* El SERVIDOR acepta la conexión --> s.accept()

	* El SERVIDOR le vomita información al cliente --> conn.send(data)

#### CODIGO


########################################################

#### EJERCICIO 22 DAYTIME CLIENT PY

* El cliente se queda escuchando (while True: (Bucle Infinito) + ataca al puerto 13 (Xinetd), se cambia luego al 50001 del servidor y el servidor le envía el daytime.




#### EJERCICIO 22 DAYTIME SERVER PY

* El servidor recibe la conexión (conn.recv(1024)) y le devuelve mediante Popen (Pipe), en su stdout (pipeData = Popen(command, stdout=PIPE)), el comando date (command = ["date"]).

##### INTRODUCCIÓN DEL POPEN EN SOCKETS

```
# POPEN
command = ["date"]  # Li especifiquem el command que utiltizarem
pipeData = Popen(command,stdout=PIPE)   # Executem el popen
# RECORRE EL POPEN Y LE ENVÍA EL COMANDO
for line in pipeData.stdout:    # Retornem les línees
  conn.send(line)   # Enviem la línEa
conn.close()    # Tanquem la connexió
```



####################### 09.02.22 SOCKETS

- Mientras se queda escuchando, escucha y printa **(ejercicio 22 CLIENT.py).**

	- Terminará de **escuchar** cuando le **cierran la puerta**.
	
	- El **s.recv(1024)** # El cliente se queda **escuchando**. Cuando le llegan datos, sale del **recv** y lo pone a **datos**.
	
	- Si **no** hay **datos = NONE**. Es porque ha le han **cerrado la CONEXIÓN**.

- El ejercicio 21 se queda **hardcoded**, por eso no hay un **while True**:




#### EJERCICIO 22 DAYTIME CLIENT SIMPLE PY

####################### 09.02.22 SOCKETS

- Mientras se queda escuchando, escucha y printa **(ejercicio 22 CLIENT.py).**

	- Terminará de **escuchar** cuando le **cierran la puerta**.
	
	- El **s.recv(1024)** # El cliente se queda **escuchando**. Cuando le llegan datos, sale del **recv** y lo pone a **datos**.
	
	- Si **no** hay **datos = NONE**. Es porque ha le han **cerrado la CONEXIÓN**.

- El ejercicio 21 se queda **hardcoded**, por eso no hay un **while True**:

- Solamente es un programa que **llama** y se pone a **escuchar**.


#### EJERCICIO 22 DAYTIME CLIENT SERVER PY



#### EJERCICIO 23 DAYTIME CLIENT ARGS PY

* Se implementan ARGUMENTOS, EL CLIENTE SE QUEDA ESCUCHANDO.

#### EJERCICIO 23 DAYTIME SERVER ONE2ONE PY

#### EJERCICIO 24 CAL CLIENT ONE2ONE PY

* Para que sea un DAEMON y no esté ocupando una terminal. 

	* Con un fork() --> Clona el proceso

	* Se obtiene el PID del PADRE. El padre MUERE pero el HIJO SIGUE ejecutándose.

		* El hijo se quedará escuchando al INFINITO.

	* Se quedará en DETACH (HIJO).

	* Se quedará en el INFINITO, hasta que le envíemos un kill -15 $(pgrep python)

* Sino se quedaría ejecutando en el infinito (SIN FORK y GETPID()).

* Se gobierna **POR SEÑALES**.

#### EJERCICIO 24 CAL SERVER ONE2ONE PY

* Para que sea un DAEMON y no esté ocupando una terminal. 

	* Con un fork() --> Clona el proceso

	* Se obtiene el PID del PADRE. El padre MUERE pero el HIJO SIGUE ejecutándose.

		* El hijo se quedará escuchando al INFINITO.

	* Se quedará en DETACH (HIJO).

	* Se quedará en el INFINITO, hasta que le envíemos un kill -15 $(pgrep python)

* Sino se quedaría ejecutando en el infinito (SIN FORK y GETPID()).


------------------

METODOLOGIA:

1. Tenemos un DAEMON. 

	* Tener un PADRE y que lance un FORK(), el padre MUERE y se queda el HIJO. (Se queda en DETACH)

	* El hijo se quedará escuchando conexiones al INFINITO.

	* Se gobernará con SEÑALES.

2. Las señales:

	* USR1 = Muestra la lista de CONEXIONES y TERMINA. (10)

	* USR2 = Muestra el número de CONEXIONES y TERMINA. (12) (S'han connectat un total de usuarios (append))

	* Si no termina (se complica más) --> Muestra la LISTA Y EL NÚMERO DE CONEXIONES. 	Y terminará

3. Orden cal = calendar.




#### EJERCICIO 25 PS CLIENT ONE2ONE PY

#### EJERCICIO 25 PS SERVER ONE2ONE PY

#### EJERCICIO 26 TELNET ONE2ONE PY

#### EJERCICIO 26 TELNET ONE2ONE PY

#### EJERCICIO 27 ECHO SERVER MULTI PY

#### EJERCICIO 28 TELNET SERVER MULTI PY
