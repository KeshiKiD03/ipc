#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 03 estructura alternativa
# Ex3
# Cristian Fernando Condolo Jimenez
# 27/10/2020
# 
# Descripcion: leer un numero real y escribir su valor absoluto.
#
# EE 1 int

# Juego de Pruebas
# Entrada 	| Salida
# 12		| 12	 			
# 0			| 0	
# -10		| 10

# Programa
# leer un numero por entrada
num = int(input())

# ver si el numero es negativo
if num < 0:
	num = num * -1

# mostrar su valor absoluto
print(num)
