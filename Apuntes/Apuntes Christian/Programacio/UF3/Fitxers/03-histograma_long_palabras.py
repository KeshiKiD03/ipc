#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Fitxers
# Ex3
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 18/05/2021
# 
# Descripcion: 
#
# Version: 1.0

# Programa
from sys import argv

ARCHIVOS = ''
# comprobar si no hay fichero por argumento
if len(argv) == 1:
    ARCHIVOS = input()
else:
    ARCHIVOS = argv[1]
