#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 03 estructura alternativa
# Ex1
# Cristian Fernando Condolo Jimenez
# 27/10/2020
# 
# Descripcion: leer un numero real y escribir si es un numero positivo o no.
#
# E.E. 1 int

# Juego de Pruebas
# Entrada 	| Salida
# 12		| positivo	 			
# 0			| positivo	
# -10		| no es positivo

# Programa
# leer un numero por entrada
num = int(input())

# ver si el numero es positivo
if num >= 0:
	print('positivo')
# o que no sea positivo
else:
	print('no es positivo')
