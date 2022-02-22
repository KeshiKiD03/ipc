#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Examen funciones
# Exercicio4
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 13/04/2021
# 
# Descripcion:
# Lo mateix en el ex3. Pero en aquest cas, l’únic que hem de modificar del traductor és la funció que descodifica un caràcter, que en comptes de retornar la lletra 
# segons la posició ens hauria deretornar el caràcter segons el codi ASCII.
#
# Juego de pruebas
# Entrada   Salida
#  

# E.E. str (' '/'\t')

# Programa
import modul_exercici4

# leer el codigo por stdin
codigo = input()
print(modul_exercici4.traductor(codigo))