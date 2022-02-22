#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Exercicis de nadal
# Felicitacio nadalenca
# Cristian Fernando Condolo Jimenez
# isx41016667
# 23/12/2020
# 
# Descripcion:
# Hacer un programa que pase un numero entero positivo y dibuje un aveto de navidad.

# Juego de pruebas
# entrada   salida
# 6              *
#               ***
#              *****
#             *******
#            *********
#           ***********
#               ***
#               ***
#               ***
#               ***

# E.E. 1 num int

# Programa
# leer el numero entero
num = int(input())
copa = '*'
tronco = '***'
distancia = 81

# muestra la punta del arbol
print(" " * distancia,copa)

long_copa = distancia
# bucle: hacer la copa del arbol
for n in range(0,num):
    copa = copa + '**'
    long_copa = long_copa - 1
    print(" " * long_copa,copa)

# bucle: hacer el tronco de del arbol 
for i in range(0,4):
    print(" " * (distancia - 1),tronco)

'''
AMPLITUD = 81		#l'amplitud de la pantalla
CARACTER = '*'
BLANC = ' '
LLARGADA_TRONC = 4
AMPLADA_TRONC = 3

llargada = int(input())

meitat = AMPLITUD // 2
blancs = meitat
punts = 1

# dibuixo la copa
for i in range(0, llargada):
	print(BLANC * blancs + CARACTER * punts)
	blancs = blancs - 1
	punts = punts + 2
	
#dibuixo el tronc
for i in range(0, LLARGADA_TRONC):
	print((meitat - 1) * BLANC + AMPLADA_TRONC * CARACTER)
'''