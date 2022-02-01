# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n nlin] [-f file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
# Exemple de programació Objectes POO v2
# -------------------------------------
class UnixUser(): # Usamos CLASES para definir nuevos TIPOS. Se usa para referirse a OBJETOS REALES. Crea un CONTENEDOR de diferentes FUNCIONES/TIPOS.
  """Classe UnixUser: prototipus de /etc/passwd login:passwd:uid:gid:gecos:home:shell"""

  def __init__(self, userLine): # Creamos un MAGIC METHOD de una CLASE. Permite INICIALIZAR nuestros OBJETOS. Es un CONSTRUCTOR.
  # INIT significa inicializar. Es la función o el método que es llamado cuando creamos nuevos POINT - OBJECT.
  # Es decir creará una caja en blanco y dentro almacenará 1 propiedad.
  # Definimos una variable que nos devolverá la línea de Usuario
    "Constructor objectes UnixUser"
    userField=userLine.split(":") # Hacemos el método split(":"), para que nos separe en : cada objeto.
    self.login=userField[0] # Cogemos los datos de la primera posición y la colocamos en LOGIN
    self.passwd=userField[1] # Cogemos los datos de la segunda posición y la colocamos PASSWD 
    self.uid=int(userField[2]) # ...
    self.gid=int(userField[3])
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6][:-1]

  def show(self): # Definimos un nuevo TIPO/FUNCIÓN que será para MOSTRAR
    "Mostra usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}") # Usamos FORMATTED STRINGS para que nos muestre el resultado de cada variable.

  def __str__(self):
    "Fa string de la instancia"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
    
    # Es importante definir el Método Especial __str__(self) ya que nos resultará más legible a la hora de hacer print en lugar de mostrarnos algo así: print(user1) --> "<__main__.UnixUser object at 0x7f35bcfb6fd0>"
    


print("Programa")

user1=UnixUser("Pere:pere12:1000:100:pere:/home/pere:/bin/bash")
user1.show()
print(user1)

# Muestra el resultado,

# 1. Le pasamos Parámetros a la CLASE.

# 2. Llamamos a la función de SHOW()

# 3. Mostramos user1().




exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS


**06b-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.

# ----------------------------------------------

## Explicación


**06b-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.


# ----------------------------------------------

## Metodología y apuntes

EL USO DEL MAGIC METHOD __STR__(SELF)


    	FINALMENTE QUEDARÍA ASÍ


	  def __str__ (self):
	      return "%s %d %d " % (self.login, self.uid, self.gid)

	print("Programa")

	user1=UnixUser("pere",1000,100)

	user1.show()

	print(user1)

	exit(0)






	VERIFIACIÓN



	isx36579183@i11:~/Documents/ipc$ python3 06-exemple-objectes.py 
	Programa
	pere
	1000
	100
	pere 1000 100 
    





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

