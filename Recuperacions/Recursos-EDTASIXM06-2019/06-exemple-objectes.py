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
  """Classe UnixUser: prototipus de 
  /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""
  def __init__(self, l, i, g):	
    "Constructor objectes UnixUser"
    self.login=l
    self.uid=i
    self.gid=g
  def show(self):
    "Mostrar les dades de l'usuari"
    print("login:%s uid: %d gid:%d" % (self.login, self.uid, self.gid))
  def sumaun(self):
	self.uid+=1
  def __str__(self):
	"Funció per retornar un string del objecte"
	return "%s %d %d" % (self.login, self.uid, self.gid)
exit(0)


