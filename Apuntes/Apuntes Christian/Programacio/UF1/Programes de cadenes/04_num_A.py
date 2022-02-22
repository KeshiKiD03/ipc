#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes de cadenes
# Exercici4
# Cristian Fernando Condolo Jimenez
# isx41016667
# 15/12/2020
# 
# Descripcion:
# Leer una frase i contar la cantidad de 'a' que hay.

# Juego de pruebas
# entrada           salida
# hola buenos dias  2
# aaaaa             5
# que bien          0

# E.E. 1 str (frase)

# Programa
# leer la frase/cadena
cadena = input()

num_a = 0
#bucle
for c in cadena:
    if c == 'a':
        num_a = num_a + 1

# cuantas a hay en la cadena?
print(num_a)

