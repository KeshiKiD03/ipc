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

