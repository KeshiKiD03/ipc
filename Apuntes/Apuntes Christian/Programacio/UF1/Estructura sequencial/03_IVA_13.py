#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M05 Programacion UF1
# 02 estructures sequecials
# Ex 3
# Cristian Fernando Condolo Jimenez
# 19/10/2020
# 
# Descripcion: programa que pida el precio de un articulo y calcule su valor aplicandole
# un 13% de IVA.
#
# E.E. 1 float(precio) >= 0.

# Juego de Prueba
# Entrada   |   Salida
# precio    |   13%
# 11.16     |   12.61

# Programa
# leer los datos
precio = float(input('Precio: '))
iva = 13 / 100

# calcular el valor aplicando el IVA
precio_total = precio + (precio * iva)

# mostrar el precio total
print(precio_total)
