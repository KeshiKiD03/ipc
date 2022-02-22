#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M05 Programacion UF1
# 02 estructures sequecials
# Ex 4
# Cristian Fernando Condolo Jimenez
# 19/10/2020
# 
# Descripcion: dada una medida de tiempo expresada en horas, minutos y segundos, elaborar
# un programa que transforme dicha medida en una expresion correcta.
#
# E.E. 1 int(hora) >= 0 y <= 23. 2 int(min, sec) >= 0 y <= 59.

# Programa
# leer los datos por ordenador
hora =  int(input('Horas: ')) 
minutos =  int(input('Minutos: ')) 
segundos =  int(input('Segundo: ')) 

# calcular el tiempo
min_rest = segundos // 60
sec_f = segundos % 60
minutos = minutos + min_rest
hora_rest = minutos // 60
min_f = minutos % 60
hora_f = hora + hora_rest

# mostrar la expresion correcta
print(f'{hora_f}h {min_f}m {sec_f}s')
