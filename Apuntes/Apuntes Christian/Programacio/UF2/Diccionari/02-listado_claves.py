#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Exercicis de diccionaris
# Ex2
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 11/05/2021
# 
# Descripcion:
# Haz un funcion que nos devuelva una lista de todos las claves de un diccioanrio. 
#
# Version: 1

# Juego de pruebas
# Entrada                       Salida
# 'dos':2 ,'uno':1 ,'tres':3    ['dos', 'uno', 'tres']

# Programa
# FUNCIONES
def clau_diccionari(diccionari):
    '''
    Funcion que devuleve una lista de
    todos las claves de un diccionario.
    in: dic
    out: lst (lista de claves)
    '''
    # crear una lista para las claves
    lista_claves = []

    # bucle: recorrer todo el diccionario
    for elem in diccionari:
        lista_claves.append(elem)
    
    # devolvel lista de claves
    return lista_claves

# PROGRAMA PRINCIPAL
diccionario = {'dos':2,'uno':1,'tres':3}
print(clau_diccionari(diccionario))