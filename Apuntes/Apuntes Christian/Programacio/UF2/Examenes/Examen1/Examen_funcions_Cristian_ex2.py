#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Examen funciones
# Exercicio2
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 13/04/2021
# 
# Descripcion:
# Fes el programa que tradueix el codi parachute (ésa dir, defineix la funció traductor icrida-la tres vegades).
# Per a provar-la, tens el fitxer de proves que es diu missatge_parachute.txt. 
#
# Juego de pruebas
# Entrada                                                       Salida
# BBBBBBBVBBBBBBBBBBBVBBBBBVBBVBBBBBBBBVBV                      DARE
# BBBBBBVVBVBBBBBBVBBVBBBBBBBVVVBBBBBBVBBBBBBBBVBVBBBBBBBVVBBV  MIGHTY
# BBBBBVBVBBBBBBBBVBBBBBBBBBVBBVBBBBBBVVVBBBBBBBBVVVBBBBBVBBVV  THINGS

# E.E. -> str(B/V).(BBB) com separadores al inicio.

# Programa
import modul_paracaigudes

# leer el codigo por stdin, 3 veces
for i in range(3):
    codigo = input()
    print(modul_paracaigudes.traductor(codigo))