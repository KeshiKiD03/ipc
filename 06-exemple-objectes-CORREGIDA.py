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

**01-head.py [file]**
  
  Mostrar les deu primeres línies de file o stdin

# ----------------------------------------------

## Explicación

Mostrar les 10 primeres línies d'un fitxer. 
El nom del fitxer a mostrar es rep com a argument, sinó es rep, 

es mostren les deu primeres línies de  l'entrada estàndard. 

Sinpsys: $ head [file] 


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

