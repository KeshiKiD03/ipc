#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Exercicis de diccionaris
# Ex1
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 11/05/2021
# 
# Descripcion:
# Haz un funcion que dado un diccionario y un valor, diga si el valor esta o 
# no en el diccionario. 
#
# Version: 1

# Juego de pruebas
# Entrada                              Salida
# dic                           valor
# 'hola':0,'a':1,'tothom,':2    2       True

# E.E. 1 dic, 1 str 

# Programa
# FUNCIONES
def valor_in_diccionari(diccionari,valor):
    '''
    Funcion que dice si un valor es dentro de
    un diccionario
    in: dic(diccionario), str (valor)
    out: boolean
    '''
    # crear una lista con los valores del diccionario
    lst_valores = diccionari.values()

    # comprueba si esta o no dentro de la lista de valores
    return valor in lst_valores
    

# PROGRAMA PRINCIPAL
diccionario = {'hola':0,'a':1,'tothom,':2}
valor = 2
print(valor_in_diccionari(diccionario,valor))

# TEST DRIVER
if __name__ == '__main__':
    if False:
        print(valor_in_diccionari({'hola':0,'a':1,'tothom,':2},2))
        print(valor_in_diccionari({},))
        print(valor_in_diccionari({},))
        print(valor_in_diccionari({},))
        print()