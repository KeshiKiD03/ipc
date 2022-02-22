#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes amb while
# Exercici3
# Cristian Fernando Condolo Jimenez
# 16/11/2020
# 
# Descripcion:
# Escribir los n primeros multiplos de m.
#
# E.E.

# Programa
# leer los datos m y n
cont = 0
multiplo = 1
m = int(input())
n = int(input())

# bucle: mostrar los n primero multiplos
while cont < n:
    # buscar los multiplos de m
    if multiplo % m == 0:
        print(multiplo)
        cont = cont + 1
        multiplo = multiplo + 1
    else:
        multiplo = multiplo + 1