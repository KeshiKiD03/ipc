#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio UF1
# 02 estructures sequecials
# Ex9
# Cristian Fernando Condolo Jimenez
# 08/10/2020
# 
# Descripcion: Un programa que realice la conversion de pies a metros.
#
# E.E. 1 pies float >= 0.
#
# Juego de pruebas
# Entrada 	 | 	Sortida
# pies		 |
# 1 * 0.3048 | 0.3048
# 0 * 	 	 | 0	
# 13 * 	 	 | 3.9624
# 256 *  	 | 78.0288
# 1000 * 	 | 304.8

# Programa
conversion = 0.3048	# pies que son 1 metro
# lee los pies
pies = float(input('Pies: '))
# pasar de pies a metros
metros = pies * conversion
print(metros)
