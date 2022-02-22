#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 03 estructura alternativa
# Ex7
# Cristian Fernando Condolo Jimenez
# 29/10/2020
# 
# Descripcion: leer un numero real i decir si es un numero entero o no.
#
# EE 1 int >= 0

# Juego de Pruebas
# Entrada 		Salida
# 12		| Entero
# 1.59		| Float
# 0			| Entero
# 0.0		| Float

# Programa
# leer el numero real por entrada
num = float(input())

# comprobar si el numero es entero o no
if (num % 1) == 0:
	print('Entero')
else:
	print('Float')
