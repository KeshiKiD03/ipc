# /usr/bin/python
#-*- coding: utf-8-*-
#
# sort-users [-s login|gid]  file
# ***usa cmps com es feia en python2 ***
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
from functools import cmp_to_key
parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks")
parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: login | gid", metavar="criteria",\
        choices=["login","gid"],dest="criteria",default="login")
parser.add_argument("fitxer",type=str,\
        help="user file (/etc/passwd style)", metavar="file")
args=parser.parse_args()
# -------------------------------------------------------
class UnixUser():
  """Classe UnixUser: prototipus de /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""
  def __init__(self,userLine):
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
    "Mostra les dades de l'usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
  def __str__(self):
    "functió to_string"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
# -------------------------------------------------------
def cmp_login(a,b):
  '''Comparador d'usuaris segons el login'''
  if a.login > b.login:
    return 1
  if a.login < b.login:
    return -1
  return 0

def cmp_gid(a,b):
  '''Comparador d'usuaris segons el gid'''
  if a.gid > b.gid:
    return 1
  if a.gid < b.gid:
    return -1
  if a.login > b.login:
    return 1
  if a.login < b.login:
    return -1
  return 0

# -------------------------------------------------------
fileIn=open(args.fitxer,"r")
userList=[]
for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
if args.criteria=="login":
  userList.sort(key=cmp_to_key(cmp_login), reverse=False)
else:
  userList.sort(key=cmp_gid)
for user in userList:
 print(user)
exit(0)

