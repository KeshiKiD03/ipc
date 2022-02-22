#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio UF1
# 02 estructures sequecials
# Ex8
# Cristian Fernando Condolo Jimenez
# 08/10/2020
# 
# Descripcion: Un programa que realice la conversion de metros a pies.
#
# E.E. 1 metro float >= 0
#
# Juego de pruebas
# Entrada 	 | 	Sortida
# m			 |
# 1 * 3.28084|	3.28084 	
# 0 * 	 	 |	0
# 13 * 	 	 |	42.6509
# 256 *  	 |	839.895
# 1000 * 	 |	3280.84

# Programa
conversion = 3.28084	# pies son 1 metro
# leer los metros
m = float(input('Metros: '))
# pasar de metros a pies
final = m * conversion
print(final)
