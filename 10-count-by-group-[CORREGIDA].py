# /usr/bin/python
#-*- coding: utf-8-*-
#
# count-by-group.py [-s gid|gname|nusers] -u users -g groups
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys, argparse
parser = argparse.ArgumentParser(description=\
        """Count-by-users.py llistat de grups per gid, gname o nusers""",
        epilog="thats all folks")
parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: gid | gname | nusers", metavar="criteria",\
        choices=["gid","gname","nusers"],dest="criteria")
parser.add_argument("userFile",type=str,\
        help="user file (/etc/passwd style)", metavar="userFile")
parser.add_argument("groupFile",type=str,\
        help="user file (/etc/passwd style)", metavar="groupFile")
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
      self.gname=groupDict[self.gid].gname
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6]
  def __str__(self):
    "functió to_string d'un objcete UnixUser"
    return "%s %s %d %d %s %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gname, self.gecos, self.home, self.shell)
# -------------------------------------------------------
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
groupDict={}
groupFile=open(args.groupFile,"r")
for line in groupFile:
  group=UnixGroup(line)
  groupDict[group.gid]=group
groupFile.close()
# ---------------------------------
userFile=open(args.userFile,"r")
userList=[]
for line in userFile:
  user=UnixUser(line)
  userList.append(user)
  if user.gid in groupDict:
    if user.login not in groupDict[user.gid].userList:
      groupDict[user.gid].userList.append(user.login)
userFile.close()
# ---------------------------------
index=[]
if args.criteria=="gname":
  index = [ (groupDict[k].gname,k) for k in groupDict ]
elif args.criteria=="nusers":
  index = [ (len(groupDict[k].userList),k) for k in groupDict ]
else:
  index = [ k for k in groupDict ]
index.sort()

if args.criteria=="gname" or args.criteria=="nusers":
  for g,k in index:
   print(groupDict[k])
else:
  for k in index:
   print(groupDict[k])	
exit(0)


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**10-count-by-group.py [-s gid | gname | nusers ] -u usuaris -g grups**

  LListar els grups del sistema ordenats pel criteri de gname, gid o de 
  número d'usuaris.
  *Atenció* cal gestionar apropiadament la duplicitat dels usuaris en un grup.
  Requeriment: desar a la llista d'usuaris del grup tots aquells usuaris
  que hi pertanyin, sense duplicitats, tant com a grup principal com a 
  grup secundari.

# ----------------------------------------------

## Explicación

**10-count-by-group.py [-s gid | gname | nusers ] -u usuaris -g grups**

  LListar els grups del sistema ordenats pel criteri de gname, gid o de 
  número d'usuaris.
  *Atenció* cal gestionar apropiadament la duplicitat dels usuaris en un grup.
  Requeriment: desar a la llista d'usuaris del grup tots aquells usuaris
  que hi pertanyin, sense duplicitats, tant com a grup principal com a 
  grup secundari.


# ----------------------------------------------

## Metodología

1. # Definir un diccionario y hacer un OPEN.

2. Abrir python3

isx36579183@i11:~/Documents/ipc$ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> class UnixUser():
...   Classe UnixUser: prototipus de /etc/passwd
...   login:passwd:uid:gid:gecos:home:shell
...   def __init__(self,userLine):
...     "Constructor objectes UnixUser"
...     userField=userLine.split(":")
...     self.login=userField[0]
...     self.passwd=userField[1]
...     self.uid=int(userField[2])
...     self.gid=int(userField[3])
...     self.gname=""
...     if self.gid in groupDict:
...       self.gname=groupDict[self.gid].gname
...     self.gecos=userField[4]
...     self.home=userField[5]
...     self.shell=userField[6]
...   def __str__(self):
...     "functió to_string d'un objcete UnixUser"
...     return "%s %s %d %d %s %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gname, self.gecos, self.home, self.shell)
... 


>>> class UnixGroup():
...   """Classe UnixGroup: prototipus de /etc/group
...   gname_passwd:gid:listUsers"""
...   def __init__(self,groupLine):
...     "Constructor objectes UnixGroup"
...     groupField = groupLine.split(":")
...     self.gname = groupField[0]
...     self.passwd = groupField[1]
...     self.gid = int(groupField[2])
...     self.userListStr = groupField[3]
...     self.userList=[]
...     if self.userListStr[:-1]:
...       self.userList = self.userListStr[:-1].split(",")
...   def __str__(self):
...     "functió to_string d'un objecte UnixGroup"
...     return "%s %d %s" % (self.gname, int(self.gid), self.userList)
... 
>>> groupDict={}
>>> 
>>> groupFile=open("group","r")
>>> for line in groupFile:
...   group=UnixGroup(line)
...   groupDict[group.gid]=group
... 
>>> group


>>> groupDict[100]
<__main__.UnixGroup object at 0x7fbd0dbd1970>
>>> 




# si no estan añadelos




# Si root está dado de alta en el DICCIONARO, sino lo añades al diccionario.



>>> print(userList[0])
root x 0 0 root root /root /bin/bash

>>> 



3. # Ordenación de las llaves.


>>> index=list(groupDict.keys())
>>> index.sort()
>>> index
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 20, 21, 22, 24, 25, 26, 27, 29, 30, 33, 34, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 50, 60, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 998, 999, 1000, 1001, 64055, 65534]
>>> 




4. Generar un ÍNDICE.

index=[ (groupDict[k].gname, k) for k in groupdict]


# Para cada GID del Diccionario,

# Es un objeto



index

[('root', 0), ('daemon', 1), ('bin, 2')]

index.sort() --> Ordena

index





for g,k in index:
	print(groupDict[k])


	
# Printará todas las entradas según las [K]






# Ordenar según el número de USUARIOS.

# Fabricar un índice de un valor calculable

index=[ (len(groupDict[k].userList), k) for k in groupDict]

index.sort()

for g,k in index:
	print(groupDict[k])
	








# Tuplas
	
# List compressions

# Generar listas a partir de diccionarios.





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

