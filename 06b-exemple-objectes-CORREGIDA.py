# /usr/bin/python3
#-*- coding: utf-8-*-
class UnixUser():
  """Classe UnixUser: prototipus de /etc/passwd login:passwd:uid:gid:gecos:home:shell"""

  def __init__(self, userLine):	
    "Constructor objectes UnixUser"
    userField=userLine.split(":")
    self.login=userField[0]
    self.passwd=userField[1]
    self.uid=int(userField[2])
    self.gid=int(userField[3])
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6][:-1]

  def show(self):
    "Mostra usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")

  def __str__(self):
    "Fa string de la instancia"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)

print("Programa")

user1=UnixUser("Pere:pere12:1000:100:pere:/home/pere:/bin/bash")
user1.show()
print(user1)




exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS


**06b-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.

# ----------------------------------------------

## Explicación


**06b-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.


# ----------------------------------------------

## Metodología

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

