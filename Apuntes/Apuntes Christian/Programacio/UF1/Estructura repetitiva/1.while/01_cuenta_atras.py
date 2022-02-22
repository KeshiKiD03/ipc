#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici1
# Cristian Fernando Condolo Jimenez
# 13/11/2020
# 
# Descripcion:
# Simular una cuenta atras.

# Juego de pruebas
# entrada   salida
# 3         3,2,1,0 BUUUM
# 7         7,6,5,4,3,2,1 BUUM

# Programa
# leer el numero
cont = int(input())

# comenzar con la cuenta atras
while cont >= 0:
    print(cont)
    cont -= 1
print('BUUM')