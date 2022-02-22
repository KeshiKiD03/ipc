#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici14
# Cristian Fernando Condolo Jimenez
# 20/11/2020
# 
# Descripcion:
# Calcula la tabla de multiplicar de un numero entero entre 1 y 9.

# E.E. 1 int >= 1 y <= 9

# Programa
# leer el numero entero
n = int(input())

i = 1
# bucle: tabla de multiplicacio de n
while i <= 10:
    resultado = n * i
    print(n,'x',i,'=',resultado)
    i = i + 1