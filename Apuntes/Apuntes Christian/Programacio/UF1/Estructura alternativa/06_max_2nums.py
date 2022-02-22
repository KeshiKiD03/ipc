#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 03 estructura alternativa
# Ex6
# Cristian Fernando Condolo Jimenez
# 28/10/2020
# 
# Descripcion: leer dos numeros reales i escribir el mas grande de los dos(el maximo).
#
# EE 2 int

# Juego de Pruebas
# Entrada 		Salida
# n1 	n2 	| 	
# 10	6	| 	10
# 0		0	| 	0
# -1  1248	|	1248

# Programa
# leer los dos numeros por entrada
num1 = int(input('Numero1: '))	
num2 = int(input('Numero2: '))
maximo = num1

# comprobar cual de los dos numeros es el mas grande
if num2 > maximo:
	maximo = num2

# mostrar cual es el mas grande
print(maximo)
