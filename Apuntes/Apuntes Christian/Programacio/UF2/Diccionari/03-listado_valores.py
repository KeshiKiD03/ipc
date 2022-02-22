#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Exercicis de diccionaris
# Ex3
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 11/05/2021
# 
# Descripcion:
# Haz un funcion que nos devuelva una lista de todos los valores de un diccioanrio.
# Si un valor esta repetido, solo tiene que salir una vez. 
#
# Version: 1

# Juego de pruebas
# Entrada                               Salida
# 'dos':2 ,'uno':1 ,'tres':3 , 'uno':1  [2, 1, 3]

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
    lista_valores = []

    # bucle: recorrer todo el diccionario
    for valor in diccionari.values():
        if valor not in lista_valores:
            lista_valores.append(valor)
    
    # devolvel lista de claves
    return lista_valores

# PROGRAMA PRINCIPAL
diccionario = {'dos':2,'uno':1,'tres':3, 'uno':1}
print(clau_diccionari(diccionario))