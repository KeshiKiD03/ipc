#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici6
# Cristian Fernando Condolo Jimenez
# 17/11/2020
# 
# Descripcion:
# Sumar los multiplos de dos menores de 100.

# Programa
# leer los datos
multiplo = 1
suma = 0

# bucle: sumar los multiplos de dos
while multiplo < 100:
    # buscar los multiplos de dos
    if multiplo % 2 == 0:
        suma = suma + multiplo
    multiplo = multiplo + 1

# mostrar la suma de los multiplos de dos
print(suma)