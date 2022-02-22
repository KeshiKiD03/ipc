#!/usr/bin/python3
# 07/25/2021
# Cristian Condolo
# M05 Programacio- UF2 
# Descripcion:
# Ordenar listas con sort()/sorted()
# ====================================
# list.sort(key=..., reverse=...)
lista_int = [9,7,2,8,1]
lista_int.sort()
print(lista_int) # [1, 2, 7, 8, 9]
print()

# sorted(list, key=..., reverse=...)
lista_int = [10,8,3,9,2]
lista_int = sorted(lista_int)
print(lista_int) # [2, 3, 8, 9, 10]
print()