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
