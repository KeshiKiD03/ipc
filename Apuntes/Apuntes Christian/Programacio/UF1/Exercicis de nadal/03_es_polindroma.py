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

# E.E. 1 str(cadena de texto)

# Programa
# leer la frase / cadena de texto
cadena = input()
es_polindramo = True

nova_cadena = ''
# bucle: hacer la cadena sin espacios
for c in cadena:
    if c != ' ':
        nova_cadena = nova_cadena + c

inversa = ''
# bucle: invertir la cadena de texto
for c in cadena:
    if c != ' ':
        inversa = c + inversa

pos = 0
# bucle: comprobar si es o no es polindramo
while pos < len(nova_cadena) and es_polindramo:
    # si no es polindramo
    if nova_cadena[pos] != inversa[pos]:
        es_polindramo = False
    pos += 1

# mostra si es o no es polindramo
print(es_polindramo)