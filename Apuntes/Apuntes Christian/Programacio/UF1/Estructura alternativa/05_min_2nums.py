#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 03 estructura alternativa
# Ex5
# Cristian Fernando Condolo Jimenez
# 28/10/2020
# 
# Descripcion: leer dos numeros reales i escribir el mas pequeño de los dos(el minimo).
#
# EE 2 int

# Juego de Pruebas
# Entrada 		Salida
# n1 	n2 	| 	
# 10	6	| 	6
# 0		0	| 	0
# -1  1248	|	-1

# Programa
# leer los dos numeros por entrada
num1 = int(input('Numero1: '))	
num2 = int(input('Numero2: '))
minimo = num1

# comprobar cual de los dos numeros es el mas pequeño
if num2 < minimo:
	minimo = num2

# mostrar cual es el mas pequeño
print(minimo)
