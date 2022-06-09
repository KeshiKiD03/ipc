# /usr/bin/python
#-*- coding: utf-8-*-
#
# sort-users [-s login|gid]  file
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
groupDict={}
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
    self.gname=""
    if self.gid in groupDict:
      self.ganame=groupDict[self.gid].gname
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6][:-1]
  def show(self):
    "Mostra les dades de l'usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
  def __str__(self):
    "functió to_string"
    return "%s %s %d %d %s %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gname, self.gecos, self.home, self.shell)
class UnixGroup():
  """ Classe grup de unix: prototipus /etc/group
  gname:paswd:gid:listusers"""
  def __init__(self, groupLine):
    "constructor de un UnixGroup donada una línia del /etc/group"
    groupField = groupLine[:-1].split(":")
    self.gname = groupField[0]
    self.passwd = groupField[1]
    self.gid = int(groupField[2])
    self.userList = groupField[3]
  def __str__(self):
    "funció to_string"
    return "%s %s %d %s" %(self.gname, self.passwd, self.gid, self.userList)
# -------------------------------------------------------
def sort_login(user):
  '''Comparador d'usuaris segons el login'''
  return user.login
  
def sort_gid(user):
  '''Comparador d'usuaris segons el gid'''
  return (user.gid, user.login)
# -------------------------------------------------------
fileIn=open("group","r")
for line in fileIn:
  oneGroup=UnixGroup(line)
  groupDict[oneGroup.gid]=oneGroup
fileIn.close()
# -------------------------------------------------------
fileIn=open("passwd","r")
userList=[]
for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
print(userList[0])
exit(0)
# ---------------------------------------------------------
if args.criteria=="login":
  userList.sort(key=sort_login)
else:
  userList.sort(key=sort_gid)
for user in userList:
 print(user)
exit(0)

