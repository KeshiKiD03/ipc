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


"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**09-gname-users.py   [-s login|gid|gname]  -u fileusers -g fileGroup**

  Carregar en una llista a memòria els usuaris provinents d'un fitxer tipus
  /etc/passwd, usant objectes UnixUser, i llistar-los. Ordenar el llistat
  (stdout) segons el criteri login o el criteri gid o el gname.
 
   Requeriments: primer carregar a un diccionari totes les dades de tots
   els grups. Després carregar a una llista totes les dades dels usuaris.
   Finalment ordenar i llistar.

# ----------------------------------------------

## Explicación

**09-gname-users.py   [-s login|gid|gname]  -u fileusers -g fileGroup**

  Carregar en una llista a memòria els usuaris provinents d'un fitxer tipus
  /etc/passwd, usant objectes UnixUser, i llistar-los. Ordenar el llistat
  (stdout) segons el criteri login o el criteri gid o el gname.
 
   Requeriments: primer carregar a un diccionari totes les dades de tots
   els grups. Després carregar a una llista totes les dades dels usuaris.
   Finalment ordenar i llistar.


# ----------------------------------------------

## Metodología y apuntes

1. Se lee el /etc/group

1.2 Se añadirá a un DICCIONARIO (CAJA GRUPO)

1.2 Luego carga el /etc/passwd

1.3 Se añadirá a un LISTA VACÍA (CAJA USUARIOS)

2. Para cada línea DEL GRUPO, se crea un objeto a UnixGroup. 

2.1 Para cada línea DEL USUARIO, se crea un objeto a UnixUser. 

3. Hay que hacer un bucle/iterar para que cargue en memoria todos los grupos. 

4. Después lo carga en una lista de usuarios.

5. La relación es que hay un GID y apunta a /etc/group.

6. Se crea un diccionario y se carga.

7. Se crea una caja llamada UnixGroup.

8. Se añaden todos los grupos en un diccionario.

9. $GID

10. Se añaden todos los usuarios en una lista.

11. Se hace un head /etc/group > minigroup.txt

12. groupFile=open(args.groupFile,"r") ES COMO groupFile=open("minigroup.txt","r")

13. Se lee linea a linea en groupFile -

# linia=groupFile.readline()
>>> linia
'root:x:0:\n'
>>> 

14.

# >>> group1=UnixGroup(linia)
>>> group1
<__main__.UnixGroup object at 0x7feabf97a610>
>>> 


Se lee cada una de las partes del Diccionario de groupDict


# >>> print(group1)
root 0 []
>>> 

# group1.gname

'root'

# group1.passwd

'x'

# group1.gid

0




# groupDict[group1.gid]=group1 

fort line in groupFile:

	group=UnixGroup
	
	
	
	
	
groupdict[O]



# print(groupdict[2])

pin 2 []

>>> groupDict[2]




################### EJERCICIO #################



EXERCICI PER FER: 

# DICCIONARI DE GRUPS, USUARIS


# DICCIONARI DE USUARIOS QUE ESTÁN EN UNA LISTA

# DICCIONARI DE GRUPOS QUE ESTÁN EN UN DICCIONARIO


# ORDENAR POR LOGIN

# COGER LA LISTA Y PONERLE UN SORT

# USUARIOS ORDENADOS POR GIT

# USUARIOS ORDENADOS POR GNAME






# GRUPOS ORDENADOS POR NUMERO DE USUARIOS POR NUMERO DE USUARIOS QUE PERTENECEN AL GRUPO. 

# DENTRO DE UN OBJETO HAY UNA LISTA

# LISTA.LENGTH

# RECORRER EL DICCIONARI DE GRUPS (FOR K IN D) // OBLIGADOS A FABRICAR UN INDEX (CRITERI D[][length], CLAU (K))

# SORT


# PROBLEMA /ETC/GROUPS --> SON USUARIOS SECUNDARIOS, APARECEN LOS PRINCIPALES.



# MODIFICAR EL PROGRAMA


# CADA VEZ QUE LEE UN USUARIO --> LO METE EN UNA CAJA [DICCIONARIO] --> AÑADIR (PERE) A LA LISTA DE USUARIOS QUE HAY EN EL GRUPO.

# CARGAR PRIMERO LOS GRUPOS

# CARGAR LOS USUARIOS --> OBTENER EL GNAME. 


# RECOGIDA DE DATOS Y LUEGO PROCESAR LOS DATOS.

SABER GENERAR UN DICCIONARIO (INDEX) Y PINTARLO.

# IF DE PROTECCIÓ




########################## APUNTES ############################


# TYPE

type(d)
<class 'dict'>

type (d['A077'])
<class 'tuple'>

type (d['A077'][1])
<class 'int'>

type (d['A077'][2])
<class 'str'>

type (d['A077'][2])
<class 'str'>


# LISTAS

# DICCIONARIOS

* Almacenan "Par de claves"/Índices y Listas o Tuplas.

* d.keys() --> Llaves es igual a 

    for clave in d:

        print(clave, d[clave])

## Es una lista de todas las claves de todos los diccionarios

>>> d.keys()
dict_keys(['A077', 'A011', 'A012', 'A013', 'B002', 'A001', 'A004', 'B004', 'B007', 'A003', 'A002', 'B015', 'A020', 'B011'])
>>> 


## Mostrar los valores de las llaves.

for v in d.values():
...     print(v)
... 
('pau puig', 9, 'barcelona')
('jan', 11, 'Girona')
('julia', 17, 'Barcelona')
('josep', 18, 'Vic')
('josep', 18, 'Girona')
('pere', 18, 'Lleida')
('pere', 18, 'Lleida')
('ricard', 18, 'Barcelona')
('ricard', 18, 'Barcelona')
('anna', 19, 'Girona')
('marta', 20, 'Vic')
('ramon', 34, 'Barcelona')
('josep', 50, 'Sidney')
('anna', 48, 'Barcelona')
>>> 


## values() --> Muestra el valor, retorna una lista con todos los valores.



## Muestra los ítems

>>> for k in d: 
...     print(k, d[k][0], d[k][1], d[k][2])


# --------------------

# Recorre listas

# Llistar el diccionari per ordre de clau

## El diccionari no es pot ordenar,

## Hay que ordenar las llaves.


>>> d.keys()
dict_keys(['A077', 'A011', 'A012', 'A013', 'B002', 'A001', 'A004', 'B004', 'B007', 'A003', 'A002', 'B015', 'A020', 'B011'])
>>> 



1. Se genera un índice


2. index=d.keys()

3. index.sort() --> Da error porque es un diccionario de valores "pair keys" y no retorna una lista.

4. Hay que convertirlo en UNA LISTA

5. index=list(d.keys())

6. type(index)

<class 'list'>

7. index.sort()

8. index

9. >>> index
['A001', 'A002', 'A003', 'A004', 'A011', 'A012', 'A013', 'A020', 'A077', 'B002', 'B004', 'B007', 'B011', 'B015']
>>> 




10. Ya podemos recorrer por ORDEN


>>> for k in index:
...     print(k,d[k])
... 
A001 ('pere', 18, 'Lleida')
A002 ('marta', 20, 'Vic')
A003 ('anna', 19, 'Girona')
A004 ('pere', 18, 'Lleida')
A011 ('jan', 11, 'Girona')
A012 ('julia', 17, 'Barcelona')
A013 ('josep', 18, 'Vic')
A020 ('josep', 50, 'Sidney')
A077 ('pau puig', 9, 'barcelona')
B002 ('josep', 18, 'Girona')
B004 ('ricard', 18, 'Barcelona')
B007 ('ricard', 18, 'Barcelona')
B011 ('anna', 48, 'Barcelona')
B015 ('ramon', 34, 'Barcelona')
>>> 


# Se convierte un diccionario en un indice (lista) y se ordena con el .sort()

# Se recorre la lista y se printa.


>>> for k in index:
...     print(k,d[k])
... 
A001 ('pere', 18, 'Lleida')
A002 ('marta', 20, 'Vic')
A003 ('anna', 19, 'Girona')
A004 ('pere', 18, 'Lleida')
A011 ('jan', 11, 'Girona')
A012 ('julia', 17, 'Barcelona')
A013 ('josep', 18, 'Vic')
A020 ('josep', 50, 'Sidney')
A077 ('pau puig', 9, 'barcelona')
B002 ('josep', 18, 'Girona')
B004 ('ricard', 18, 'Barcelona')
B007 ('ricard', 18, 'Barcelona')
B011 ('anna', 48, 'Barcelona')
B015 ('ramon', 34, 'Barcelona')
>>> 





## CHEAT SHEET

# Conservar el nombre y la clave.

# Index de un libro, es una clau.

# Agafa los valores de la llave, los mete en una lista y printa las claves.

# Un indice de un libro es un criterio [INDEX] --> Necesita el número de páginas [ADREÇAMENT]

# Tienen el criterio, CRITERIO --> DNI --> 

# NOM AUTOR E ISBN --> 

# INDEX : 2 COLUMNES (CRITERI) I EL ADREÇAMENT.

# Per recorrer tot el diccionari.

index=[]

# for k in d:

# Per cada element del diccionari tindrá una tupla.


>>> index=[]
>>> for k in d:
...     t=(d[k][1],k) 

# k es la clave # son enteros, desempata con la clave, es un campo único. No se ordena nada que no se desempate ## no se define ningun criterio. S'ha de definir un criteri, ordenació inestable.

# Criteri de comparació, sempre hi haurà algo que desempati, un camp clau

# index.append(t)


# Llistar el diccionari ordenat per edat




>>> index=[]
>>> for k in d:
...     t=(d[k][1],k)
...     index.append(t)
... 
>>> index
[(9, 'A077'), (11, 'A011'), (17, 'A012'), (18, 'A013'), (18, 'B002'), (18, 'A001'), (18, 'A004'), (18, 'B004'), (18, 'B007'), (19, 'A003'), (20, 'A002'), (34, 'B015'), (50, 'A020'), (48, 'B011')]
>>> 





















# k es la tupla

>>> for e,k --> e es la edad, k es la clau.




>>> for e,k in index:
...     print(d[k])
... 
('pau puig', 9, 'barcelona')
('jan', 11, 'Girona')
('julia', 17, 'Barcelona')
('josep', 18, 'Vic')
('josep', 18, 'Girona')
('pere', 18, 'Lleida')
('pere', 18, 'Lleida')
('ricard', 18, 'Barcelona')
('ricard', 18, 'Barcelona')
('anna', 19, 'Girona')
('marta', 20, 'Vic')
('ramon', 34, 'Barcelona')
('josep', 50, 'Sidney')
('anna', 48, 'Barcelona')
>>> 



# Me quedo con el campo que me interesa + llaves --> generamos un INDEX.

# Un index es una lista donde tenemos tuplas.

# Tuplas contiene CRITERIOS y la CLAVE.


INDEX [(criteri,clau),(...)...]

# Desempatat per KEYs





























# LIST COMPRESSION

>>> l=[2,6,3,8,9,1,20]
>>> l
[2, 6, 3, 8, 9, 1, 20]
>>> 


# Fabricar una lista L1

>>> l1=[]
>>> for e in l:
...     l1.append(2*e)
... 
>>> l1
[4, 12, 6, 16, 18, 2, 40]
>>> 





>>> l1=l1*2
>>> l1
[4, 12, 6, 16, 18, 2, 40, 4, 12, 6, 16, 18, 2, 40]
>>> 

Lo lista 2 veces












l1=[2*e for e in l]

l1

>>> l1
[4, 12, 6, 16, 18, 2, 40]
>>> 


l1=[(e,2*e) for e in l] --> Lista de tuplas

l1

>>> l1
[(2, 4), (6, 12), (3, 6), (8, 16), (9, 18), (1, 2), (20, 40)]
>>> 



l2=[ (segon,primer) for primer,segon in l1]

# List compression para generar índices.


>>> l2
[(4, 2), (12, 6), (6, 3), (16, 8), (18, 9), (2, 1), (40, 20)]
>>> 



# for k in d --> Se recorrer todo el diccionario

edat = d[k][1]

# index=[ (d[k][1],k) for k in d]




# DICCIONARI ES UN ELEMENT

# EDAT I LA CLAU




>>> index=[ (d[k][1],k) for k in d]

>>> index
[(9, 'A077'), (11, 'A011'), (17, 'A012'), (18, 'A013'), (18, 'B002'), (18, 'A001'), (18, 'A004'), (18, 'B004'), (18, 'B007'), (19, 'A003'), (20, 'A002'), (34, 'B015'), (50, 'A020'), (48, 'B011')]
>>> 

# Index.


>>> index=[ (d[k][2],d[k][1],k) for k in d]
>>> index
[('barcelona', 9, 'A077'), ('Girona', 11, 'A011'), ('Barcelona', 17, 'A012'), ('Vic', 18, 'A013'), ('Girona', 18, 'B002'), ('Lleida', 18, 'A001'), ('Lleida', 18, 'A004'), ('Barcelona', 18, 'B004'), ('Barcelona', 18, 'B007'), ('Girona', 19, 'A003'), ('Vic', 20, 'A002'), ('Barcelona', 34, 'B015'), ('Sidney', 50, 'A020'), ('Barcelona', 48, 'B011')]
>>> 




index.sort() --> Ordena


>>> index.sort()
>>> for x,y,k in index:
...     print(k,d[k])
... 
A012 ('julia', 17, 'Barcelona')
B004 ('ricard', 18, 'Barcelona')
B007 ('ricard', 18, 'Barcelona')
B015 ('ramon', 34, 'Barcelona')
B011 ('anna', 48, 'Barcelona')
A011 ('jan', 11, 'Girona')
B002 ('josep', 18, 'Girona')
A003 ('anna', 19, 'Girona')
A001 ('pere', 18, 'Lleida')
A004 ('pere', 18, 'Lleida')
A020 ('josep', 50, 'Sidney')
A013 ('josep', 18, 'Vic')
A002 ('marta', 20, 'Vic')
A077 ('pau puig', 9, 'barcelona')
>>> 



	
	# DESEMPATATS PER COGNOM I CLAU
	
	
Filtrar de dades

l2=[ (a,b) for a,b in l1 if b>5]

l2






l2=[ a+b for a,b in l1]

l2



>>> l2=[ a+b for a,b in l1]
>>> l2
[6, 18, 9, 24, 27, 3, 60]
>>> 



"""

