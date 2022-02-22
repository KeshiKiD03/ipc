#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Exercicis de nadal
# Exercici2
# Cristian Fernando Condolo Jimenez
# isx41016667
# 24/12/2020

# Descripcion:
# Cuenta el numero de palabras que hay dentro de una cadena de texto que lea (las palabras siempres estan
# separadas por un o dos espacio en blanco)

# Juego de pruebas
# entrada                   salida
# feliz navidad             5
# feliz año nuevo           7
# hola buenos dias a todos  10
# hola que tal              5
# hhhh hh hhhh              0
# llapis                    2
# aaaaaeee                  9
#                           0 

# E.E. 1 str(cadena de texto)

# Programa
# leer la frase / cadena de texto
cadena = input()
cadena = cadena.lower() # minimizamos la cadena para que cuente tambien las mayusculas
cadena_vocal = 'aeiou'

cont = 0
# bucle: contar las vocales de la cadena
for c in cadena:
    # si el caracter es una vocal
    if c in cadena_vocal:
        # contar
        cont += 1

# mostra cuantas vocales hay
print(cont)

'''
# leer frace
cadena = input()

cont = 0
# bucle: caracter por caracter
for c in cadena:
    # si el caracter es una vocal
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        # contar
        cont += 1

# mostrar cuantas vocales hay
print(cont)
'''