#!/usr/bin/python3

# Autor: Escola del Treball
# Data: curs 2020-21

# programa per a buscar el màxim

import funcions_racionals

entrada = input().split()

racionals = []

for paraula in entrada:
	if funcions_racionals.es_racional_valid(paraula):
		racionals.append(paraula)

print(racionals)

print(funcions_racionals.maxim_rac(racionals))
