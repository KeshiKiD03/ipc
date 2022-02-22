#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici25
# Cristian Fernando Condolo Jimenez
# 20/11/2020
# 
# Descripcion:
# Decir si el numero entero es primo o no.

# E.E. 1 int

# Juego de pruebas
# Entrada   Salida
# 2         T
# 11        T
# 4         F
# 12        F

# Programa
# leer los datos
n = int(input())

div = 2
es_primo = True
# bucle: comprobar si es primo o no
for d in range(div,n):
    if n % d == 0:
        es_primo = False 

# muestro si es o no
print(es_primo)
