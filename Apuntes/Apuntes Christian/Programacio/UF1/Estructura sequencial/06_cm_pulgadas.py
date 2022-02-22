#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio UF1
# 02 estructures sequecials
# Ex6
# Cristian Fernando Condolo Jimenez
# 08/10/2020
# 
# Descripcion: Un programa que realice la conversion de cm a pulgadas.
#
# E.E. 1 cm float >= 0
#
# Juego de pruebas
# Entrada 	 | 	Sortida
# cm		 |
# 1 * 0.393701|	0.39737
# 0 * 		 |	0.0
# 13 * 		 |	5.118113
# 256 * 	 |	100.787
# 1000 * 	 |	393.701

# Programa
conversion = 0.393701 # pulgadas que son 1 cm
# leer los centimetros
cm = float(input('Centimetros: '))
# pasar de centimetros a pulgadas
final = cm * conversion
print(final)
