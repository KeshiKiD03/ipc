#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Sort() Sorted()
# Peluixos gegants
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 10/05/2021
# 
# Descripcion:
# Leer por entrada un n y leer 3 n precio, y aplicar oferta de 3x2 (quitar el mas barato).
#
# Version: 1.0

# Juego de pruebas
# Entrada Salida

# E.E. 1 int, 3 x 1 ints 

# Programa
# FUNCIONES

def preu_triple(triplet):
    '''
    '''
    return triplet[0] + triplet[1]

# PROGRAMA PRINCIPAL
# leer n y los 3 n precios
lista_precio = [[7,7,9]]

for caso in lista_precio:
    caso.sort(reverse=True)
    precio = 0
    for i in range(0,len(caso)+1,3):
        precio = preu_triple(caso)
    
print(precio)