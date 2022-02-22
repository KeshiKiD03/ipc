#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes de cadenes
# Exercici7
# Cristian Fernando Condolo Jimenez
# isx41016667
# 23/12/2020
# 
# Descripcion:
# .

# Juego de pruebas
# entrada   salida
# 

# E.E. 1 str (frase)

# Programa
# leer los numeros del dni
numeros = input()

suma = 0
# bucle: sumar numeros del dni
for num in numeros:
    suma = suma + int(num)

# buscar la letra final del dni
letra = 'TRWAGMYFPDXBNJZSQVHLCKE'
resto = suma % 23

# mostrar la letra final del dni
print(letra[resto])