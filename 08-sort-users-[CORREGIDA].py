# /usr/bin/python
#-*- coding: utf-8-*-
#
# sort-users [-s login|gid]  file
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys, argparse # Llamamos a la LIBRERÍA SYS y ARGPARSE
from functools import cmp_to_key # Especificamos que dentro de FUNCTOOLS importamos CMP_TO_KEY
parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks") # Inicializamos el ARGPARSE
parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: login | gid", metavar="criteria",\
        choices=["login","gid"],dest="criteria",default="login") # Añadimos un argumento opcional donde podemos escoger login o gid. Se guarda en una variable "criteria", por defecto es login.
        # Choices es entre claudators.
parser.add_argument("fitxer",type=str,\
        help="user file (/etc/passwd style)", metavar="file") # Se usa un argumento posicional obligatorio que nos permite especificar el archivo.
args=parser.parse_args() # Se pulsa el botón de ARGPARSE.
# -------------------------------------------------------
class UnixUser(): # Creamos una CLASE donde tendremos nuevos TIPOS.
  """Classe UnixUser: prototipus de /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""
  def __init__(self,userLine): # Creamos una INSTANCIA nueva de una CLASE. En este caso es un MÉTODO ESPECIAL. Un CONSTRUCTOR INICIALIZADOR de OBJETOS. Se especifica una variable como parámetro.
    "Constructor objectes UnixUser"
    userField=userLine.split(":") # # Hacemos el método split(":"), para que nos separe en : cada objeto.
    self.login=userField[0] # Cogemos los datos de la primera posición y la colocamos en LOGIN ...
    self.passwd=userField[1]
    self.uid=int(userField[2])
    self.gid=int(userField[3])
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6][:-1]
    
    
  def show(self): # Mostramos los datos del usuario con FORMATTED STRINGS
    "Mostra les dades de l'usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
    
    
  def __str__(self): # Hacemos que sea más legible el OUTPUT. To STRING
    "functió to_string"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
# -------------------------------------------------------
def sort_login(user):
  '''Comparador d'usuaris segons el login'''
  return user.login # Comparador de usuarios según el LOGIN
  
def sort_gid(user):
  '''Comparador d'usuaris segons el gid'''
  return (user.gid, user.login) # COMPARADOR DE USUARIOS SEGÚN EL GID
# -------------------------------------------------------
fileIn=open(args.fitxer,"r")
userList=[] # Creamos una LISTA VACÍA
for line in fileIn: # Se recorre cada línea en fileIn de /etc/passwd
  oneUser=UnixUser(line) # Se separa cada línea en OBJETOS y se añaden en oneUser
  userList.append(oneUser) # Cada usuario se añade a la LISTA VACÍA.
fileIn.close() # Cerramos el fichero
if args.criteria=="login": # Si el CRITERIO es igual a LOGIN
  userList.sort(key=sort_login) # Ordename por LOGIN. Sort_login se añade a la varaible = key.
else: # De lo contrario
  userList.sort(key=sort_gid) # Ordename el GID. Sort_gid se añade a la varaible = key.
for user in userList: # Se recorre cada usuario en la LISTA userList
 print(user) # Muestrame el USUARIO.
exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**08-sort-users.py [-s login|gid] file**

  Carregar en una llista a memòria els usuaris provinents d'un fitxer
  tipus /etc/passwd, usant objectes *UnixUser*, i llistar-los.
  Ordenar el llistat (stdout) segons el criteri login o el criteri 
  gid (estable).

# ----------------------------------------------

## Explicación

**08-sort-users.py [-s login|gid] file**

  Carregar en una llista a memòria els usuaris provinents d'un fitxer
  tipus /etc/passwd, usant objectes *UnixUser*, i llistar-los.
  Ordenar el llistat (stdout) segons el criteri login o el criteri 
  gid (estable).


# ----------------------------------------------

## Metodología Y APUNTES

CMP_TO_KEY

SORT()

	* Python es capaz de ordenar TUPLAS.
	
	* help(sort)
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

