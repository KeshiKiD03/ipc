# /usr/bin/python
#-*- coding: utf-8-*-
#
# gname-users [-s login|gid|gname] -u users -g groups
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------

# SE IMPLEMENTA ARGPARSE

import sys, argparse # Se llaman los módulos SYS y ARGPARSE
groupDict={} # Se crea un DICCIONARIO VACÍO
parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks") # Se llama ArgPARSE
parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: login | gid | gname", metavar="criteria",\
        choices=["login","gid","gname"],dest="criteria") # Argumento opcional CRITERIA con opciones LOGIN, GID o GNAME.
parser.add_argument("-u","--userFile",type=str,\
        help="user file (/etc/passwd style)", metavar="userFile",required=True)
parser.add_argument("-g","--groupFile",type=str,\
        help="user file (/etc/passwd style)", metavar="groupFile",required=True)
args=parser.parse_args()
# -------------------------------------------------------

# SE DEFINE UNA CLASE UNIXUSER

class UnixUser():
  """Classe UnixUser: prototipus de /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""
  def __init__(self,userLine):
    "Constructor objectes UnixUser"
    userField=userLine.split(":") # Hacemos el método split(":"), para que nos separe en : cada objeto.
    self.login=userField[0]
    self.passwd=userField[1]
    self.uid=int(userField[2])
    self.gid=int(userField[3])
    self.gname=""
    if self.gid in groupDict: # Si el gid está en groupDict
      self.gname=groupDict[self.gid].gname # Asigname la posición del diccionario en donde se encuentra el GID.
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6]
    
  def show(self):
    "Mostra les dades de l'usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
    
  def __str__(self):
    "functió to_string d'un objcete UnixUser"
    return "%s %s %d %d %s %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gname, self.gecos, self.home, self.shell)
# -------------------------------------------------------

# SE DEFINE UNA CLASE UNIXGROUP

class UnixGroup():
  """Classe UnixGroup: prototipus de /etc/group
  gname_passwd:gid:listUsers"""
  def __init__(self,groupLine):
    "Constructor objectes UnixGroup"
    groupField = groupLine.split(":")
    self.gname = groupField[0]
    self.passwd = groupField[1]
    self.gid = int(groupField[2])
    self.userListStr = groupField[3]
    self.userList=[]
    if self.userListStr[:-1]:
      self.userList = self.userListStr[:-1].split(",")
  def __str__(self):
    "functió to_string d'un objecte UnixGroup"
    return "%s %d %s" % (self.gname, int(self.gid), self.userList)
# -------------------------------------------------------
def sort_login(user):
  '''Comparador d'usuaris segons el login'''
  return user.login
def sort_gid(user):
  '''Comparador d'usuaris segons el gid'''
  return (user.gid, user.login)
def sort_gname(user):
  '''Comparador d'usuaris segons el gname'''
  return (user.gname, user.login)
# -------------------------------------------------------

# SE RECORRE EL GRUPO

groupFile=open(args.groupFile,"r")
for line in groupFile:
  group=UnixGroup(line)
  groupDict[group.gid]=group
groupFile.close()
# -------------------------------------------------------

# SE RECORREN LOS USUARIOS

userFile=open(args.userFile,"r")
userList=[]
for line in userFile:
  user=UnixUser(line)
  userList.append(user)
userFile.close()
# -------------------------------------------------------
if args.criteria=="login":
  userList.sort(key=sort_login)
elif args.criteria=="gid":
  userList.sort(key=sort_gid)
else:
  userList.sort(key=sort_gname)
for user in userList:
 print(user, end=" ")
exit(0)
