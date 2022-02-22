#!/usr/bin/python3
#-*- coding: utf-8-*-

# Autor: Cristian Condolo
# Data: curs 2020-21
    
# Descripción: 
'''
Mòdulo para cifrar i descifrar mensajes basados en el codigo binario
Podemos escoger el mètodo de cifrado pasando la función de cifrado que 
queremos a la función traductor
'''
	
def convertir_a_binari(para, zero, un):
	'''
	Función que pasa una cadena escrita en codigo binario utilizando dos
	símbolos cualquiera a codigo binario de 0's y 1's
	Input: (str, str, str) (Codigo binario creado con 2 caràcteres, 
	caràcter que represeta el zero, caràcter del '1')
	Output: str (codigo binario de zeros y unos)
	'''
	binari = ''
	# bucle: pasar el codigo a binario
	for c in para:
		if c == zero: # los caracteres zero
			carac = '0'
		else:
			carac = '1' # los caracteres uno
		# añadimos al codigo binario
		binari = binari + carac
	# devolvemos el codigo binario
	return binari
	
def traductor(missatge_x, zero, un, len_pack, len_sep, desxifrar_car):
	'''
	Función que traduce un mensaje cifrado en codigo ‘binario’ a texto.
	El mensaje tiene separadores entre letras de longitud len_sep y se 
	escribe	empleando para cada caràcter una cadena de longitud len_pack.
	
	Input: (str, str, str, int, int, función) (mensaje cifrado segun el codigo 
	(correcto), caràcter del 0, caràcter del 1, int >= 0, int >=0, función
	que utilizamos para descifrar un caràcter)
	
	Output: str (Mensaje de texto descifrado)
	'''
	missatge_d = ''
	llargada = len_sep + len_pack # longitud total de cada parte
	# bucle: recortar segun los caracteres
	for i in range(0, len(missatge_x), llargada):
		pack = missatge_x[i + len_sep: i + llargada]
		# paso a binario un set
		bina = convertir_a_binari(pack, zero, un)
		# paso de binario a decimal
		deci = int(bina, 2)
		# descifro el caràcter
		car = desxifrar_car(deci)
		missatge_d = missatge_d + car # añadir al mensaje
	
	# devolver mensaje descrifrado
	return missatge_d
	
def posicio_alfabet(n):
	'''
	Devuelve el caràcter corresponiente al codigo numèrico segun nostre cifrado
	En este caso, la posición de la letra mayuscula
	Input: int 
	Output: str (letra mayuscula corresponeinte)
	'''
	LLETRES = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'  #LA A vale 1
	return LLETRES[n % (len(LLETRES) -1 )  ] #hay 26 letras i len(LLETRES es 27)
	
# TEST DRIVER
if __name__ == '__main__':
	# test driver de convertir_a_binari:
	if False:
		# mensaje cifrado de paraguas: Blanc(Blanco) y Vermell(Rojo)
		print(convertir_a_binari('BBBBBBBVBBBBBBBBBBBVBBBBBVBBVBBBBBBBBVBV','B', 'V'))
		# mensaje cifrado invisible: espacio( ) y tabulacion(\t)
		print(convertir_a_binari('     	 	        	  	      			      	 	           	'
		,' ', '\t'))
	# test driver de traductor
	if True:
		# en este caso utilizaremos la posición del alfabeto
		print(traductor('BBBBBBBVBBBBBBBBBBBVBBBBBVBBVBBBBBBBBVBV','B', 'V', 7, 3, posicio_alfabet))
		# en este caso utiliamos el codigo ASCII
		print(traductor(' 		  	   		    	 			 		  		    	 		 			  			 	    	      		  	   		  	 	  	      		 		    	  			 		  	 	 			  		 		   		 		 				 		 		   		    	'
		,' ', '\t', 8, 0, chr))


