#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Exercicis de nadal
# Exercici1
# Cristian Fernando Condolo Jimenez
# isx41016667
# 24/12/2020

# Descripcion:
# Cuenta el numero de palabras que hay dentro de una cadena de texto que lea (las palabras siempres estan
# separadas por un o dos espacio en blanco)

# Juego de pruebas
# entrada                   salida
# feliz navidad             2
# feliz año nuevo           3
# hola buenos dias a todos  5

# E.E. 1 str(cadena de texto)

# Programa
# leer la frase / cadena de texto
cadena = input()

anterior = ' ' # inicializamos el anterior en el espacio para contar la primera
cont = 0
# bucle: recorrer caracter por caracter
for c in cadena:
    # en una palabra nueva, si el anterior es un espacio y la actual no
    if anterior == ' ' and c != ' ':
        cont += 1
    anterior = c

# mostrar cuantas palabras hay en una cadena
print(cont)