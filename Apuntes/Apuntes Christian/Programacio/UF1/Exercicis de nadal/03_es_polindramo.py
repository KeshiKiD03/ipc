#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Exercicis de nadal
# Exercici3
# Cristian Fernando Condolo Jimenez
# isx41016667
# 24/12/2020

# Descripcion:
# Hacer un programa que dada una cadena nos diga si es polindramo o no.
# Una frase o cadena es polidramo si se puede leer en orden o a la inversa obteniedo la misma frase.

# Juego de pruebas
# entrada                          salida
# dabale arroz a la zorra el abad   True
# abbca                             False

# E.E. 1 str(cadena de texto)

# Programa
# leer la frase / cadena de texto
cadena = input()
es_polindramo = True

frase = ''
# bucle: sacar los espacio
for c in cadena:
    if c != ' ':
        frase = frase + c

# bucle: recorrer caracter por caracter, tambien de forma inversa
for pos in range(0,len(frase)):
    if frase[pos] != frase[-pos - 1]:
        es_polindramo = False

# mostrar si es o no es palindramo
print(es_polindramo)

'''
# esta version solo recorre hasta la mitad como maximo
i = 0
es_polindramo = True

while i < len(frase) // 2 and es_polindramo:
    if frase[i] != frase[-i - 1]:
        es_polindramo = False
    i += 1

print(es_polindramo)
'''