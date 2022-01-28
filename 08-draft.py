# /usr/bin/python
#-*- coding: utf-8-*-
#
# list-users [-f file]
# 10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, argparse
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
# ------------------------------------------------------
def sort_login(user):
  '''comparador d'usuaris pert login'''
  return user.login
# -------------------------------------------------------
fileIn=open(args.fitxer,"r")
userList=[]
for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
# ----------------------------
userList.sort(key=sort_login)

# ----------------------------
for user in userList:
 print(user)
exit(0)

