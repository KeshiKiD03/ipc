#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes amb while
# Exercici1
# Cristian Fernando Condolo Jimenez
# 16/11/2020
# 
# Descripcion:
# Escribir los multiplos de dos menors o iguals a 100
#
# E.E.

# Programa
# leer los datos
multiplo = 1

# bucle: mostrar los multiplos de 2
while multiplo <= 100:
    # buscar los multiplos de 2
    if multiplo % 2 == 0:
        print(multiplo)
    multiplo = multiplo + 1 