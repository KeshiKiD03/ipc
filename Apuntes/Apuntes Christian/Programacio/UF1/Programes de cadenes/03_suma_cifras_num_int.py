#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes de cadenes
# Exercici3
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
# leer el int y calcular la suma de la cifras
numero = input()

# descartar el signo
primer_car = numero[0]
inicio = 0
if primer_car in '+-':  # if primer_car == '+' or primer_car == '-':
    inicio = 1

suma = 0
# por cada cifra
for pos in range(inicio,len(numero)):
    # sumar
    suma = suma + int(numero[pos])

print(suma)