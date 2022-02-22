#!/usr/bin/python3
#-*- coding: utf-8-*-

# Autor: Escola del Treball
# Data: curs 2020-21
    
# Descripció: Utilitzamos el mòdulo traductor per a traducir un mensaje escrito en codigo
# binario 'normal'
# como que el codigo binario 'normal' utiliza el codigo ASCII, hace falta que en el mòdulo
# comentamos la función desxifra_car que no nos va bien
# Comprueba que puedes descifrar el mensaje binario de la carpeta
import xifratge

print(xifratge.traductor(input(), '0', '1', 8, 0, chr))
