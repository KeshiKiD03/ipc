#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici7
# Cristian Fernando Condolo Jimenez
# 17/11/2020
# 
# Descripcion:
# Sumar las potencias de dos menores de 100.

# Programa
# leer los datos
potencia = 1
suma = 2

# bucle: sumar las potencias de dos
while suma < 100:
    resultado = 2 ** potencia
    print(resultado)
    suma = suma + resultado
    potencia = potencia + 1 

# mostrar la suma de los multiplos de dos
print(suma)