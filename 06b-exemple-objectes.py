# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n nlin] [-f file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
# Exemple de programació Objectes POO
# -------------------------------------
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
    self.bash=userField[6]
 
  def show(self):
    "Mostra les dades de l'usuari"
    
    print(f"login:")

    print(self.login)
    print(self.uid)
    print(self.gid)
    print
    print
    print
    print

  def __str__ (self):
    "Funció to string"
    return "%s %d %d " % (self.login, self.uid, self.gid)

print("Programa")

user1=UnixUser("pere",x,1000:100::/home/pere:/bin/bash")

user1.show()

print(user1)

exit(0)
