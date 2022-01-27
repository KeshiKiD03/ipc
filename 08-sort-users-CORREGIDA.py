# /usr/bin/python
#-*- coding: utf-8-*-
#
# sort-users [-s login|gid]  file
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
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
def sort_login(user):
  '''Comparador d'usuaris segons el login'''
  return user.login
  
def sort_gid(user):
  '''Comparador d'usuaris segons el gid'''
  return (user.gid, user.login)
# -------------------------------------------------------
fileIn=open(args.fitxer,"r")
userList=[]
for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
if args.criteria=="login":
  userList.sort(key=sort_login)
else:
  userList.sort(key=sort_gid)
for user in userList:
 print(user)
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

