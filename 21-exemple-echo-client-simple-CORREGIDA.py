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
HOST = 'localhost'   # Definim la constant 'HOST' --> Si no val res = 'localhost'
#HOST = 'i23'
PORT = 50001    # Definim port per connectar-nos al servidor (ex 21 (server))
#PORT = 7    # Definim el 'PORT' contra el que volem connectar-nos (7 = echo)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Constructor de socket (socket.socket) | socket.AF_INET --> per defecte | socket.SOCK_STREAM --> quan diu 'STREAM' és en TCP, 'DGRAM' és en UDP.
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Ens permet reutilitzar les IPs 

s.connect((HOST, PORT)) # Ens connectem
s.send(b'Hello, world') # Enviem el missatge 'Hello, world' (b --> dades binàries)

data = s.recv(1024) # Rep el missatge i contestarà.
s.close()   # Tanquem la connexió.

print('Received', repr(data))   # Printem el que hem rebut
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

# ----------------------------------------------

27.01.22 - SOCKETS

https://docs.python.org/3/library/socket.html 

## Metodología

Un altre mecanisme de comunicació IPC és la utilització de sockets. 

Podem analitzar els sockets existents amb ordres com netstat, ss, iptraf,  wiresark i nap. Amb la utilitat nc (netcat) podem observar també una comunicació client servidor simple 

1. Quien inicia la conversa y el turno.

2. Los SOCKETS los ENCHUFES --> Permite hay un enchufe.

3. El cliente siempre usa puertos dinámicos. El SO le asigna un puerto dinámico libre de los que tiene.

4. El servidor escucha un puerto conocido. O un puerto definido por la aplicación.

5. La comunicación es única:

	IP ORIGEN.
	
	IP DESTINO.
	
	SOCKET ORIGEN.
	
	SOCKET DESTINO.
	
	Establecen una comunicación única.

6. Ejemplo de Socket:

	Construir un echo server - echo client.

7. Si le dices hola bon dia, te responde hola bon dia.

8. apt-get install xinetd

9. 

echo

daytime

chargen

10. systemctl stop xinetd + systemctl start xinetd + systemctl status xinetd

11. nmap localhost (han de sortir 7, 13 i 19)

12. telnet  [7 / 13 / 19]
CTRL + ALT GR + CLAUDATOR --> HO PAREM

13. 

-------	  -------
|      |          |      |
|      |   Hola   |      |
|      |          |      |
|      |          |      |
-------          -------

14. STREAM = TCP

15. DGRAM = UDP

16. s.connect((HOST, PORT)) # Ens connectem, hasta que no se conecte estará en esa instrucción.

17. s.send(b'Hello, world') # Enviem el missatge 'Hello, world' (b --> dades binàries)

18. Retornan objetos.

19. 1. Ejecutar python3 21*-server.py y luegoe l CLIENTE.

20.







"""

