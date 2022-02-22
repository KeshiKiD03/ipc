#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes amb for in
# Cristian Fernando Condolo Jimenez
# 01/12/2020
# 
# Descripcion:
# Realizar una cuenta atras.

# Juego de pruebas
# Entrada   Salida

# E.E. 1 numero int > 0

# Programa
# leer el ultimo numero
n = int(input())

# bucle: hacer la cuenta atras
for i in range(n,-1,-1):
    print(i)
print('BUUM')