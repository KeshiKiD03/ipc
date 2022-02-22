#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici26
# Cristian Fernando Condolo Jimenez
# 20/11/2020
# 
# Descripcion:
# Mostrar los num primos inferior de n.

# E.E. 1 int

# Juego de pruebas
# Entrada   Salida
# 

# Programa
# leer los datos
n = int(input())
div = 2

# bucle: comprobar si es primo o no
for d in range(div,n):
    es_primo = True
    if n % d == 0:
        es_primo = False
    # muestra los numeros primos
    if es_primo == True:
        print(d)
