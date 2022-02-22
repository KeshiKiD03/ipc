#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio UF1
# 02 estructures sequecials
# Ex11
# Cristian Fernando Condolo Jimenez
# 08/10/2020
# 
# Descripcion: Un programa que realice la conversion de libras a kilogramos.
#
# E.E. 1 libras float >= 0.
#
# Juego de pruebas
# Entrada 	 | 	Sortida
# k			 |
# 1 * 0.453592| 0.453592
# 0 * 	 	 | 0
# 13 * 	 	 | 5.8967
# 256 *  	 | 116.12
# 1000 * 	 | 453.592

# Programa
conversion = 0.453592 	# libras que son 1 kilogramo
# lee las libras
libras = float(input('Libras: '))
# pasar de libras a kilogramos
kilogramos = libras * conversion
print(kilogramos)
