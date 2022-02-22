#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
# M03 Programacio UF1
# Practica examen1
# Ex5
# Cristian Fernando Condolo Jimenez
# 21/10/2020
# 
# Descripcion: estan planeado una boda y quieren que todos los invitados ocupen mesa de 12 en 12. 
# Hacer un programa que muestre cuantas mesas ocuparan los invitados y cuantos invitados quedara
# en la ultima mesa.  
#
# E.E. 1 int invitados > 0

# Programa
# leer los invitados que asistiran a la boda
invitados = int(input('Invitados: '))
personas_mesa = 12

# calcular cuantas mesas ocuparan y las personas que sobran en la ultima mesa
mesas = invitados // personas_mesa
ultima_mesa = invitados % personas_mesa

# mostrar las mesas y las personas sobrantes
print(f'mesas ocupadas: {mesas} mesas, ultima mesa: {ultima_mesa} invitados')
