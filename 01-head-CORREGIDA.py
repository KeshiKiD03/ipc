# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys

"""
  
  * Se importa una LIBRERÍA "sys".

"""

MAXLIN=10

"""
  
  * Se define una CONSTANTE que vale 10.

  * Se definen en mayúsculas.


"""
fileIn=sys.stdin

"""
  
  * fileIn es stdin, una entrada estándar.

  * Dentro de la LIBRERÍA sys, hay una FUNCIÓN llamada "stdin".

"""
if len(sys.argv)==2:
  fileIn=open(sys.argv[1],"r")
counter=0

"""
  
  * Si el NÚMERO DE ARGUMENTOS es igual a == 2

  * SYS.argv es un array(vector) que contiene la LLAMADA del PROGRAMA.

  * El fichero a procesar es fileIn --> el Argumento sub 1 y se hace read, write y append.

  * [fileIn apunta a un flujo de entrada]

  * [Establecer un contador]

"""
for line in fileIn:
  counter+=1
  print (line, end="")

  """
  
  * [Llegir linia a linia]

  * [Incrementa el contador]

  * [Cuando printa una linea no la salta, end es un valor interno de print que termina con espacio]
  


  """
  if counter==MAXLIN: break

  """
  
  * [Cuando el contador se llena hace un BREAK, salta]

  * hexdump -C 01-head.py

  """
fileIn.close()

"""
  
  * Cerramos el fichero.

"""
exit(0)



"""

## NOMBRE DEL PROGRAMA + SINTAXIS

**01-head.py [file]**
  
  Programa que mostra deu primeres línies de file o stdin

# ----------------------------------------------

## Explicación

Mostrar les 10 primeres línies d'un fitxer. 
El nom del fitxer a mostrar es rep com a argument, sinó es rep, 

es mostren les deu primeres línies de  l'entrada estàndard. 

Sinpsys: $ head [file] 


# ----------------------------------------------

## SOLUCIÓN

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
