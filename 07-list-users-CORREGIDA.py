# /usr/bin/python
#-*- coding: utf-8-*-
#
# list-users [-f file]
# 10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks")
parser.add_argument("-f","--fit",type=str,\
        help="user file or stdin (/etc/passwd style)", metavar="file",\
        default="/dev/stdin",dest="fitxer")
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
fileIn=open(args.fitxer,"r")
userList=[]
for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
for user in userList:
 print(user)
exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**07-list-users.py   [-f file]**

  Donat un file tipus /etc/passwd o stdin (amb aquest format) fer:
  * el constructor d'objectes *UnixUser* rep un strg amb la línia sencera 
    tipus /etc/passwd.
  * llegir línia a línia cada usuari assignant-lo a un objecte 
    UnixUser i afegir l’usuari a una llista d’usuaris UnixUser.
  * un cop completada la carrega de dades i amb la llista amb 
    tots els usuaris, llistar per pantalla els usuaris recorrent la llista.

# ----------------------------------------------

## Explicación

**07-list-users.py   [-f file]**

  Donat un file tipus /etc/passwd o stdin (amb aquest format) fer:
  * el constructor d'objectes *UnixUser* rep un strg amb la línia sencera 
    tipus /etc/passwd.
  * llegir línia a línia cada usuari assignant-lo a un objecte 
    UnixUser i afegir l’usuari a una llista d’usuaris UnixUser.
  * un cop completada la carrega de dades i amb la llista amb 
    tots els usuaris, llistar per pantalla els usuaris recorrent la llista.

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

