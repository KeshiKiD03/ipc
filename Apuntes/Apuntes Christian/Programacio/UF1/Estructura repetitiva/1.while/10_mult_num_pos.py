#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici10
# Cristian Fernando Condolo Jimenez
# 19/11/2020
# 
# Descripcion:
# Multipica dos numeros enteros positivos en base sumas sucesivas

# Juego de pruebas
# Entrada       Salida
# 9     5       45
# 0     2       0

# E.E. 2 num int >= 0.

# Programa
n1 = int(input())
n2 = int(input())

i = 0
suma = 0
# bucle: multiplicacio base suma
while i < n1:
    # multiplica los dos numeros
    suma = suma + n1
    i = i + 1

# muestra el resultado de la multiplicacion
print(suma)