#!/usr/bin/python3
#-*- coding: utf-8-*-

# Autor: Escola del Treball
# Data: curs 2020-21

''' 
Mòdul amb funcions per a desxifrar missatges en codi 'paracaigudes' i 
binaris de ' ' i '\t'
'''

def baseb_to_deci(num_b, b):
	'''
	Funció que passa un nonbre escrit en una base b a decimal
	Input: str, int(num_b: cadena en base b correcta. Lletres minúscules,
	la base b pot ser entre 2 i qualsevol nombre que les lletres minúscules 
	puguin representar-ne els dígits, o inclús majors si escollim els
	
	Output: int
	'''
	
	total = 0
	exponent = len(num_b) - 1
	for car in num_b:
		
		if car >= '0' and car <= '9':
			total = total + int(car) * b ** exponent		
		else:
			#trampeta
			total = total + (ord(car) - ord('a') + 10) * b ** exponent
	
		exponent = exponent - 1
	return total
	
def convertir_a_binari(para,zero,un):
	'''
	Funció que passa un nombre escrit en parachute binari
	Input: Codi parachute correcte (B/V)
	Output: codi binari
	'''
	ZERO = zero
	UN = un

	binario = ''
	# bucle: pasar el blanco y rojo a 0 y 1
	for car in para:
		# si es BLANCO
		if car == ZERO:
			binario = binario + '0'
		# si es ROJO
		elif car == UN:
			binario = binario + '1'
	return binario

	
def traductor(missatge_x):
	'''
	Funció que tradueix un missatge xifrat en codi ‘paracaigudes’ a text.
	El missatge té separadors entre lletres de longitud 3 i s'escriu emprant
	per a cada caràcter una cadena de longitud 7.
	Input: str (missatge xifrat segons el codi (correcte))
	Output: Missatge desxifrat
    '''
	LEN_PACK = 7
	LEN_SEP = 3

	mensaje = ''
	# bucle: recortar codigo a 7 bits como 3 de separador
	for i in range(0,len(missatge_x),LEN_PACK + LEN_SEP):
		# passar a binario un set
		num_2 = convertir_a_binari(missatge_x[i + LEN_SEP:i + LEN_PACK + LEN_SEP],' ','\t')

		# pasar de binario a decimal
		num = baseb_to_deci(num_2,2)

		# pasar el num a letra
		letra = desxifrar_car(num)

		# añadir al mensaje
		mensaje = mensaje + letra

	return mensaje

def desxifrar_car(n):
	'''
	Retorna el caràcter corresponent al codi ASIIC
	Input: int
	Output: str (lletra majúscula corresponent)
	'''
	return chr(n)

# TEST DRIVER
if __name__ == '__main__':
	if True:
		# Test driver de convertir_a_binari
		print('     	:',convertir_a_binari('     	 ',' ','\t'))
		print('     	:',convertir_a_binari('   	  	',' ','\t'))
		print()
	if False:
		# Test driver de baseb_to_deci
		print('0000100:',baseb_to_deci('0000100',2))
		print('0000001:',baseb_to_deci('0000001',2))
		print('0010010:',baseb_to_deci('0010010',2))
		print('0000101:',baseb_to_deci('0000101',2))
		print()
	if False:
		# Test driver de desxifrar_car
		print('4:',desxifrar_car(4))
		print('1:',desxifrar_car(1))
		print('18:',desxifrar_car(18))
		print('5:',desxifrar_car(5))
		print()
	if False:
		# Test driver de traductor
		print('BBBBBBBVBBBBBBBBBBBVBBBBBVBBVBBBBBBBBVBV:',traductor('BBBBBBBVBBBBBBBBBBBVBBBBBVBBVBBBBBBBBVBV'))
		print()