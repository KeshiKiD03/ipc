#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# Escola del Treball 2020-21
#
# M03 Programacio
# Examen funciones
# Exercicio3
#
# Cristian Fernando Condolo Jimenez
# isx41016667
# 13/04/2021
# 
# Descripcion:
# Fes un modul_traductor_ex3 on modifiquis les funcionsque calguin i un programaon desxifris el missatge que es troba en el fitxer missatge_secret_1.txt
# Com pots veure si obres el fitxer, conté 2 paraules. 
#
# Juego de pruebas
# Entrada   Salida
#      	 	        	  	      			      	 	           	--> TINTA
#       	  	      			      	 		       	  	     	  		      	  	        	       		         	 	    --> INVISIBLE

# E.E. str (' '/'\t')

# Programa
import modul_exercici3

# leer el codigo por stdin, 3 veces
for i in range(2):
    codigo = input()
    print(modul_exercici3.traductor(codigo))