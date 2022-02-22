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
import sys

AMPLITUD = 81		#l'amplitud de la pantalla
MISSATGE = f'Usage: felicitacio nadalena num {AMPLITUD // 2}'
CARACTER = '*'
BLANC = ' '
LLARGADA_TRONC = 4
AMPLADA_TRONC = 3

# CONTROL D'ERRORS
# perque no peti si no hi ha argument, cal comprovar la llargada de sys.argv
if len(sys.argv) < 2:
    print(MISSATGE)
    exit(1)

# com que ho hem comprovat abans aquesta linia no petara
cadena = sys.argv[1]

# comprovar que es un enter i major de 0
if not cadena.isdigit():
    print(MISSATGE)
    exit(1)

# ara no petara al fer int()
llargada = int(cadena)

meitat = AMPLITUD // 2 
# descartem els enters que no ens van bé
if llargada > meitat :
	print(MISSATGE)
	exit(1)

# PROGRAMA PRINCIPAL
blancs = meitat
punts = 1

# dibuixo la copa
for i in range(0, llargada):
	print(f'{BLANC * blancs}{CARACTER * punts}')
	blancs = blancs - 1
	punts = punts + 2
	
#dibuixo el tronc
for i in range(0, LLARGADA_TRONC):
	print(f'{(meitat - 1) * BLANC}{AMPLADA_TRONC * CARACTER}')