#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio
# Exercicis de nadal
# Exercici2
# Cristian Fernando Condolo Jimenez
# isx41016667
# 24/12/2020

# Descripcion:
# Cuenta el numero de palabras que hay dentro de una cadena de texto que lea (las palabras siempres estan
# separadas por un o dos espacio en blanco)

# Juego de pruebas
# entrada                   salida
# feliz navidad             a:2, e:1, i:2, o:0, u:0
# feliz año nuevo           a:1, e:2, i:1, o:2, u:1
# hola buenos dias a todos  a:3, e:1, i:1, o:4, u:1
# hola que tal              a:2, e:1, i:0, o:1, u:1
# hhhh hh hhhh              a:0, e:0, i:0, o:0, u:0
# llapis                    a:1, e:0, i:1, o:0, u:0
# aaaaaeee                  a:6, e:3, i:0, o:0, u:0
#                           a:0, e:0, i:0, o:0, u:0

# E.E. 1 str(cadena de texto)

# Programa
# leer la frase / cadena de texto
cadena = input()

a = 0
e = 0
i = 0
o = 0
u = 0
# bucle: contar las vocales de la cadena
for c in cadena:
    # si el caracter es una vocal
    if c == 'a':
        a += 1
    elif c == 'e':
        e += 1
    elif c == 'i':
        i += 1
    elif c == 'o':
        o += 1
    elif c == 'u':
        u += 1

# mostra cuantas vocales hay
print('a:',a)
print('e:',e)
print('i:',i)
print('o:',o)
print('u:',u)


'''
cadena = input()
cadena = cadena.lower()

cadena_vocals = 'aeiou'
cadena_resultado = [0,0,0,0,0]
for pos in range(0,len(cadena_vocals)):
    for c in cadena:
        if c == cadena_vocals[pos]:
            cadena_resultado[pos] += 1

print(cadena_resultado)
'''