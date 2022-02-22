#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes de cadenes
# Exercici3v2
# Cristian Fernando Condolo Jimenez
# isx41016667
# 18/12/2020
# 
# Descripcion:
# Hacer un programa que lea un numero entero y escriba la suma de sus cifras.

# Juego de pruebas
# Entrada   Salida
# num       suma
# 234       9
# 12345     14
# -23       5
# 0         0
# +1        1

# E.E. 1 numero str

# Programa
# leer el int
nombre = int(input())

#descartar el signo
if nombre < 0:
    nombre = -nombre
#por cada cifra
nombre_c = str(nombre)
suma = 0
for car in nombre_c:
    #sumamos
    suma = suma + int(car)
print(suma)
