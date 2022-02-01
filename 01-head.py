# /usr/bin/python
#-*- coding: utf-8-*-
#
# PROGRAMA QUE LE 10 LINEAS
# 
# head [file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2022
# -------------------------------------
import sys # Importamos librería de SYS
MAXLIN=10 # Definimos una CONSTANTE MAXLIN de 10 Líneas.
fileIn=sys.stdin # En la variable fileIn, definimos que dentro de la librería SYS, sea stdin = entrada estándar.
if len(sys.argv)==2: # Si el número de argumentos es 2
  fileIn=open(sys.argv[1],"r") # Abreme el argumento 1 en modo read.
counter=0 # Establecemos un contador
for line in fileIn: # Recorremos cada línea en fileIn
  counter+=1 # Aumentamos el contador
  print (line, end="") # Printamos cada línea y un salto de línea.
  if counter==MAXLIN: break # Si el contador alcanza el MAXLIN, hace un break.
fileIn.close()
exit(0)



