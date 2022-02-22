#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici2
# Cristian Fernando Condolo Jimenez
# 13/11/2020
# 
# Descripcion:
# escribir los multiplos de 2 menores o iguales a 100

# leer el numero
limit = 100
n= 1

# mostra los multiplos de 2:
while n < limit:
	# si es multiplo de 2
	if n % 2 == 0:
		# mostrar
		print(n)
	n = n + 1
