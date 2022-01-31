# /usr/bin/python
#-*- coding: utf-8-*-
#
# list-users [-f file]
# 10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse # Llamamos a la LIBRERÍA SYS y ARGPARSE
parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks") # Activamos ARGPARSE
parser.add_argument("-f","--fit",type=str,\
        help="user file or stdin (/etc/passwd style)", metavar="file",\
        default="/dev/stdin",dest="fitxer") # Añadimos un argumento opcional
args=parser.parse_args() # Apretamos el botón de ARGPARSE
# -------------------------------------------------------
class UnixUser(): # Definimos una clase de UnixUser()
  """Classe UnixUser: prototipus de /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""
  def __init__(self,userLine): # Definimos un nuevo tipo para la clase, en este caso es un MÉTODO ESPECIAL, un CONSTRUCTOR INICIALIZADOR.
    # Es decir creará una caja en blanco y dentro almacenará 1 propiedad.
    "Constructor objectes UnixUser"
    userField=userLine.split(":") # Hacemos el método split(":"), para que nos separe en : cada objeto.
    self.login=userField[0] # Cogemos los datos de la primera posición y la colocamos en LOGIN
    self.passwd=userField[1] # Cogemos los datos de la segunda posición y la colocamos PASSWD 
    self.uid=int(userField[2]) # ...
    self.gid=int(userField[3])
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6][:-1]

  def show(self): # Definimos un nuevo TIPO/FUNCIÓN que será para MOSTRAR
    "Mostra usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}") # Usamos FORMATTED STRINGS para que nos muestre el resultado de cada variable.

  def __str__(self):
    "Fa string de la instancia"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
    
    # Es importante definir el Método Especial __str__(self) ya que nos resultará más legible a la hora de hacer print en lugar de mostrarnos algo así: print(user1) --> "<__main__.UnixUser object at 0x7f35bcfb6fd0>"
    
# -------------------------------------------------------
fileIn=open(args.fitxer,"r") # Abrimos el ARGPARSE --> Fitxer en modo READ.
userList=[] # Se declara una LISTA VACÍA.
for line in fileIn: # Se recorre cada línea del FICHERO.
  oneUser=UnixUser(line) # Asigname cada LÍNEA de UnixUSer(line) a un objeto, en este caso oneUser.
  userList.append(oneUser) # La LISTA userList contiene 10 cajas de memorias. # Añadimos cada USUARIO (Objeto) a la LISTA.
fileIn.close() # Cerramos el FICHERO de entrada.
for user in userList:
 print(user) # Lista por pantalla todos los usuarios recorriendo la LISTA.
exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**07-list-users.py   [-f file]**

  Donat un file tipus /etc/passwd o stdin (amb aquest format) fer:
  * el constructor d'objectes *UnixUser* rep un strg amb la línia sencera 
    tipus /etc/passwd.
  * llegir línia a línia cada usuari assignant-lo a un objecte 
    UnixUser i afegir l’usuari a una llista d’usuaris UnixUser.
  * un cop completada la carrega de dades i amb la llista amb 
    tots els usuaris, llistar per pantalla els usuaris recorrent la llista.

# ----------------------------------------------

## Explicación

**07-list-users.py   [-f file]**

  Donat un file tipus /etc/passwd o stdin (amb aquest format) fer:
  * el constructor d'objectes *UnixUser* rep un strg amb la línia sencera 
    tipus /etc/passwd.
  * llegir línia a línia cada usuari assignant-lo a un objecte 
    UnixUser i afegir l’usuari a una llista d’usuaris UnixUser.
  * un cop completada la carrega de dades i amb la llista amb 
    tots els usuaris, llistar per pantalla els usuaris recorrent la llista.

# ----------------------------------------------

## Metodología




# Hay una clase UnixUser(): 



# userList=[]

Declara una lista 

# for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
for user in userList:
 print(user)
 
 
Hace 2 bucles, el primer bucle


LEER UNA LINEA, CREA UN OBJETO UnixUser():

Contiene una lista de Usuarios

Otro bucle que hace que recorre y printa.












----------------------------------------------------------------------------

# head /etc/passwd > passwd.txt

# python3 07-list-users.py -f passwd.txt


# isx36579183@i11:~/Documents/ipc$ head /etc/passwd > passwd.txt
# isx36579183@i11:~/Documents/ipc$ python3 07-list-users.py -f passwd.txt

root x 0 0 root /root /bin/bash
daemon x 1 1 daemon /usr/sbin /usr/sbin/nologin
bin x 2 2 bin /bin /usr/sbin/nologin
sys x 3 3 sys /dev /usr/sbin/nologin
sync x 4 65534 sync /bin /bin/sync
games x 5 60 games /usr/games /usr/sbin/nologin
man x 6 12 man /var/cache/man /usr/sbin/nologin
lp x 7 7 lp /var/spool/lpd /usr/sbin/nologin
mail x 8 8 mail /var/mail /usr/sbin/nologin
news x 9 9 news /var/spool/news /usr/sbin/nologin
isx36579183@i11:~/Documents/ipc$ 


"slicing"

Hace un slicing desde el principio.

python3


"kakakum"[:3] --> Muestra el número de string


hexdump -C passwd.txt

04 --> Salt de Linea

["patata","pere","poma"][1] 

'pere'

["patata","pere","poma"][1][:2]
0         1       2

'pe'



UnixUser():



python3


>>> class UnixUser():
...   """Classe UnixUser: prototipus de /etc/passwd
...   login:passwd:uid:gid:gecos:home:shell"""
...   def __init__(self,userLine):
...     "Constructor objectes UnixUser"
...     userField=userLine.split(":")
...     self.login=userField[0]
...     self.passwd=userField[1]
...     self.uid=int(userField[2])
...     self.gid=int(userField[3])
...     self.gecos=userField[4]
...     self.home=userField[5]
...     self.shell=userField[6][:-1]
...   def show(self):
...     "Mostra les dades de l'usuari"
...     print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
...   def __str__(self):
...     "functió to_string"
...     return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)



# userList
[]

# for line in fileIn:

oneUser=UnixUser(line)

userList.append(oneUser)

userList --> Contiene 10 cajas de memorias.

userList[0] --> <__main__.UnixUser object at ....



# help(user1)

# help(user1.show)

# l=[] --> Es una lista

# help(l) --> Language reference, el library reference

# l="papa"

# help(l) --> Información de una string

# help(str)

# help(dict)

# dir(str) --> Todos los métodos que tiene un string

# dir(list) --> Todos los métodos de una lista

# dir(UnixUser)



# Programació de Sistemes

# Probar interactivamente

# Library Reference o dentro del Python

# userList[1].show()

# >>> fileIN=open("passwd.txt","r")
>>> fileIN
<_io.TextIOWrapper name='passwd.txt' mode='r' encoding='UTF-8'>
>>> 


# fileIN.readline() --> Es un STRINg

>>> fileIN.readline()
'root:x:0:0:root:/root:/bin/bash\n'
>>> 



# fileIN.readline()[1:5]

>>> fileIN.readline()[1:5]
'aemo'


# fileIN.readline()[:-1]

>>> fileIN.readline()[:-1]
'bin:x:2:2:bin:/bin:/usr/sbin/nologin'
>>> 


# type(userList)

>>> type(userList)
<class 'list'>
>>> 

# userList[0].uid --> Es un enter

# type(userList[0].uid)

#






# Da error en el python3

####################################

fileIn=open(args.fitxer,"r")
userList=[]
for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
for user in userList:
 print(user)

####################################


# VERIFICACIÓN



isx36579183@i11:~/Documents/ipc$ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> class UnixUser():
...   """Classe UnixUser: prototipus de /etc/passwd
...   login:passwd:uid:gid:gecos:home:shell"""
...   def __init__(self,userLine):
...     "Constructor objectes UnixUser"
...     userField=userLine.split(":")
...     self.login=userField[0]
...     self.passwd=userField[1]
...     self.uid=int(userField[2])
...     self.gid=int(userField[3])
...     self.gecos=userField[4]
...     self.home=userField[5]
...     self.shell=userField[6][:-1]
...   def show(self):
...     "Mostra les dades de l'usuari"
...     print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
...   def __str__(self):
...     "functió to_string"
...     return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
... 
>>> fileIn=open("passwd.txt","r")
>>> userList=[]
>>> for line in fileIn:
...   oneUser=UnixUser(line)
...   userList.append(oneUser)
... 
>>> for user in userList:
...  print(user)
... 
root x 0 0 root /root /bin/bash
daemon x 1 1 daemon /usr/sbin /usr/sbin/nologin
bin x 2 2 bin /bin /usr/sbin/nologin
sys x 3 3 sys /dev /usr/sbin/nologin
sync x 4 65534 sync /bin /bin/sync
games x 5 60 games /usr/games /usr/sbin/nologin
man x 6 12 man /var/cache/man /usr/sbin/nologin
lp x 7 7 lp /var/spool/lpd /usr/sbin/nologin
mail x 8 8 mail /var/mail /usr/sbin/nologin
news x 9 9 news /var/spool/news /usr/sbin/nologin
>>> 




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

