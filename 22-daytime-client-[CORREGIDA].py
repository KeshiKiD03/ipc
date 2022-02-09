# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-client.py  
# Fem una connexió amb el servidor, i ell quan vegi una connexió ens vomitarà informació.
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket
# -------------------------------------
HOST = '' # Se define una constante al HOST a la que atacar
#PORT = 50001 # Se define una constante al PUERTO a atacar
PORT = 13

#### -------- PLANTILLA SOCKET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Se crea el constructor del SOCKET
s.connect((HOST, PORT)) # Se conecta al HOST y PUERTO

#### -------- 

while True: # Bucle que permite escuchar Infinitamente, porque no sabemos cuantas líneas enviará. # Bucle perquè no sabem quan acabarà ja que no sabem quantes línees ens enviarà
  data = s.recv(1024)   # El client rep la data del servidor.
  if not data: # s'ha tancat la connexió (SERVER FINALITZA)
      break
  print('Data:', repr(data))
s.close()

sys.exit(0)


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

 * 22-daytime-client.py / 22-daytime-server.py 


 * *One2one*: No té sentint que un servidor atengui un client i finalitzi. Una millora 
   (elemental) és anar atenent els clients un a un. Es connecta un client, se l'atén, es tanca
   la conexió amb aquest client i es passa a escoltar per rebre una nova conexió.
   En aquest cas el server fa un bucle ininit, va atenent clients infinitament un darrera l'altre
   (o si més no s'espera a entendre'ls). És per això que cal governar el servidor, per exemple
   amb senyals.


# ----------------------------------------------

## Metodología

1. El cliente envía datos. El servidor recibe los datos. 

2. El programa recibe llama a la puerta

Hace s.connect((HOST, PORT))

# Se quedará enganchado hasta que alguien le abra la puerta.

3. Cuando termina de escuchar? Cuando cierra de golpe.

4. Como root se enciende el xinetd.

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

