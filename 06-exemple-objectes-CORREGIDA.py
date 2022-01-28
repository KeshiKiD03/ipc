# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n nlin] [-f file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
# Exemple de programació Objectes POO
# -------------------------------------
class UnixUser():
  """Classe UnixUser: prototipus de /etc/passwd login:passwd:uid:gid:gecos:home:shell"""
  
  def __init__(self, l, i, g):	
    "Constructor objectes UnixUser"
    self.login=l
    self.uid=i
    self.gid=g
 
  def show(self):
    print(self.login)
    print(self.uid)
    print(self.gid)

  def __str__ (self):
      return "%s %d %d " % (self.login, self.uid, self.gid)

print("Programa")

user1=UnixUser("pere",1000,100)

user1.show()

print(user1)

exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS


**06-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.

# ----------------------------------------------

## Explicación


**06-exemple-objectes.py**

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

