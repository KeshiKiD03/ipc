#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Programes amb for in
# Cristian Fernando Condolo Jimenez
# 01/12/2020
# 
# Descripcion:
# Realizar un programa que proporcione el desglose en billetes y monedas de
# una cantidad de euros.

# Programa
# leer los euros
euros = int(input())

# bucle: por cada billete y moneda
for valor in (500,200,100,50,20,10,5,2,1):
    # calculamos la cant de billetes
    c_billetes = euros // valor
    # calculamos lo que sobre
    euros = euros % valor
    # mostrar la cantidad
    if c_billetes > 0:
        print(c_billetes,'de',valor)