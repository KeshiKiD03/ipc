#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Exercicis de diccionaris
# Ex8
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 12/05/2021
# 
# Descripcion:
# Haz un programa que cuente las repeticiones de las palabras que
# salen en una frase. 
#
# Version: 1

# Juego de pruebas
# Entrada                           Salida
# "hola hola tres cadena tres tres" {"hola":2,"tres":3,"cadena":1}

# Programa
# FUNCIONES
def frequencia_paraula(frase):
    '''
    Funcion que cuenta las repeticiones
    de una palabra.
    in: str (frase/secuencia), str(palabra/caracter)
    out: int (repticiones)
    '''
    # crear un diccionario
    dic = {}
    # listar las palabras de la frase
    lista = frase.split()

    # bucle: recorrer palabra por palabra
    for palabra in lista:
        # si esta palanbra esta en el diccionario
        if palabra in dic:
            dic[palabra] = dic[palabra] + 1 # contar repeticion
        else:
            dic[palabra] = 1
    
    # devolver el diccionario de repeticiones de palabras
    return dic

def ordenaFreq(tupla):
    '''
    Function key que ordena un diccionario segun
    su valor.
    in:
    '''
    # ordernar por valores
    return tupla[1]

def llista_ordernada(frase):
    '''
    Funcion que ordena un diccionario
    segun sus valores.
    '''
    # crear diccionrio de repeticiones de palabras
    dic = frequencia_paraula(frase)

    # crear un lista de valores (repeticiones de palabras)
    lista = list(dic.items())

    # ordena la lista de valores
    lista.sort(key=ordenaFreq)
    
    # devuelve la lista de valores, ordenada
    return lista

# PROGRAMA PRINCIPAL
frase = "hola hola tres cadena tres tres"
print(frequencia_paraula(frase))
print(llista_ordernada(frase))