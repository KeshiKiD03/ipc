#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes de llistes
# Exercici1
# Cristian Fernando Condolo Jimenez
# isx41016667
# 12/02/2021
# 
# Descripcion:
# Hacer un programa que reciba un seguido de numeros enteros por argumento i nos diga
# quien es el maximo y en que posicion se encuentra.

# Juego de pruebas
# Entrada               Salida
# 3 5 7 12 2 -4 12 4    12, 3
# 1 1 1 1 1 1 1 1 1     1, 0


# E.E. nums int 

# Programa
import sys

# leer los numeros por argumento
lista = sys.argv[1:]

# pasar la lista de cadenas a num enteros
for i in range(0,len(lista)):
    lista[i] = int(lista[i])

maximo = lista[0]
pos_max = 0
# bucle: bucar el num maximo
for pos in range(0,len(lista)):
    candidato = lista[pos]
    if candidato > maximo:
        maximo = candidato
        pos_max = pos

# muestra el numero maximo
print(f'{maximo}, {pos_max}')