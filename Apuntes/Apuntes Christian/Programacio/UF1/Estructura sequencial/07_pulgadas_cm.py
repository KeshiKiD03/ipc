#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio UF1
# 02 estructures sequecials
# Ex7
# Cristian Fernando Condolo Jimenez
# 08/10/2020
# 
# Descripcion: Un programa que realice la conversion de pulgadas a centimetros.
#
# E.E. 1 pulgada float >= 0
#
# Juego de pruebas
# Entrada 	 | 	Sortida
# plg		 |
# 1 * 2.54 	 |	2.54
# 0 * 	 	 | 	0
# 13 * 	 	 |	33.02
# 256 *  	 |	650.24
# 1000 * 	 |	2540

# Programa
conversion = 2.54	# centimetros que son 1 pulgada
# leer las pulgadas
plg = float(input('Pulgadas: '))
# pasar de pulgadas a centimetro
final = plg * conversion
print(final)




