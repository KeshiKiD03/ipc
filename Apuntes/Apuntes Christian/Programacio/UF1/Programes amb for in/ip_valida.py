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
# Comporbar si es un IP valida.

# Juego de pruebas
# Entrada   Salida

# E.E. 4 numero int >= 0 y <= 255

# Programa
ip_valida = True
# bucle:(4 veces)
for i in range(0,4):
    # pedidos los 4 campos de la ip
    ip = int(input())
    # validar
    if not ip >= 0 and not ip <= 255:
        ip_valida = False
print(ip_valida)