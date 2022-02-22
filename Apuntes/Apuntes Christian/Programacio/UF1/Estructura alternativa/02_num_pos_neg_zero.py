#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 03 estructura alternativa
# Ex2
# Cristian Fernando Condolo Jimenez
# 27/10/2020
# 
# Descripcion: leer un numero real y escribir si es un numero positivo, negativo o zero.
#
# E.E. 1 int

# Juego de Pruebas
# Entrada 	| Salida
# 12		| positivo	 			
# 0			| zero	
# -10		| negativo

# Programa
# escribir un numero por entrada
a = int(input())

# averiguar si es un numero positvo o zero
if a > 0:
	print('positivo')
elif a == 0:
	print('zero')
# en caso de que sea negativo
else:
	print('negatiu')
