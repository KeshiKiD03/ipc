# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n nlin] [-f file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
# Exemple de programació Objectes POO
# -------------------------------------
class UnixUser(): # Usamos CLASES para definir nuevos TIPOS. Se usa para referirse a OBJETOS REALES. Crea un CONTENEDOR de diferentes FUNCIONES/TIPOS.
  """Classe UnixUser: prototipus de /etc/passwd login:passwd:uid:gid:gecos:home:shell"""
  
  def __init__(self, l, i, g): # Creamos un MAGIC METHOD de una CLASE. Permite INICIALIZAR nuestros OBJETOS. Es un CONSTRUCTOR.
  # INIT significa inicializar. Es la función o el método que es llamado cuando creamos nuevos POINT - OBJECT.
  # Self es el current object.
  # El resto son variables.
  # Es decir creará una caja en blanco y dentro almacenará 3 propiedades.
    "Constructor objectes UnixUser"
    self.login=l # Definimos variable LOGIN.
    self.uid=i # Definimos variable UID.
    self.gid=g # Definimos variable GID
 
  def show(self): # Definimos un nuevo TIPO/FUNCIÓN que será para MOSTRAR
    print(self.login) # Muestra LOGIN
    print(self.uid) # Muestra UID
    print(self.gid) # Muestra GID

  def __str__ (self): # Método especial que construyen un OBJETO a STRING.
  # Un método __str__(self) le dice a Python cómo mostrar la representación "string" de un objeto. Cuando creas una clase y le defines un método __str__(self)
  
  # Permite que el objeto sea más legible.
      return "%s %d %d " % (self.login, self.uid, self.gid) # Retorna los valores.

print("Programa")

user1=UnixUser("pere",1000,100) # Llamamos a la CLASE UnixUser y lo pasamos user1

user1.show() # Mostramos con la función definida.

print(user1) # Mostramos user1

exit(0)

"""

## NOMBRE DEL PROGRAMA + SINTAXIS


**06-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.

# ----------------------------------------------

## Explicación


**06-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.


# ----------------------------------------------

## Metodología Y APUNTES


## RESUMEN

* Usamos CLASES para definir NUEVOS TIPOS de OBJETOS. Estos **OBJETOS** poseen **MÉTODOS** que definen el cuerpo de **NUESTRA CLASE** y también pueden **ATRIBUTOS** donde se pueden introducir donde sea en **NUESTRO PROGRAMA**



## RECUERDA

### Una clase es un objeto real, este objeto real tiene métodos.

### En otras palabras, un objeto es una INSTANCIA de una CLASE, una simple CLASE define un contenedor o huella para CREAR OBJETOS.

### Los objetos son las actuales instancias basadas en ese CONTENEDOR.

### Los métodos son las ACCIONES o FUNCIONES que hará nuestra CLASE.








CONSTRUCTORES


Usamos un **CONSTRUCTOR**, un contructor es una función que es llamada al mismo tiempo que se **CREA** el **OBJETO**.

* **init method** --> Podemos inicializar nuestros objetos. __init__ Construye o crea objetos.

* Nos referimos a este método como **CONSTRUCTORES**


--------

Usamos un **CONSTRUCTOR**, un contructor es una función que es llamada al mismo tiempo que se **CREA** el **OBJETO**.

class Point:

	def __init__(self, x, y)
		self.x = x
		self.y = y

	def draw(self):
		print("Draw")

point = point(10, 20)
print(point.x)


* INIT significa inicializar. Es la función o el método que es llamado cuando creamos nuevos POINT - OBJECT.

* Self es el current object.

* Cuando creamos nuevos point object, self referencia el objeto en la memoria.

* El mismo objeto que usamos en esta variable. point = point(10, 20).

* point = 10 --> Con este código asigname que el atributo x de este "point object"

* Hay muchos constructores.

* **init method** --> Podemos inicializar nuestros objetos. __init__ Construye o crea objetos.

* Nos referimos a este método como **CONSTRUCTORES**







__STR__



Un método __str__(self) le dice a Python cómo mostrar la representación "string" de un objeto. Cuando creas una clase y le defines un método __str__(self), por ejemplo:

----
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
 
persona=Persona("Panchito","Gómez Toro")
print(persona)
---
Por ejemplo, imprime:
--
<__main__.Persona object at 0x0000020B0787CA20>
----



----
class Persona1:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido = apellido

    def __str__(self):
        return self.nombre + " " + self.apellido

persona1=Persona1("Panchito","Gómez Toro")
print(persona1)
--------


Imprime: Panchito Gómez Toro


--------------





W3SCHOOLS

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:





Note: The __init__() function is called automatically every time the class is being used to create a new object.


------------------------------------------------------







 Las ventajas de implementar el método __init__ en lugar del método inicializar son:

    El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
    El método __init__ se llama automáticamente. Es decir es imposible de olvidarse de llamarlo ya que se llamará automáticamente.
    Quien utiliza POO en Python (Programación Orientada a Objetos) conoce el objetivo de este método.

Otras características del método __init__ son:

    Se ejecuta inmediatamente luego de crear un objeto.
    El método __init__ no puede retornar dato.
    el método __init__ puede recibir parámetros que se utilizan normalmente para inicializar atributos.
    El método __init__ es un método opcional, de todos modos es muy común declararlo.




https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=44&codigo=44&inicio=30





TEORIA 12.01.22


Concepto de idea de ciertos objetos.

Conceptos básicos de programación orientada a objetos.

POO 


CLASES 

Una clase describe una idea.

Cuando construye una clase desde la informática, es una abstracción de la realidad, te quedas con los datos que realmente quieres.

Tendrá unas PROPIEDADES y unos MÉTODOS.


UNIXUSER

Cual es su UID, GID, 

Las propiedades son variables de una entidad. 

La edad de un arbol es una propiedad, la altura del arbol es una propiedad.




Cuando un programador diseña una base, selecciona que propiedades debe tener en cuanto a la clase definida.



MÉTODOS son acciones que realizamos, o sea funciones.

Una acción es subirse, frenar, pedalear.



VARIABLES

FUNCIONES





~
-

Un CONSTRUCTOR, permite crear objetos.

En caso de Python el contructor es __init__ --> ES OBLIGATORIO DEFINIRLA

def = Método


Método __str__ --> La manera de representar un objeto en un string. Construeix l'objecte a string.




Una idea es una clase.

A traves del constructor, creamos objetos , los objetos se le llaman INSTANCIAS.

Un objeto es una "caja"



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

