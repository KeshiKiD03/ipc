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
