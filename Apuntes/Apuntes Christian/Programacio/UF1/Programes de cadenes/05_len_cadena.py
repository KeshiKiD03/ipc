#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes de cadenes
# Exercici5
# Cristian Fernando Condolo Jimenez
# isx41016667
# 15/12/2020
# 
# Descripcion:
# Hacer un programa que haga lo mismo que la funcio len().

# Juego de pruebas
# entrada           salida
# hola buenos dias  16
# aaaaa             5
# que bien          8

# E.E. 1 str (frase)p

# Programa
# leer la frase/cadena
cadena = input()

num_len = 0
#bucle
for c in cadena:
    num_len += 1

# mostra len() de la cadena
print(num_len)
