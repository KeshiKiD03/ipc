#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes amb while
# Exercici2
# Cristian Fernando Condolo Jimenez
# 16/11/2020
# 
# Descripcion:
# Escribir los 10 primeros multiplos de dos
#
# E.E.

# Programa
# leer los datos
multiplo = 1
cont = 0

# bucle: mostrar los multiplos de 2
while cont < 10:
    # buscar los multiplos de dos
    if multiplo % 2 == 0:
        print(multiplo)
        cont = cont + 1
        multiplo = multiplo + 1
    else:
        multiplo = multiplo + 1