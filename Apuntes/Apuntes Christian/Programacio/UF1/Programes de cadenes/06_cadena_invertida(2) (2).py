#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes de cadenes
# Exercici6v2
# Cristian Fernando Condolo Jimenez
# isx41016667
# 18/12/2020
# 
# Descripcion:
# Invertir el valor de una cadena.

# Juego de pruebas
# Entrada   Salida
# num       suma
# 

# E.E. 1 numero str

# Programa
cadena = input()

cadena_nueva = ''
for pos in range(len(cadena) - 1,-1,-1):
    cadena_nueva = cadena_nueva + cadena[pos]

print(cadena_nueva)