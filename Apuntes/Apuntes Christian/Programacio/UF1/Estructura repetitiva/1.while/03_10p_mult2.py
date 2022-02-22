#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# 04 estructura repetitiva
# Exercici3
# Cristian Fernando Condolo Jimenez
# 16/11/2020
# 
# Descripcion:
# Escribir los multiplos de dos menors o iguals a 100
#
# E.E. No hay entradas

# Juego de pruebas
# Entrada       Salida
#               2,4,6,8,10,12,14,16,18,20

# Programa
# leer los datos
multiplo = 2
cont = 0

# bucle: mostrar los multiplos de 2
while cont < 10:
    # buscar los multiplos de dos
    if multiplo % 2 == 0:
        # cuento
        cont += 1
        # muestro
        print(multiplo)
    multiplo += 1