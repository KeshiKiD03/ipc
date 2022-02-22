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
cadena = ' ' + cadena

cont = 0
# bucle: contar las palabras
for pos in range(0,len(cadena)):
    # si es un espacio
    if cadena[pos] == ' ':
        # si si despues del espacio hay una letra
        if cadena[pos + 1] not in " ,.?!-'":
            # cuenta palabra
            cont += 1

# muestra cuantas palabras hay
print(cont)