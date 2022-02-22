#!/usr/bin/python3
#-*- coding: utf-8-*-

# Autor: Escola del Treball
# Data: curs 2020-21
    
# Descripció: 

'''
Mòdul per a xifrar i desxifrar missatges basats en el codi binari

Podem triar el mètode de xifratge passant la funció de xifratge que 
volem a la funció traductor

'''

	
def convertir_a_binari(para, zero, un):
	'''
	Funció que passa una cadena escrita en codi binari utilitzant dos
	símbols qualsevol a codi binari de 0's i 1's
	Input: (str, str, str) (Codi binari creat amb 2 caràcters qualsevol, 
	caràcter amb el que hem 'escrit' el zero, caràcter del '1')
	Output: str (codi binari de zeros i uns)
	'''
	binari = ''
	for c in para:
		if c == zero:
			carac = '0'
		else:
			carac = '1'
		binari = binari + carac
	return binari
	
def traductor(missatge_x, zero, un, len_pack, len_sep, desxifrar_car):
	'''
	Funció que tradueix un missatge xifrat en codi ‘binari’ a text.
	El missatge té separadors entre lletres de longitud len_sep i s'escriu 
	emprant	per a cada caràcter una cadena de longitud len_pack.
	
	Input: (str, str, str, int, int, funció) (missatge xifrat segons el codi 
	(correcte), caràcter del 0, caràcter del 1, int >= 0, int >=0, funció
	que utilitzem per a desxifrar un caràcter)
	
	Output: str (Missatge de text desxifrat)
	'''
	
	missatge_d = ''

	llargada = len_sep + len_pack
	# retallo segons els caràcters
	for i in range(0, len(missatge_x), llargada):
		pack = missatge_x[i + len_sep: i + llargada]
		# passo a binari un set
		bina = convertir_a_binari(pack, zero, un)
		# passo de binari a decimal
		deci = int(bina, 2)
		# desxifro el caràcter
		car = desxifrar_car(deci)
		missatge_d = missatge_d + car
		
	return missatge_d
	
def posicio_alfabet(n):
	'''
	Retorna el caràcter corresponent al codi numèric segons el nostre xifratge
	En aquest cas, la posició de la lletra majúscula
	Input: int 
	Output: str (lletra majúscula corresponent)
	'''
	LLETRES = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'  #LA A val 1
	return LLETRES[n % (len(LLETRES) -1 )  ] #hi ha 26 lletres i len(LLETRES es 27)
	

if __name__ == '__main__':
	
	# joc de proves de convertir_a_binari:

	if False:
		print(convertir_a_binari('BBBBBBBVBBBBBBBBBBBVBBBBBVBBVBBBBBBBBVBV',
		'B', 'V'))
		print(convertir_a_binari('     	 	        	  	      			      	 	           	',
		' ', '\t'))
		
	if True:
		# en aquesta prova hem utilitzar la posició de l'alfabet
		print(traductor('BBBBBBBVBBBBBBBBBBBVBBBBBVBBVBBBBBBBBVBV',
		'B', 'V', 7, 3, posicio_alfabet))
		
		# en aquesta prova hem utilitzat el codi ASCII
		print(traductor(' 		  	   		    	 			 		  		    	 		 			  			 	    	      		  	   		  	 	  	      		 		    	  			 		  	 	 			  		 		   		 		 				 		 		   		    	',
		' ', '\t', 8, 0, chr))


